import pytest
from django.test import TestCase, Client, override_settings
from django.contrib.auth import get_user_model, authenticate
from django.urls import reverse
from django.contrib.messages import get_messages
from core.models import Role


class AuthenticationTests(TestCase):

    def setUp(self):
        self.client = Client()
        Employee = get_user_model()

        self.admin_role = Role.objects.create(name='ADMIN', visible=True)
        self.clerk_role = Role.objects.create(name='CLERK', visible=True)

        self.admin_user = Employee.objects.create_user(
            username='testadmin',
            email='admin@test.com',
            firstName='Test',
            lastName='Admin',
            role=self.admin_role,
            isActive=True,
            visible=True
        )
        self.admin_user.set_password('TestPass123!')
        self.admin_user.save()

        self.clerk_user = Employee.objects.create_user(
            username='testclerk',
            email='clerk@test.com',
            firstName='Test',
            lastName='Clerk',
            role=self.clerk_role,
            isActive=True,
            visible=True
        )
        self.clerk_user.set_password('TestPass123!')
        self.clerk_user.save()

    def test_authenticate_with_email_and_username(self):

        user = authenticate(username='testadmin', password='TestPass123!')
        self.assertIsNotNone(user)
        self.assertEqual(user.username, 'testadmin')
        self.assertEqual(user.email, 'admin@test.com')

        user = authenticate(username='admin@test.com', password='TestPass123!')
        self.assertIsNotNone(user)
        self.assertEqual(user.username, 'testadmin')
        self.assertEqual(user.email, 'admin@test.com')

        user = authenticate(username='ADMIN@TEST.COM', password='TestPass123!')
        self.assertIsNotNone(user)
        self.assertEqual(user.username, 'testadmin')

        user = authenticate(username='TESTADMIN', password='TestPass123!')
        self.assertIsNotNone(user)
        self.assertEqual(user.username, 'testadmin')

        user = authenticate(username='testadmin', password='wrongpassword')
        self.assertIsNone(user)

        user = authenticate(username='nonexistent@test.com', password='TestPass123!')
        self.assertIsNone(user)

        self.admin_user.isActive = False
        self.admin_user.save()
        user = authenticate(username='testadmin', password='TestPass123!')
        self.assertIsNone(user)

    @override_settings(RBAC_ADMIN_PATHS=['/reports/', '/employees/', '/price-adjustments/'])
    def test_rbac_denies_clerk_on_admin_paths_allows_admin(self):

        self.client.login(username='testclerk', password='TestPass123!')

        admin_paths = ['/reports/', '/employees/', '/price-adjustments/']
        for path in admin_paths:
            response = self.client.get(path, follow=True)

            self.assertRedirects(response, '/')

            messages = list(get_messages(response.wsgi_request))
            self.assertTrue(any('Access denied' in str(msg) for msg in messages))

        allowed_paths = ['/books/', '/sales/', '/customers/']
        for path in allowed_paths:
            response = self.client.get(path)

            self.assertNotEqual(response.status_code, 302)

        self.client.logout()

        self.client.login(username='testadmin', password='TestPass123!')

        for path in admin_paths:
            response = self.client.get(path)

            self.assertNotEqual(response.status_code, 302)

        for path in allowed_paths:
            response = self.client.get(path)
            self.assertNotEqual(response.status_code, 302)

    def test_rbac_redirects_unauthenticated_users(self):

        protected_paths = ['/', '/books/', '/sales/', '/customers/', '/reports/']

        for path in protected_paths:
            response = self.client.get(path)
            self.assertRedirects(response, '/login/')

        public_paths = ['/login/', '/admin/login/']
        for path in public_paths:
            response = self.client.get(path)
            self.assertNotEqual(response.url if hasattr(response, 'url') else None, '/login/')

    def test_login_flow_redirects_to_dashboard(self):

        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Username or Email')
        self.assertContains(response, 'Password')

        response = self.client.post('/login/', {
            'usernameOrEmail': 'testadmin',
            'password': 'TestPass123!'
        }, follow=True)

        self.assertRedirects(response, '/')

        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any('Welcome back' in str(msg) for msg in messages))

        self.client.logout()

        response = self.client.post('/login/', {
            'usernameOrEmail': 'clerk@test.com',
            'password': 'TestPass123!'
        }, follow=True)

        self.assertRedirects(response, '/')

        self.client.logout()

        response = self.client.post('/login/', {
            'usernameOrEmail': 'testadmin',
            'password': 'wrongpassword'
        })

        self.assertEqual(response.status_code, 200)

        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any('Invalid username/email or password' in str(msg) for msg in messages))

        response = self.client.post('/login/', {})
        self.assertEqual(response.status_code, 200)

        self.client.login(username='testadmin', password='TestPass123!')
        response = self.client.get('/login/')
        self.assertRedirects(response, '/')

    def test_logout_flow(self):

        self.client.login(username='testadmin', password='TestPass123!')

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/logout/', follow=True)

        self.assertRedirects(response, '/login/')

        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(any('logged out successfully' in str(msg) for msg in messages))

        response = self.client.get('/')
        self.assertRedirects(response, '/login/')

    def test_dashboard_role_based_content(self):

        self.client.login(username='testadmin', password='TestPass123!')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, 'Reports')
        self.assertContains(response, 'Price Adjustments')
        self.assertContains(response, 'Welcome Test')

        self.client.logout()
        self.client.login(username='testclerk', password='TestPass123!')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        self.assertNotContains(response, 'Reports')
        self.assertNotContains(response, 'Price Adjustments')

        self.assertContains(response, 'Catalog')
        self.assertContains(response, 'Sales')
        self.assertContains(response, 'Customers')
        self.assertContains(response, 'Welcome Test')

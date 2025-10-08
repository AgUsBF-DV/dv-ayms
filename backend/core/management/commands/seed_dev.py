from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from core.models import Role


class Command(BaseCommand):
    help = 'Seeds development data: roles (ADMIN, CLERK) and default users'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting development data seeding...'))

        created_count = 0
        updated_count = 0

        admin_role, admin_role_created = Role.objects.get_or_create(
            name='ADMIN',
            defaults={'visible': True}
        )
        if admin_role_created:
            created_count += 1
            self.stdout.write(f'✓ Created ADMIN role')
        else:
            self.stdout.write(f'- ADMIN role already exists')

        clerk_role, clerk_role_created = Role.objects.get_or_create(
            name='CLERK',
            defaults={'visible': True}
        )
        if clerk_role_created:
            created_count += 1
            self.stdout.write(f'✓ Created CLERK role')
        else:
            self.stdout.write(f'- CLERK role already exists')

        Employee = get_user_model()

        admin_user, admin_user_created = Employee.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@local',
                'firstName': 'System',
                'lastName': 'Administrator',
                'role': admin_role,
                'is_staff': True,
                'is_superuser': True,
                'isActive': True,
                'visible': True,
            }
        )

        if admin_user_created:
            admin_user.set_password('Admin123!')
            admin_user.save()
            created_count += 1
            self.stdout.write(f'✓ Created admin user (username: admin, password: Admin123!)')
        else:
            admin_user.set_password('Admin123!')
            admin_user.email = 'admin@local'
            admin_user.firstName = 'System'
            admin_user.lastName = 'Administrator'
            admin_user.role = admin_role
            admin_user.is_staff = True
            admin_user.is_superuser = True
            admin_user.isActive = True
            admin_user.visible = True
            admin_user.save()
            updated_count += 1
            self.stdout.write(f'- Admin user already exists, updated password and settings')

        clerk_user, clerk_user_created = Employee.objects.get_or_create(
            username='clerk',
            defaults={
                'email': 'clerk@local',
                'firstName': 'Store',
                'lastName': 'Clerk',
                'role': clerk_role,
                'is_staff': False,
                'is_superuser': False,
                'isActive': True,
                'visible': True,
            }
        )

        if clerk_user_created:
            clerk_user.set_password('Clerk123!')
            clerk_user.save()
            created_count += 1
            self.stdout.write(f'✓ Created clerk user (username: clerk, password: Clerk123!)')
        else:
            clerk_user.set_password('Clerk123!')
            clerk_user.email = 'clerk@local'
            clerk_user.firstName = 'Store'
            clerk_user.lastName = 'Clerk'
            clerk_user.role = clerk_role
            clerk_user.is_staff = False
            clerk_user.is_superuser = False
            clerk_user.isActive = True
            clerk_user.visible = True
            clerk_user.save()
            updated_count += 1
            self.stdout.write(f'- Clerk user already exists, updated password and settings')

        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS('=== SEEDING SUMMARY ==='))
        self.stdout.write(f'Created: {created_count} items')
        self.stdout.write(f'Updated: {updated_count} items')
        self.stdout.write('')
        self.stdout.write('Available users:')
        self.stdout.write(f'  Admin: username=admin, password=Admin123! (role=ADMIN)')
        self.stdout.write(f'  Clerk: username=clerk, password=Clerk123! (role=CLERK)')
        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS('Development data seeding completed successfully!'))

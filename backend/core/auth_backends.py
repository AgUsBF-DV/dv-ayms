from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q


class EmailOrUsernameBackend(ModelBackend):


    def authenticate(self, request, username=None, password=None, **kwargs):

        if username is None or password is None:
            return None

        Employee = get_user_model()

        try:

            user = Employee.objects.get(
                Q(email__iexact=username) | Q(username__iexact=username)
            )
        except Employee.DoesNotExist:

            Employee().set_password(password)
            return None
        except Employee.MultipleObjectsReturned:

            return None

        if user.check_password(password) and user.is_active:
            return user

        return None

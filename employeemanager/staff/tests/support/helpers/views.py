from django.contrib.auth.models import User

from staff.tests.factories.user import UserFactory

class ViewsHelpers():

    @staticmethod
    def force_login_for_views(client):
        """
        Forces the login for views' tests.
        Returns a superuser.
        """

        user = ViewsHelpers.get_or_create_superuser()
        client.force_login(user)

        return user

    @staticmethod
    def get_or_create_superuser():
        """
        Get a superuser from database.
        If it does not exist yet, it is created and returned.
        """

        user = UserFactory.build()
        superuser = User.objects.filter(is_superuser=True)

        if superuser.exists():
            user = superuser.first()
        else:
            user = User.objects.create_superuser(
                username=user.username,
                email=user.email,
                password='123456abcde'
            )

        return user


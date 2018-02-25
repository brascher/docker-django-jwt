from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    """
    Custom user management class.
    """

    def create_new_user(self, email, password, **exargs):
        """
        Create a new user with the supplied user information. Only email and password
        are required.
        """

        if not email or not password:
            raise ValueError("The submitted new user is missing required information")

        user = self.model(
            email=self.normalize_email(email),
            **exargs
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password, **exargs):
        """
        Overridden method in the BaseUserManager class to create a user.
        """

        exargs.setdefault("is_superuser", False)
        return self.create_new_user(email, password, **exargs)

    def create_superuser(self, email, password, **exargs):
        """
        Overridden method in the BaseUserManager class to create a super user.
        """

        exargs.setdefault("is_superuser", True)
        return self.create_new_user(email, password, **exargs)

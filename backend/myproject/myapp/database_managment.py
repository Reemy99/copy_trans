from django.contrib.auth.hashers import check_password, make_password
from django.db import IntegrityError, transaction
from .models import PrimaryUsers, UserSettings, EmailUsers  # Assuming your model is named PrimaryUser


class DatabaseManagement:
    def create_user(self, username, user_type):
        try:
            with transaction.atomic():
                user = PrimaryUsers(username=username, user_type=user_type)
                user.save()
                # No need to commit manually, as atomic block handles it
                return user.id
        except IntegrityError as e:
            # Handle integrity error (e.g., duplicate entry)
            print(f"IntegrityError: {e}")
            return False

    def create_email_user(self, username, email, password):
        try:
            with transaction.atomic():
                user = PrimaryUsers.objects.get(username=username)
                hashed_password = make_password(password)
                usersettings = EmailUsers(user=user,
                                          email_id=email,
                                          password=hashed_password)
                usersettings.save()
                # No need to commit manually, as atomic block handles it
                return True
        except IntegrityError as e:
            # Handle integrity error (e.g., duplicate entry)
            print(f"IntegrityError: {e}")
            return False

    def create_user_settings(self, id, nickname, avatar, description, is_logged):
        try:
            with transaction.atomic():
                usersettings = UserSettings(user_id=id,
                                            nickname=nickname,
                                            avatar=avatar,
                                            description=description,
                                            is_logged=is_logged)
                usersettings.save()
                # No need to commit manually, as atomic block handles it
                return True
        except IntegrityError as e:
            # Handle integrity error (e.g., duplicate entry)
            print(f"IntegrityError: {e}")
            return False

    def login_user(self, email, password):
        try:
            # Retrieve the user from the database based on the username
            user = EmailUsers.objects.get(email_id=email)

            # Check if the provided password matches the stored hashed password
            if check_password(password, user.password):
                # Passwords match, user is authenticated
                return True
            else:
                # Passwords do not match
                return False
        except EmailUsers.DoesNotExist:
            # User with the given username does not exist
            return False

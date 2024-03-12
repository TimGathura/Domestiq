from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from datetime import date, timedelta
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth import get_user_model
from django.contrib.auth import login


class CustomUser(AbstractUser):
    client_dob = models.DateField(null=True, blank=True)
    client_gender = models.CharField(max_length=10, blank=True)
    client_maritalStatus = models.CharField(max_length=20, blank=True)
    client_nationality = models.CharField(max_length=50, blank=True)
    client_acceptTerms = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.username
    
    '''

    USER_TYPE_CHOICES = [
        ('client', 'Client'),
        ('worker', 'Worker'),
    ]

    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='client')
    client_dob = models.DateField(null=True, blank=True)
    client_gender = models.CharField(max_length=10, blank=True)
    client_maritalStatus = models.CharField(max_length=20, blank=True)
    client_nationality = models.CharField(max_length=50, blank=True)
    client_acceptTerms = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.username
'''




'''   
# - - - - - WORKS GREAT FOR CLIENT REGISTRATIONS ONLY - - - - -
class CustomUser(AbstractUser):
    client_dob = models.DateField(null=True, blank=True)
    client_gender = models.CharField(max_length=10, blank=True)
    client_maritalStatus = models.CharField(max_length=20, blank=True)
    client_nationality = models.CharField(max_length=50, blank=True)
    client_acceptTerms = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.username

'''





'''
# Trial Code to automatically add groups to users based on the form they used to register
# Code to ensure dob is at least 18 years ago
def validate_age(value):
    today = date.today()
    age_limit = today - timedelta(days=(18 * 365))  # Assuming an average year has 365 days

    if value > age_limit:
        raise ValidationError("Must be at least 18 years old.")


#Client registration form
# Basically the table where the client form field info will be going
class ClientRegistration(models.Model):
    client_fname = models.CharField(max_length=255, default='First')
    client_lname = models.CharField(max_length=255, default='Last')
    client_email = models.EmailField()
    client_password = models.CharField(
        max_length=16, 
        validators=[MinLengthValidator(limit_value=8)],
        help_text="Enter a password between 8 and 16 characters."
    )
    client_confirmPassword = models.CharField(
        max_length=16, 
        validators=[MinLengthValidator(limit_value=8)],
        help_text="Enter the same password as above."
    )
    client_dob = models.DateField(
        validators=[
            MaxValueValidator(date.today(), message="Date cannot be in the future."),
            validate_age                # Reference utility function for dob (18 years)
        ]
    )
    CLIENT_GENDER_CHOICES = [('male', 'Male'), ('female', 'Female')]
    client_gender = models.CharField(max_length=10, choices=CLIENT_GENDER_CHOICES)
    CLIENT_MARITAL_STATUS_CHOICES = [('single', 'Single'), ('married', 'Married')]
    client_maritalStatus = models.CharField(max_length=10, choices=CLIENT_MARITAL_STATUS_CHOICES)
    CLIENT_NATIONALITY_CHOICES = [('kenyan', 'Kenyan'), ('foreigner', 'Foreigner')]
    client_nationality = models.CharField(max_length=10, choices=CLIENT_NATIONALITY_CHOICES)
    client_acceptTerms = models.BooleanField()


    def __str__(self):
        return f"{self.client_fname} {self.client_lname}"


# Worker registration form
# Same logic as the client form, except we will redirect to the worker dashboard now
class WorkerRegistration(models.Model):
    worker_fname = models.CharField(max_length=255, default='First')
    worker_lname = models.CharField(max_length=255, default='Last')
    worker_email = models.EmailField()
    worker_password = models.CharField(
        max_length=16, 
        validators=[MinLengthValidator(limit_value=8)],
        help_text="Enter a password between 8 and 16 characters."
    )
    worker_confirmPassword = models.CharField(
        max_length=16, 
        validators=[MinLengthValidator(limit_value=8)],
        help_text="Enter the same password as above."
    )
    worker_id = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(99999999),  # Max 8 digits (99999999)
        ]
    )
    worker_dob = models.DateField(
        validators=[
            MaxValueValidator(date.today(), message="Date cannot be in the future."),
            validate_age                # Reference utility function for dob (18 years)
        ]
    )
    WORKER_GENDER_CHOICES = [('male', 'Male'), ('female', 'Female')]
    worker_gender = models.CharField(max_length=10, choices=WORKER_GENDER_CHOICES)
    WORKER_MARITAL_STATUS_CHOICES = [('single', 'Single'), ('married', 'Married')]
    worker_maritalStatus = models.CharField(max_length=10, choices=WORKER_MARITAL_STATUS_CHOICES)
    WORKER_NATIONALITY_CHOICES = [('kenyan', 'Kenyan'), ('foreigner', 'Foreigner')]
    worker_nationality = models.CharField(max_length=10, choices=WORKER_NATIONALITY_CHOICES)
    WORKER_ROLE_CHOICES = [
        ('house help', 'House Help'),
        ('nanny', 'Nanny'),
        ('gardener', 'Gardener'),
        ('gatekeeper', 'Gatekeeper'), 
        ('chef', 'Chef'),
    ]
    worker_role = models.CharField(max_length=20, choices=WORKER_ROLE_CHOICES)
    WORKER_LOCATION_CHOICES = [
        ('nairobi', 'Nairobi'),
        ('mombasa', 'Mombasa'),
        ('kisumu', 'Kisumu'),
        ('nakuru', 'Nakuru'),
        ('eldoret', 'Eldoret'),
    ]
    worker_location = models.CharField(max_length=20, choices=WORKER_LOCATION_CHOICES)
    worker_acceptTerms = models.BooleanField()


    def __str__(self):
        return f"{self.worker_fname} {self.worker_lname}"

'''



























'''
# - - - - - WORKING BASIC REGISTRATION FUNCTIONALITY - - - - -
# Trial Code to automatically add groups to users based on the form they used to register
# Code to ensure dob is at least 18 years ago
def validate_age(value):
    today = date.today()
    age_limit = today - timedelta(days=(18 * 365))  # Assuming an average year has 365 days

    if value > age_limit:
        raise ValidationError("Must be at least 18 years old.")


#Client registration form
# Basically the table where the client form field info will be going
class ClientRegistration(models.Model):
    client_fname = models.CharField(max_length=255, default='First')
    client_lname = models.CharField(max_length=255, default='Last')
    client_email = models.EmailField()
    client_password = models.CharField(
        max_length=16, 
        validators=[MinLengthValidator(limit_value=8)],
        help_text="Enter a password between 8 and 16 characters."
    )
    client_confirmPassword = models.CharField(
        max_length=16, 
        validators=[MinLengthValidator(limit_value=8)],
        help_text="Enter the same password as above."
    )
    client_dob = models.DateField(
        validators=[
            MaxValueValidator(date.today(), message="Date cannot be in the future."),
            validate_age                # Reference utility function for dob (18 years)
        ]
    )
    CLIENT_GENDER_CHOICES = [('male', 'Male'), ('female', 'Female')]
    client_gender = models.CharField(max_length=10, choices=CLIENT_GENDER_CHOICES)
    CLIENT_MARITAL_STATUS_CHOICES = [('single', 'Single'), ('married', 'Married')]
    client_maritalStatus = models.CharField(max_length=10, choices=CLIENT_MARITAL_STATUS_CHOICES)
    CLIENT_NATIONALITY_CHOICES = [('kenyan', 'Kenyan'), ('foreigner', 'Foreigner')]
    client_nationality = models.CharField(max_length=10, choices=CLIENT_NATIONALITY_CHOICES)
    client_acceptTerms = models.BooleanField()


    def __str__(self):
        return f"{self.client_fname} {self.client_lname}"


# Worker registration form
# Same logic as the client form, except we will redirect to the worker dashboard now
class WorkerRegistration(models.Model):
    worker_fname = models.CharField(max_length=255, default='First')
    worker_lname = models.CharField(max_length=255, default='Last')
    worker_email = models.EmailField()
    worker_password = models.CharField(
        max_length=16, 
        validators=[MinLengthValidator(limit_value=8)],
        help_text="Enter a password between 8 and 16 characters."
    )
    worker_confirmPassword = models.CharField(
        max_length=16, 
        validators=[MinLengthValidator(limit_value=8)],
        help_text="Enter the same password as above."
    )
    worker_id = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(99999999),  # Max 8 digits (99999999)
        ]
    )
    worker_dob = models.DateField(
        validators=[
            MaxValueValidator(date.today(), message="Date cannot be in the future."),
            validate_age                # Reference utility function for dob (18 years)
        ]
    )
    WORKER_GENDER_CHOICES = [('male', 'Male'), ('female', 'Female')]
    worker_gender = models.CharField(max_length=10, choices=WORKER_GENDER_CHOICES)
    WORKER_MARITAL_STATUS_CHOICES = [('single', 'Single'), ('married', 'Married')]
    worker_maritalStatus = models.CharField(max_length=10, choices=WORKER_MARITAL_STATUS_CHOICES)
    WORKER_NATIONALITY_CHOICES = [('kenyan', 'Kenyan'), ('foreigner', 'Foreigner')]
    worker_nationality = models.CharField(max_length=10, choices=WORKER_NATIONALITY_CHOICES)
    WORKER_ROLE_CHOICES = [
        ('house help', 'House Help'),
        ('nanny', 'Nanny'),
        ('gardener', 'Gardener'),
        ('gatekeeper', 'Gatekeeper'), 
        ('chef', 'Chef'),
    ]
    worker_role = models.CharField(max_length=20, choices=WORKER_ROLE_CHOICES)
    WORKER_LOCATION_CHOICES = [
        ('nairobi', 'Nairobi'),
        ('mombasa', 'Mombasa'),
        ('kisumu', 'Kisumu'),
        ('nakuru', 'Nakuru'),
        ('eldoret', 'Eldoret'),
    ]
    worker_location = models.CharField(max_length=20, choices=WORKER_LOCATION_CHOICES)
    worker_acceptTerms = models.BooleanField()


    def __str__(self):
        return f"{self.worker_fname} {self.worker_lname}"

'''












'''
# Trial Code to automatically add groups to users based on the form they used to register
User = get_user_model()


# Code to ensure dob is at least 18 years ago
def validate_age(value):
    today = date.today()
    age_limit = today - timedelta(days=(18 * 365))  # Assuming an average year has 365 days

    if value > age_limit:
        raise ValidationError("Must be at least 18 years old.")


#Client registration form
# Basically the table where the client form field info will be going
class ClientRegistration(AbstractUser):
    client_fname = models.CharField(max_length=255)
    client_lname = models.CharField(max_length=255)
    client_email = models.EmailField()
    client_password = models.CharField(
        max_length=16, 
        validators=[MinLengthValidator(limit_value=8)],
        help_text="Enter a password between 8 and 16 characters."
    )
    client_confirmPassword = models.CharField(
        max_length=16, 
        validators=[MinLengthValidator(limit_value=8)],
        help_text="Enter the same password as above."
    )
    client_dob = models.DateField(
        validators=[
            MaxValueValidator(date.today(), message="Date cannot be in the future."),
            validate_age                # Reference utility function for dob (18 years)
        ]
    )
    CLIENT_GENDER_CHOICES = [('male', 'Male'), ('female', 'Female')]
    client_gender = models.CharField(max_length=10, choices=CLIENT_GENDER_CHOICES)
    CLIENT_MARITAL_STATUS_CHOICES = [('single', 'Single'), ('married', 'Married')]
    client_maritalStatus = models.CharField(max_length=10, choices=CLIENT_MARITAL_STATUS_CHOICES)
    CLIENT_NATIONALITY_CHOICES = [('kenyan', 'Kenyan'), ('foreigner', 'Foreigner')]
    client_nationality = models.CharField(max_length=10, choices=CLIENT_NATIONALITY_CHOICES)
    client_acceptTerms = models.BooleanField()

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Check if the user exists, if not, create one<-----Goated Code------->
        if not self.user:
            user = User.objects.create_user(username=self.client_lname, email=self.client_email)
            self.user = user

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.client_fname} {self.client_lname}"


# Worker registration form
# Same logic as the client form, except we will redirect to the worker dashboard now
class WorkerRegistration(AbstractUser):
    worker_fname = models.CharField(max_length=255)
    worker_lname = models.CharField(max_length=255)
    worker_email = models.EmailField()
    worker_password = models.CharField(
        max_length=16, 
        validators=[MinLengthValidator(limit_value=8)],
        help_text="Enter a password between 8 and 16 characters."
    )
    worker_confirmPassword = models.CharField(
        max_length=16, 
        validators=[MinLengthValidator(limit_value=8)],
        help_text="Enter the same password as above."
    )
    worker_id = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(99999999),  # Max 8 digits (99999999)
        ]
    )
    worker_dob = models.DateField(
        validators=[
            MaxValueValidator(date.today(), message="Date cannot be in the future."),
            validate_age                # Reference utility function for dob (18 years)
        ]
    )
    WORKER_GENDER_CHOICES = [('male', 'Male'), ('female', 'Female')]
    worker_gender = models.CharField(max_length=10, choices=WORKER_GENDER_CHOICES)
    WORKER_MARITAL_STATUS_CHOICES = [('single', 'Single'), ('married', 'Married')]
    worker_maritalStatus = models.CharField(max_length=10, choices=WORKER_MARITAL_STATUS_CHOICES)
    WORKER_NATIONALITY_CHOICES = [('kenyan', 'Kenyan'), ('foreigner', 'Foreigner')]
    worker_nationality = models.CharField(max_length=10, choices=WORKER_NATIONALITY_CHOICES)
    WORKER_ROLE_CHOICES = [
        ('house help', 'House Help'),
        ('nanny', 'Nanny'),
        ('gardener', 'Gardener'),
        ('gatekeeper', 'Gatekeeper'), 
        ('chef', 'Chef'),
    ]
    worker_role = models.CharField(max_length=20, choices=WORKER_ROLE_CHOICES)
    WORKER_LOCATION_CHOICES = [
        ('nairobi', 'Nairobi'),
        ('mombasa', 'Mombasa'),
        ('kisumu', 'Kisumu'),
        ('nakuru', 'Nakuru'),
        ('eldoret', 'Eldoret'),
    ]
    worker_location = models.CharField(max_length=20, choices=WORKER_LOCATION_CHOICES)
    worker_acceptTerms = models.BooleanField()

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Check if the user exists, if not, create one<-----Goated Code------->
        if not self.user:
            user = User.objects.create_user(username=self.worker_lname, email=self.worker_email)
            self.user = user

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.worker_fname} {self.worker_lname}"



@receiver(post_save, sender=ClientRegistration)
def assign_to_client_group(sender, instance, created, **kwargs):
    if created:
        client_group = Group.objects.get(name='client')
        instance.user.groups.add(client_group)


@receiver(post_save, sender=WorkerRegistration)
def assign_to_worker_group(sender, instance, created, **kwargs):
    if created:
        worker_group = Group.objects.get(name='worker')
        instance.user.groups.add(worker_group)

'''






















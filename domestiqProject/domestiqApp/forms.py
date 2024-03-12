from django import forms
from .models import CustomUser

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'username', 'first_name', 'last_name', 'email',
            'password', 'client_dob', 'client_gender',
            'client_maritalStatus', 'client_nationality',
            'client_acceptTerms'
        ]
        widgets = {
            'password': forms.PasswordInput(),  # Use a password input widget for the password field
        }

    # If you need additional validation or customization, you can add it here
















'''
# Create a Django form that corresponds to your model. 
# This will help in rendering the form in your templates.
# Renders my custom styled form without the duplicate: {{% form as .p %}}
class ClientRegistrationForm(forms.ModelForm):
    class Meta:
        model = ClientRegistration
        fields = '__all__'

# You can add custom validation methods if needed
# Example: Validate that password and confirm_password match
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('client_password')
        confirm_password = cleaned_data.get('client_confirmPassword')

        if password != confirm_password:
            raise forms.ValidationError("Password and confirm password do not match.")



# Call in worker registration form
class WorkerRegistrationForm(forms.ModelForm):
    class Meta:
        model = WorkerRegistration
        fields = '__all__'

# You can add custom validation methods if needed
# Example: Validate that password and confirm_password match
    def clean(self):
        cleaned_data = super().clean()
        # Convert integer fields to strings
        # cleaned_data['worker_id'] = str(cleaned_data['worker_id'])
        # Password validation
        password = cleaned_data.get('worker_password')
        confirm_password = cleaned_data.get('worker_confirmPassword')

        if password != confirm_password:
            raise forms.ValidationError("Password and confirm password do not match.")

'''
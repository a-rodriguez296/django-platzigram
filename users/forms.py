from django import forms
from django.contrib.auth.models import User
from users.models import Profile


class SignupForm(forms.Form):

    username = forms.CharField(max_length=50, min_length=4)
    password = forms.CharField(max_length=70, widget=forms.PasswordInput())
    password_confirmation = forms.CharField(max_length=70, widget=forms.PasswordInput())

    first_name = forms.CharField(max_length=50, min_length=2)
    last_name = forms.CharField(max_length=50, min_length=2)

    email = forms.CharField(max_length=50, min_length=8, widget=forms.EmailInput())


    #How to validate forms
    
    #with this method we can validate a field. The name of the method must be clean_<field's name>
    def clean_username(self):

        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('Username is already in use')
        #siempre hay q regresar el campo
        return username

    
    #With this method we can validate fields that depend on each other. In this case password and password confirmation
    def clean(self):

        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match')
        
        return data

    def save(self):

        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()




class ProfileForm(forms.Form):

    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField()
from django import forms
from django.contrib.auth import (
authenticate,
get_user_model
)

User=get_user_model()

class UserRegistrationForm(forms.ModelForm):
    email=forms.EmailField(label="Email")
    password=forms.CharField(label="Password")
    class Meta:
        model=User
        fields=[
            'username',
            'email',
            'password'
        ]
    def clean(self,*args,**kwargs):
        email=self.cleaned_data.get('email')
        email_val=User.objects.filter(email=email)
        if email_val.exists():
            raise forms.ValidationError(
                "Email already exist"
            )
        return super(UserRegistrationForm,self).clean(*args,**kwargs)

class UserLoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

    def clean(self,*args,**kwargs):
        username=self.cleaned_data.get('username')
        password=self.cleaned_data.get('password')

        if username and password:
            user=authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
        return super(UserLoginForm,self).clean(*args,**kwargs)
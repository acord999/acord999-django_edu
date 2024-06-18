from re import I
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.forms import CharField, ImageField

from users.models import User

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        
    username = CharField()
    password = CharField()
    
    
    
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2"
        ]
        
        
    first_name = CharField()
    last_name = CharField()    
    username = CharField()
    email = CharField()
    password1 = CharField()
    password2 = CharField()
    
    
    
class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = [
            "image",
            "first_name",
            "last_name",
            "username",
            "email",
        ]
        
    image = ImageField(required=False)    
    first_name = CharField()
    last_name = CharField()    
    username = CharField()
    email = CharField()

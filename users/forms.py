from django.contrib.auth.forms import AuthenticationForm
from django.forms import CharField

from users.models import User

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        
    username = CharField()
    password = CharField()
from django.forms import ModelForm
from .models import Room, User
from django.contrib.auth.forms import UserCreationForm


class myUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  #fields to be used in the form for user creation
        help_texts = {k: "" for k in fields}  #to remove help texts from the form

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host' , 'participants']  #create the RoomForm using Room class using all the attributes

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'username'  , 'email', 'bio']  #create the UserForm using User class using all the attributes
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile, Sports, Levels, Comment, EventAttendance, Message, Event
from flatpickr import DatePickerInput, TimePickerInput, DateTimePickerInput
from django.forms import ModelForm
import time


class CreateUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = "__all__"


class CreatePost(forms.Form):
    title = forms.CharField(label='Tytul')
    sport = forms.MultipleChoiceField(
        choices=[(sports.id, sports.sport_name) for sports in Sports.objects.all()],
        widget=forms.CheckboxSelectMultiple())
    accepted_levels = forms.MultipleChoiceField(
        choices=[(levels.id, levels.level) for levels in Levels.objects.all()],
        # related_name='levels',
        widget=forms.CheckboxSelectMultiple()
    )
    content = forms.CharField(widget=forms.Textarea)

class DateInput(forms.DateTimeInput):
    input_type = 'datetime'


class CreateEvent(ModelForm):

    class Meta:
        model = Event
        fields = ['title', 'number_of_players', 'location', 'start', 'end', 'price', 'content', 'sport']
        widgets = {
            'start' : DateTimePickerInput(),
            'end' : DateTimePickerInput(),

        }






class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content': forms.Textarea()
        }


class EventAttendanceForm(forms.ModelForm):
    attended = forms.BooleanField()

    class Meta:
        model = EventAttendance
        fields = ('attended',)


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('subject', 'content')

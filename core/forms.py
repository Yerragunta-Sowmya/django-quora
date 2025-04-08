from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Question, Answer

class RegisterForm(UserCreationForm):
    mobile_number = forms.CharField(max_length=10, required=False)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2', 'mobile_number']
        help_texts = {
            'username': None,
            'password1': None,
            'password2': None,
        }

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password1')

        if not username or not password:
            raise forms.ValidationError("Invalid credentials")
        
        return cleaned_data    

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'body']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['body']

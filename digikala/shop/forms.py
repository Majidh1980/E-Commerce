from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms


class UpdateUserForm(UserChangeForm):
    password = None
    first_name = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                       'placeholder':'نام خود را وارد کنید'}))
    last_name = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                      'placeholder': 'نام خانوادگی خود را وارد کنید'}))
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل خود را وارد کنید'}))
    username = forms.CharField(label="", max_length=20, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                      'placeholder': 'نام کاربری خود را وارد کنید'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')

class SignUpForm(UserCreationForm):
    phone_number = forms.CharField(label="", max_length=15, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'شماره تلفن خود را وارد کنید'}))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'اسم رمز بالای 8 کارکتری را وارد کنید'}), help_text="")
    password2 = forms.CharField(label="", widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'تکرار اسم رمز'}), help_text="")

    class Meta:
        model = User
        fields = ('phone_number', 'password1', 'password2')

class AdditionalInfoForm(forms.ModelForm):
    first_name = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خود را وارد کنید'}))
    last_name = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خانوادگی خود را وارد کنید'}))
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل خود را وارد کنید'}))
    username = forms.CharField(label="", max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کاربری خود را وارد کنید'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')





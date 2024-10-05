#own

# forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, UserChangeForm
from myEduu.models import Profile

class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_pic', 'website_url', 'youtube_url', 'github_url', 'instagram_url', 'linkedin_url']
        widgets = {
        'bio' : forms.Textarea(attrs={'class': 'form-control'}),
        #'profile_pic' : forms.TextInput(attrs={'class': 'form-control-file'}, null=True, blank=True, upload_to="images/profile/"),
        'website_url' : forms.TextInput(attrs={'class': 'form-control-file'}),
        'youtube_url' : forms.TextInput(attrs={'class': 'form-control-file'}),
        'instagram_url' : forms.TextInput(attrs={'class': 'form-control-file'}),
        'github_url' : forms.TextInput(attrs={'class': 'form-control-file'}),
        'linkedin_url' : forms.TextInput(attrs={'class': 'form-control-file'}),
        }

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Add email field
    first_name = forms.CharField(max_length=30, required=True)  # Add first name field
    last_name = forms.CharField(max_length=30, required=True)  # Add last name field

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']  # Specify field order

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(max_length=100, label='New password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(max_length=100, label='Confirm new password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
        
class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    #last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    #is_superuser = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    #is_staff = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    #is_active = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    #date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        
    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
     
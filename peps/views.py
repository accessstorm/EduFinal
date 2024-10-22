from django.shortcuts import render, get_object_or_404
from django.views import generic
#from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, PasswordChangingForm, EditProfileForm, ProfilePageForm  # Import the custom form
from django.contrib.auth.views import PasswordChangeView
from . import views
from django.views.generic import DetailView, CreateView
from myEduu.models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

class EditProfilePageView(LoginRequiredMixin, generic.UpdateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/edit_profile_page.html'
    #fields = ['bio', 'profile_pic', 'website_url', 'youtube_url', 'instagram_url', 'github_url', 'linkedin_url']
    success_url = reverse_lazy('view1')

    def get_object(self):
        # Ensure that the user is authenticated before accessing their profile
        user = self.request.user
        if user.is_authenticated:
            return get_object_or_404(Profile, user=user)

    def handle_no_permission(self):
        # You can customize what happens when an anonymous user tries to access this view
        return render(self.request, 'error.html', {})

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'
    
    def get_context_data(self, *args, **kwargs):
        #users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        
        context["page_user"] = page_user
        return context
    

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('password_success')
    
def password_success(request):
    return render(request, 'registration/password_success.html', {}) 


class UserRegistrationView(generic.CreateView):
    form_class = CustomUserCreationForm  # Use the custom form
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):  # Change CreateView to UpdateView
    model = Profile
    form_class = EditProfileForm  # Use the form for editing
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('view1')

    def get_object(self):
        return self.request.user


class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_user_profile_page.html'
    #fields = ['bio', 'profile_pic', 'website_url', 'youtube_url', 'instagram_url', 'github_url', 'linkedin_url']
    success_url = reverse_lazy('view1')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
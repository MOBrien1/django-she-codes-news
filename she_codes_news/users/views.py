from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model

# Create your views here.
class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class UserProfileView(generic.DetailView):
    model = CustomUser
    template_name = 'users/user_profile.html'
    context_object_name = 'profile_user'

class LoggedInUserView(generic.TemplateView):
    template_name = 'users/user_profile.html'
    
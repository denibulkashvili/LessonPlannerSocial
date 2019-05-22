"""Account app views"""
from django.urls import reverse_lazy
from django.views.generic import CreateView

from . import forms

# Create your views here.
# pylint:disable=too-many-ancestors
class SignUp(CreateView):
    """User sign up view"""
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"

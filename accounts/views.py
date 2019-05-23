"""Account app views"""
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.shortcuts import redirect, render

from . import forms

# Create your views here.
# pylint:disable=too-many-ancestors
class SignUp(CreateView):
    """User sign up view"""
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"


def change_password(request):
    """Change the password view"""
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Password has been changed successfully.")
            return redirect(reverse("accounts:change_password"))
        # else
        messages.error(request, "There's been an error.")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "accounts/change_password.html", {
        "form": form
    })           

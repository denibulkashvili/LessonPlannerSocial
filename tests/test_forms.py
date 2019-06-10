"""Module for testing forms"""
from django.test import TestCase

# from django.test import Client
from accounts.forms import UserCreateForm
from accounts.models import User


class UserFormTest(TestCase):
    """Tests User create form"""

    def test_user_form_valid_data(self):
        """Test user form with valid data"""
        # form = UserCreateForm(data={
        #     'username': "test_user",
        #     'email':"test_user@email.com",
        #     'password1':"pass123",
        #     'password2':"pass123"
        # })
        # self.assertTrue(form.is_valid())
        pass

    def test_user_form_invalid_data(self):
        """Test user form with invalid data"""
        pass

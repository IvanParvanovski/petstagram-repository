from django.contrib.auth.forms import UserCreationForm

from core.BootstrapFormMixin import BootstrapFormMixin


class SignUpForm(UserCreationForm,
                 BootstrapFormMixin):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_form()

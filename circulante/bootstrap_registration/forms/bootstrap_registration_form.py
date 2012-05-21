from bootstrap.forms import BootstrapForm, Fieldset
from registration.forms import RegistrationForm


class BootstrapRegistrationForm(BootstrapForm, RegistrationForm):
    """
    Thin wrapper over the django-registration RegistrationForm appending the
    bootstrap benefits to it.
    """
    class Meta:
        layout = (
            Fieldset('BootstrapRegistrationForm', 'username', 'email', 'password1', 'password2', ),
            )

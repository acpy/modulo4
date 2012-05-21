from bootstrap.forms import BootstrapForm, Fieldset
from django.contrib.auth.forms import AuthenticationForm


class BootstrapAuthenticationForm(BootstrapForm, AuthenticationForm):
    """
    Thin wrapper over the usual AuthenticationForm appending the bootstrap
    benefits to it.
    """
    class Meta:
        layout = (
            Fieldset('BootstrapAuthenticationForm', 'username', 'password', ),
            )

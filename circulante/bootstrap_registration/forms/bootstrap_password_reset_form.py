from bootstrap.forms import BootstrapForm, Fieldset
from django.contrib.auth.forms import PasswordResetForm


class BootstrapPasswordResetForm(BootstrapForm, PasswordResetForm):
    """
    Thin wrapper over the usual PasswordChangeForm appending the bootstrap
    benefits to it.
    """

    class Meta:
        layout = (
            Fieldset('BootstrapPasswordResetForm', 'email', ),
            )

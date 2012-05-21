from registration.backends.default import DefaultBackend
from bootstrap_registration.forms.bootstrap_registration_form import \
    BootstrapRegistrationForm


class RegistrationBackend(DefaultBackend):
    """
    Backend used by django-registration on the register view and supplied by us

    The only difference with the default one is that we want to use our own
    registration form that is integrated with the Bootstrap framework.
    """
    def get_form_class(self, request):
        return BootstrapRegistrationForm

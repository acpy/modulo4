from django.conf.urls import patterns, url, include
from bootstrap_registration.forms import BootstrapAuthenticationForm
from bootstrap_registration.forms import BootstrapPasswordResetForm
from bootstrap_registration.forms import BootstrapPasswordChangeForm
from bootstrap_registration.forms import BootstrapSetPasswordForm

urlpatterns = patterns('django.contrib.auth.views',
    url(r'^login/$', 'login', {
            'authentication_form': BootstrapAuthenticationForm,
        }, name='login'),
    url(r'^logout/$', 'logout', {
        'next_page': '/accounts/login/'
    }, name='logout'),
    url(r'^password/change/$', 'password_change', {
        'password_change_form': BootstrapPasswordChangeForm,
        }, name='auth_password_change'),
    url(r'^password/reset/$', 'password_reset', {
        'password_reset_form': BootstrapPasswordResetForm,
    }, name='auth_password_reset'),
    url(r'^password/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
        'password_reset_confirm', {
            'set_password_form': BootstrapSetPasswordForm
        }, name='auth_password_reset_confirm'),
)

urlpatterns += patterns('registration.views',
    url(r'^register/$',
        'register', {
            'backend':
                'bootstrap_registration.backends.RegistrationBackend',
        },
        name='registration_register'),
)

urlpatterns += patterns('',
    url(r'', include('registration.backends.default.urls')),
    )

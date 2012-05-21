from django.conf.urls import patterns, url

urlpatterns = patterns('test_client.views',
    url(r'accounts/profile/$', 'account_profile'),
    )

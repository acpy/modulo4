from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response


@login_required
def account_profile(request):
    return render_to_response('accounts/profile.html', {
        'user': request.user
    })

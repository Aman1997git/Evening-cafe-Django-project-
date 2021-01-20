from django.contrib import messages
from django.shortcuts import redirect


def check_login_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):

        if request.session.get('customer') is None:

            return_link = request.META['PATH_INFO']
            messages.info(request, "please login first")
            return redirect(f'/accounts/login?return_link={return_link}')

        response = get_response(request)
        return response

    return middleware

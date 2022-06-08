from django.shortcuts import redirect

# While the application has only RESTful API UI-functional that starts from "rest-api/v1/" url,
# server must redirect users from this application main page
# to login page, if user is not auth-ed, otherwise to documentation page.


def redirection(request):
    if request.user.is_authenticated:
        return redirect('home-docs')
    return redirect('user_auth')

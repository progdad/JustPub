from django.urls import path, include
from django.shortcuts import redirect

import Pub.redirect_request_from_root_app_and_api_pages

urlpatterns = [
    path('rest-api/v1/', include('Pub.rest_api.urls')),

    # This url view name speaks for itself meaning.
    # See the explanation inside ./redirect_request_from_root_app_and_api_pages.py file
    path('', Pub.redirect_request_from_root_app_and_api_pages.redirection)
]


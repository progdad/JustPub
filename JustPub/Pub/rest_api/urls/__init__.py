from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

import Pub.redirect_request_from_root_app_and_api_pages

from Pub.rest_api.views import LoginView, LogoutView, documentation_view

from .pub_rest_endpoints import rest_endpoints


urlpatterns = [
    path('authentication/', LoginView.as_view(), name="user_auth"),
    path('logout/', LogoutView.as_view(), name="user_logout"),

    path('documentation/', documentation_view.with_ui('swagger', cache_timeout=0), name='home-docs'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    *rest_endpoints,
    
    # See the explanation inside ../../redirect_request_from_main_page.py file
    path('', Pub.redirect_request_from_root_app_and_api_pages.redirection)
]

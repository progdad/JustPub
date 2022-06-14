from django.urls import path, include


urlpatterns = [
    path('rest-api/v1/', include('Pub.rest_api.urls')),
]

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework.authentication import SessionAuthentication


documentation_view = get_schema_view(
    openapi.Info(
        title="Pub API",
        default_version='v1',
        description="""
        ```SHORT DESCRIPTION```
        
        To be able to make requests to the endpoints documented below 
        you have to get your JSON Web Token. *You can get it right on this documentation page.*
        
        Scroll down this page till you see **"token"** documentation chapter 
        and there just put your credentials to get your JWT.
        """,
    ),
    authentication_classes=(SessionAuthentication,)
)

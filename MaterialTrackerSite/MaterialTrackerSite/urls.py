from django.contrib import admin
from django.urls import path
from MaterialTrackerApp import views
from MaterialTrackerApp.models import *
from django.urls.conf import include
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import PasswordChangeDoneView
from MaterialTrackerSite.views import *
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetCompleteView
from rest_framework import routers
from rest_framework import permissions
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from drf_yasg.views import get_schema_view as yasg_schema_view
from drf_yasg import openapi

schema_view = yasg_schema_view(
    openapi.Info(
        title="API MaterialTracker",
        default_version='v1',
        description="API for materials",
        contact=openapi.Contact(email="lucastoscanop@gmail.com"),
        license=openapi.License(name='GNU GPLv3'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include('django.contrib.auth.urls')),
    
    # Access control -------------------------------------------------------------
    # path('accounts/', include('accounts.urls')),
    path('docs/', include_docs_urls(title='Documentação da API')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/v1/', include(routers.DefaultRouter().urls)),
    path('openapi', get_schema_view(
        title="API material", 
        description="API to fetch material data",), 
        name='openapi-schema'
    ),
    #-----------------------------------------------------------------------------

    
    path('', include('MaterialTrackerApp.urls')),
    path('accounts/', include('accounts.urls')),
]

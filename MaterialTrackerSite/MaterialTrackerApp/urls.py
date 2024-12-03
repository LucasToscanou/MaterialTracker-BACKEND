from django.contrib import admin
from django.urls import path
from MaterialTrackerApp import views
from django.conf.urls.static import static
from django.conf import settings
app_name = 'MaterialTrackerApp'


urlpatterns = [
    path("material/list/", views.MaterialView.as_view(), name='material-list'),
    path("material/create/", views.MaterialCreateView.as_view(), name='material-create'),
    path('projects/', views.ProjectView.as_view(), name='project-list'),
    path('userprofiles/', views.UserProfileView.as_view(), name='userprofile-list'),
    path('locations/', views.LocationView.as_view(), name='location-list'),
    path('materialimgs/', views.MaterialImgView.as_view(), name='materialimg-list'),
    path('currencies/', views.CurrencyView.as_view(), name='currency-list'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

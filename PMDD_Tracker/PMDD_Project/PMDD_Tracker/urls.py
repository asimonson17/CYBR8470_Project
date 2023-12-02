from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
from Tracker import views
from rest_framework import routers
from django.urls import include, re_path
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


router = routers.SimpleRouter()


router.register(r'Tracker', views.TrackerViewSet, basename='tracker')
#router.register(r'User', views.UserViewSet, basename='user')

urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path("addentry", views.addentry, name="addentry"),
    path("calendar", views.calendar, name="calendar"),
    path("accounts/", include("django.contrib.auth.urls")), 
    path("registeruser", views.registeruser, name="registeruser"),
    path('login', views.custom_login, name='login'),
    path('logout', views.custom_logout, name='logout'),
    re_path(r"^$", views.index, name="index"),
]

urlpatterns = format_suffix_patterns(urlpatterns)


 
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
from Tracker import views
from rest_framework import routers
from django.urls import include, re_path


router = routers.SimpleRouter()

#router.register(r'pmdd', views.PMDDViewSet, basename='PMDD')
#router.register(r'user', views.UserViewSet, basename='User')


urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    re_path(r"^$", views.index, name="index"),
]

urlpatterns = format_suffix_patterns(urlpatterns)

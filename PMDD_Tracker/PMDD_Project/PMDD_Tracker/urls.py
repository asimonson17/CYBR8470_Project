from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
from Tracker import views
from rest_framework import routers
from django.urls import include, re_path


router = routers.SimpleRouter()

#router.register(r'pmdd', views.PMDDViewSet, basename='PMDD')
#router.register(r'user', views.UserViewSet, basename='User')


router.register(r'Tracker', views.TrackerViewSet, basename='tracker')

urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path("addentry", views.addentry, name="addentry"),
    re_path(r"^$", views.index, name="index"),
]

urlpatterns = format_suffix_patterns(urlpatterns)


#django forms or javascript to call api like we did with postman - jquery - to call data. django templating syntax 
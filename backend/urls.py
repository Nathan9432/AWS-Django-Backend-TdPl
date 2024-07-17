from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from TdPl import views

router = routers.DefaultRouter()
router.register(r'person', views.PersonView)
router.register(r'task', views.TaskView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]

from django.contrib import admin
from django.urls import path
from assignments.api import assignments_urlpatterns
from rest_framework_swagger.views import get_swagger_view

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += assignments_urlpatterns

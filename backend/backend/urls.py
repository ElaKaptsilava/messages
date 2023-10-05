from django.contrib import admin
from django.urls import path

from assignments.urls import assignments_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += assignments_urlpatterns

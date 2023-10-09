from django.contrib import admin
from django.urls import path
from assignments.api import assignments_urlpatterns
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema', SpectacularAPIView.as_view(), name="schema"),
    path('api/schema/docs/', SpectacularSwaggerView.as_view(url_name='schema'))
]

urlpatterns += assignments_urlpatterns

from django.urls import re_path
from rest_framework.routers import DefaultRouter

from .views import AssignmentViewSet

router = DefaultRouter()
router.register(r"assignments", AssignmentViewSet, basename="assignments")
assignments_urlpatterns = router.urls
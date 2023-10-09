from rest_framework.routers import DefaultRouter
from .views import EmailViewSet, MailBoxViewSet, TemplateViewSet

router = DefaultRouter()
router.register(r"email", EmailViewSet, basename="email")
router.register(r"mailbox", MailBoxViewSet, basename="mailbox")
router.register(r"template", TemplateViewSet, basename="template")
assignments_urlpatterns = router.urls
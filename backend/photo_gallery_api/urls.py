from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from .views import TodoView, UserView, check_credentials, PhotoView


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'todos', TodoView)
router.register(r'users', UserView)
router.register(r'photos', PhotoView)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('login/', check_credentials, name='post_val'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
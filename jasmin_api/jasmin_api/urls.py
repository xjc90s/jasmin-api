from django.conf.urls import include, url
from django.conf import settings

from rest_framework.routers import DefaultRouter

from rest_api.views import GroupViewSet, UserViewSet, MORouterViewSet

router = DefaultRouter()
router.register(r'groups', GroupViewSet, base_name='groups')
router.register(r'users', UserViewSet, base_name='users')
router.register(r'morouters', MORouterViewSet, base_name='morouters')

urlpatterns = [
    url(r'^api/', include(router.urls)),
]


if settings.SHOW_SWAGGER:
    urlpatterns += [url(r'^docs/', include('rest_framework_swagger.urls'))]



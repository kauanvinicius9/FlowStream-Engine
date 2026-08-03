from django.urls import path, include
from manuals.views import ProcessDefinitionViewSet, ProcessExecutionViewSet
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'definitions', ProcessDefinitionViewSet,basename='definition')
router.register(r'executions',ProcessExecutionViewSet,basename='execution')

urlpatterns = [
    path('api/', include(router.urls)),
]

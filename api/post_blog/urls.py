from django.urls import path,include
from rest_framework import routers
from post_blog import views

router=routers.DefaultRouter()
router.register(r'login', views.loginViewSet)
router.register(r'personal_data_user',views.personaldatauserViewSet)
router.register(r'publications',views.publicationsViewSet)

urlpatterns = [
    path('',include(router.urls))
]

from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('posts', views.PostView, 'posts')

urlpatterns = router.urls

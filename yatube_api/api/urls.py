from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet


router = DefaultRouter()

router.register('posts', PostViewSet)
router.register('posts/(?P<post_id>\\d+)/comments', CommentViewSet,
                basename='comment')
router.register('groups', GroupViewSet)
router.register('follow', FollowViewSet, basename='follow')


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]

from rest_framework.routers import DefaultRouter
from django.urls import include, path
from .views import (
    PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet
)


routers = DefaultRouter()
routers.register(
    'posts', PostViewSet
)
routers.register(
    'posts/(?P<post_id>\\d+)/comments', CommentViewSet
)
routers.register(
    'groups', GroupViewSet
)
routers.register(
    'follow', FollowViewSet
)

urlpatterns = [
    path('', include(routers.urls)),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
]

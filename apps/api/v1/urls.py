from django.conf.urls import url, include
from rest_framework import routers

from .accounts.views import UserViewSet, GroupViewSet, UserCreate
from .posts.views import PostList, PostDetail, CommentList, CommentDetail


# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = [
    url(r'^', include(router.urls)),

    # url(r'^users/list/$', UserList.as_view()),
    url(r'^users/create/$', UserCreate.as_view()),
    # url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view())

    url(r'^posts/$', PostList.as_view()),
    url(r'^posts/(?P<pk>[0-9]+)/$', PostDetail.as_view()),

    url(r'^comments/$', CommentList.as_view()),
    url(r'^comments/(?P<pk>[0-9]+)/$', CommentDetail.as_view())
]
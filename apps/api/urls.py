from django.conf.urls import url, include
from .views import UserList, UserCreate, UserDetail,\
                   PostList, PostDetail, CommentList, CommentDetail


urlpatterns = [
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^users/$', UserList.as_view()),
    url(r'^users/create/$', UserCreate.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view()),
    url(r'^posts/$', PostList.as_view()),
    url(r'^posts/(?P<pk>[0-9]+)/$', PostDetail.as_view()),
    url(r'^comments/$', CommentList.as_view()),
    url(r'^comments/(?P<pk>[0-9]+)/$', CommentDetail.as_view())
]

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (CreateBucketView,
                    DetailsBucketView, CreateItemView, DetailsItemView)

urlpatterns = {
    url(r'^bucketlists/$', CreateBucketView.as_view(),
        name="create bucketlist"),
    url(r'^bucketlists/(?P<pk>[0-9]+)/$',
        DetailsBucketView.as_view(), name="bucketlist details"),
    url(r'^bucketlists/(?P<pk>[0-9]+)/items/$',
        CreateItemView.as_view(), name="create item"),
    url(r'^bucketlists/(?P<pk>[0-9]+)/Items/(?P<it>[0-9]+)/$',
        DetailsItemView.as_view(), name="item details"),
}

urlpatterns = format_suffix_patterns(urlpatterns)

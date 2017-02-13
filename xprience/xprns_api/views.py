from django.shortcuts import get_object_or_404
from rest_framework import generics
from .serializers import BucketlistSerializer, BucketlistItemSerializer
from .models import Bucketlist, BucketlistItem

# Create your views here.


class CreateBucketView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()


class DetailsBucketView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer


class CreateItemView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = BucketlistItem.objects.all()
    serializer_class = BucketlistItemSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()
        pk = self.kwargs.get('pk')
        bucketlist = get_object_or_404(
            Bucketlist,
            pk=pk,
            created_by=self.request.user)


class DetailsItemView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = BucketlistItem.objects.all()
    serializer_class = BucketlistItemSerializer

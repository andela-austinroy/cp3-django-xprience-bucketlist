from django.db import models

# Create your models here.


class Bucketlist(models.Model):
    """This class represents the bucketlist model."""
    name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Return a human readable representation of the model instance name.
        """
        return "{}".format(self.name)


class BucketlistItem(models.Model):
    """This class represents the bucketlist model."""
    name = models.CharField(max_length=255, blank=False, unique=True)
    done = models.CharField(max_length=5, blank=False)
    bucketlist = models.ForeignKey(Bucketlist, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Return a human readable representation of the model instance name.
        """
        return "{}".format(self.name)

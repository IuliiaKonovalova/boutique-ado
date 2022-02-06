from django.db import models


class Category(models.Model):
    """ Category model """
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        """ Return string representation """
        return self.name

    def get_friendly_name(self):
        """ Return friendly name """
        return self.friendly_name

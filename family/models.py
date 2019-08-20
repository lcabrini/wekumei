from django.db import models

class Person(models.Model):
    family_name = models.CharField(max_length=100)
    maiden_name = models.CharField(max_length=100)
    given_name = models.CharField(max_length=100)
    other_names = models.CharField(max_length=255)

    def __str__(self):
        return "{}, {}".format(self.family_name, self.first_name)


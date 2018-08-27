from django.db import models

# Create your models here.

#TODO: make a birthday model

#

class Birthday (models.Model):

    date = models.DateField( auto_now=False, auto_now_add=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)



    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("birthdays", kwargs={"pk": self.pk})

from django.db import models

# Create your models here.
class Contact(models.Model):
    Sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=14)
    content = models.TextField()
    email = models.CharField(max_length=150)

    def __str__(self):
        return "This is from " + self.name + ' - ' + self.email


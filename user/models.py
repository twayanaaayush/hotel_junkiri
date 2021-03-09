from django.db import models

class User(models.Model):
    u_name = models.CharField(max_length=50, verbose_name="Name")
    u_email = models.EmailField(verbose_name="Email")
    u_contact = models.IntegerField(verbose_name="Contact")
    u_address = models.CharField(max_length=50, verbose_name="Address")

    def __str__(self):
        return self.u_name
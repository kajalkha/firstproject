from django.db import models

# Create your models here.
class Form(models.Model):
    name = models.CharField(max_length = 20)
    address = models.CharField(max_length = 20)
    contact = models.CharField(max_length = 10)
    email = models.EmailField(max_length = 20, null = True)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = "Form"

    def __str__(self):    #helps to defined in the admin panel to search 
        return self.name

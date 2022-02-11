from django.db import models
import uuid

# Create your models here.
class customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length = 255,blank=False,null=False,unique =True)
    email = models.CharField(max_length = 255,blank=False,null=False,unique=True)
    balance = models.DecimalField(default=0,max_digits=12,decimal_places=2)
    def __str__(self):
            return self.name


class transactionsTable(models.Model):
    name_one= models.CharField(max_length = 255,blank=False,null=False,unique =False)
    name_two= models.CharField(max_length = 255,blank=False,null=False,unique =False)
    amount= models.DecimalField(default=0,max_digits=12,decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_one
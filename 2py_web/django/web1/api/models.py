from django.db import models

    
class Item(models.Model):
    objects = models.Manager() # vs code 오류제거용

    no      = models.AutoField(primary_key=True) 
    name    = models.CharField(max_length=30)
    price   = models.IntegerField() # inteRger 오타 주의
    regdate = models.DateTimeField(auto_now_add=True) 
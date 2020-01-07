# python manage.py check
# python manage.py makemigrations member
# python manage.py migrate member

# 1. 회원20명을 한번에 추가하시오
# ex) 101 103   506 409

# urls.py
# exam_insert
# exam_update
# exam_delete
# exam_select
from django.db import models

class Table2(models.Model):
    objects = models.Manager() # vs code 오류제거용

    no      = models.AutoField(primary_key=True) 
    name    = models.CharField(max_length=30)
    kor     = models.IntegerField() # inteRger 오타 주의
    eng     = models.IntegerField()
    math    = models.IntegerField()
    classroom=models.CharField(max_length=3)
    regdate = models.DateTimeField(auto_now_add=True) 
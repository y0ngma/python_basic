from django.db import models

class Table1(models.Model):
    object = models.Manager() # vs code 오류 제거용

    no      = models.AutoField(primary_key=True) # 자동 번호매기기
        # 자동의 이점 : 개발자가 번호 중복 매기지 않을 수 있음
# 사용자로부터 받을 내용-----------------------------
    title   = models.CharField(max_length=200) 
    content = models.TextField() 
    writer  = models.CharField(max_length=50)
# -------------------------------------------------
    hit     = models.IntegerField() # 조회수
    img     = models.BinaryField(null=True) # 바이너리 필수
    regdate = models.DateTimeField(auto_now_add=True) # 자동

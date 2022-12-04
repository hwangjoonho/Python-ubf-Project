from django.db import models

# Create your models here.



class Board(models.Model):
    boardno     = models.AutoField(primary_key=True)
    title       = models.CharField(max_length=100,default='')
    content     = models.CharField(max_length=100)
    name        = models.CharField(max_length=20)
    boardfile   = models.TextField(null=True, blank=True)
    created_at  = models.DateField(auto_now=True)

    # 이거 뭐더라
    # __str__ 메소드는 interface 역할수행위해 존재
    # 서로 다른 타입을 가진 데이터끼리 상호작용 할 때 문자열로 변환시킴으로서 상호간의 호환이 가능하도록 만들어줌. 사용자에 초점.
    def __str__(self):
        return self.msg

    class Meta:
        db_table ='board'








    #__repr__

    # __repr__ 메소드는 '객체를 문자열로 표현'하기 위해 존재. 개발자에 초점.

    # 객체를 문자열로 표현했다는 말 그대로 __repr__의 반환 값은 eval 함수에 사용 가능하며, 이를 활용하여 새로운 객체를 만들어 내는 것도 가능합니다.
    #  __str__ 메소드의 반환 값은 eval 함수에 사용할 수 없다

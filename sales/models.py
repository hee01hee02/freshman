from django.db import models
from django.contrib.auth.models import AbstractUser

class id(AbstractUser):
    pass 


class Sale(models.Model):
    choose_path = (
('nr', 'naver'),('shop2','shopworld'),('news','emailnews')

    )
    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    person = models.ForeignKey("Person", on_delete=models.CASCADE)

    def __str__(self) :
        return f"{self.first_name} {self.last_name}"

   # base_customer = models.BooleanField(default=False)
   # Inflow_path = models.CharField(choices=choose_path, max_length=200)
   # image_person = models.ImageField(blank=True, null=True)
   # image_file = models.FileField(blank=True, null=True)

class Person(models.Model):
    member = models.OneToOneField(id, on_delete=models.CASCADE)
   
    def __str__(self) :
        return self.member.username
   # 이미 만들어진 파일:class id(AbstractUser)을 가져다가 쓰기 때문에 
   # 따로 정의할 필요는 없음.  
   # first_name = models.CharField(max_length=30)
   # last_name = models.CharField(max_length=30)

   
    
    

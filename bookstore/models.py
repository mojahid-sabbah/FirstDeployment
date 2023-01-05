from django.db import models

# Create your models here.



class Tag (models.Model):
    name = models.CharField(max_length=100 , null=True)
    def __str__(self):
        return self.name   #هكذا نجعله يعرض الاسم في صفحة الادمين 

class Book (models.Model):
    CATEGORY=(
        ('Classic' , 'Classic'),
        ('Comic book' , 'Comic book'),
        ('Fantasy' , 'Fantasy'),
        ('Horror' , 'Horror'),
    )
    name = models.CharField(max_length=100 , null=False)
    auther = models.CharField(max_length=100 , null=False)
    price = models.FloatField( null=True)
    category = models.CharField(max_length=200 , null=True , choices=CATEGORY)
    description = models.CharField(max_length=200 , null=True)
    tags = models.ManyToManyField(Tag)#هنا نعرفها كعلاقة ماني تو ماني  M:M
    created_at = models.DateTimeField(auto_now_add=True , null=False)

    def __str__(self):
        return self.name  #هكذا نجعله يعرض الاسم في صفحة الادمين 

class Customer (models.Model):
    name = models.CharField(max_length=100 , null=True)
    email = models.CharField(max_length=100 , null=True)
    books = models.ManyToManyField(Book)#هنا نعرفها كعلاقة ماني تو ماني  M:M
    phone = models.CharField(max_length=100 , null=True)
    age = models.CharField( max_length=100 ,null=True)
    created_at = models.DateTimeField(auto_now_add=True , null=True)

    def __str__(self):
        return self.name 


    
class order (models.Model):
    STATUS=(
        ('Pending' , 'Pending'),
        ('Delivered' , 'Delivered'),
        ('in progress' , 'in progress'),
        ('out of order' , 'out of order'),

    )
    customer= models.ForeignKey(Customer, null=True ,on_delete=models.SET_NULL) # 1:M
    book= models.ForeignKey(Book, null=True ,on_delete=models.SET_NULL)# 1:M
    tags = models.ManyToManyField(Tag)#هنا نعرفها كعلاقة ماني تو ماني  M:M
    status = models.CharField(max_length=100 , null=True , choices=STATUS) #choices=STATUS هذه نخبره ان قيمه محددة بالقيم المعطاه اله فقط ويختار المستخدم منهن فقط 
    created_at = models.DateTimeField(auto_now_add=True , null=True)

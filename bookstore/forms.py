from django.forms import ModelForm
from .models import order
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#هنا يقوم ببناء الفورم حسب شو عنا في الجدول او الموديل هو بقرأ الفيلدز وبقرر عشان هيك بنعرف شو الموديل وشو يوخذ من 
class Orderform(ModelForm):
    class Meta: 
        model = order #نربط الكلاس مع الموديل اللي بنحط هون (order)
        fields = "__all__"#هيك بنجيب كل الداتا


class regesterform(UserCreationForm):
    class Meta: 
        model = User #نربط الكلاس مع الموديل اللي بنحط هون (order)
        fields = ['username' ,'email' , 'password1', 'password2']#هيك بنجيب كل الداتا
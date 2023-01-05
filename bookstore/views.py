from django.shortcuts import render, HttpResponse ,redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate ,login , logout
from .forms import *
# Create your views here.


def Home(request):
    return render(request, "BookStore/home.html" )

def Books(request):
    books =Book.objects.all()
    return render(request, "BookStore/Books.html", {'books' :books})

#صفحة الزبون وعرض وكل طلباته
def customer(request ,pk):
    Customers= Customer.objects.get(id =pk) #\روح على الموديل \اوردر\ وجيب الداتا وهات منها اللي \الاي دي\ تبعها بساوي\ بي كي
    orders =Customers.order_set.all()# يجلب طلبات كل زبون بعد ان اخترناه من الاي دي 
    count_orders=orders.count() 
    context={
        'custemer' :Customers,
        'orders': orders,
        'count_orders' :count_orders
    }
    return render(request , "BookStore/customer.html" , context)

def dashbord(request):
    Orders =order.objects.all()
    Customers =Customer.objects.all()


    return render(request , "BookStore/dashbord.html" , {'Orders' : Orders , 'Customers':Customers})



    # create
def create(request):
    form = Orderform()
    if request.method=="POST":
        form = Orderform(request.POST)        #request.POST عبارة عن البيانات القادمة من المستخدم
        if form.is_valid():
            form.save()
            return redirect('dashbord')
    context ={
        'form':form
    }
    return render(request , "BookStore/my_order_form.html" ,context)



    
def Update(request ,pk):
    Order = order.objects.get(id = pk)#\روح على الموديل \اوردر\ وجيب الداتا وهات منها اللي \الاي دي\ تبعها بساوي\ بي كي
    form = Orderform(instance=Order )
    if request.method=="POST":
        form = Orderform(request.POST , instance=Order)   #request.POST عبارة عن البيانات القادمة من المستخدم
        if form.is_valid():
            form.save()
            return redirect('dashbord')
    context ={'form':form }

    return render(request , "BookStore/my_order_form.html" ,context)

    
    
def delete(request ,pk):
    Order = order.objects.get(id = pk)
    if request.method=="POST":
        Order.delete()
        return redirect('dashbord')


    context ={'Order':Order }

    return render(request , "BookStore/delete.html" ,context)


    
def regester(request ):
    form = regesterform()
    if request.method=="POST":
        form = regesterform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashbord')
    context ={ 'form':form}
    return render(request , "BookStore/regester.html" ,context)


    
def userlogin(request ):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        login(request,user)
        return redirect('dashbord')


    context ={ }
    return render(request , "BookStore/login.html" ,context)

    
def userlogout(request ):
    logout(request)
    return redirect('userlogin')


from django.contrib import admin

# Register your models he
from .models import Book ,Customer ,order ,Tag
#from .models import * نفس اللي فوق

admin.site.register(Book)
admin.site.register(Customer)
admin.site.register(order)
admin.site.register(Tag)
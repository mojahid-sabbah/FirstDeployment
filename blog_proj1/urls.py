
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('' , include('bookstore.urls')),  # just to connect the project (blog_proj1) with {app (BookeStore)} using urls
    path('admin/', admin.site.urls),

]

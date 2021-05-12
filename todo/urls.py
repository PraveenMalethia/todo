from django.contrib import admin
from django.urls import path
from myapp.views import Index , Completed , NonCompleted , Delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Index),
    path('complete/<int:id>/',Completed),
    path('un-complete/<int:id>/',NonCompleted),
    path('delete/<int:id>/',Delete)
]

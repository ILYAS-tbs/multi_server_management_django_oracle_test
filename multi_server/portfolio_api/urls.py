from django.urls import path

from . import views 

urlpatterns = [
    path("first", views.sayHelloView ),
    path("second", views.replyWithJsonview ),

]

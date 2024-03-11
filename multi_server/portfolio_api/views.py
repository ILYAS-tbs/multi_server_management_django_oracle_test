from django.shortcuts import render

from django.http import HttpResponse

from django.http import JsonResponse

# Create your views here.
def sayHelloView(request): 


    return HttpResponse("hello , world! ")


def replyWithJsonview(request): 

    data = { "message":"From the server , in the cloud ....."}
    
    return JsonResponse(data)
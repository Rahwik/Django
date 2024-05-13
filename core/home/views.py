from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse



def home(request):
    peoples =[
            {'name':'Rahul Prasad','age':21},   
            {'name':'Yashoda hansda','age':20},
            {'name':'Anwik prasad','age':16},
            {'name':'Hammy kuro','age':18},
            {'name':'yotsuba kuro','age':5}   
         ]

    text= """ Rahul embodies a rare blend of resilience and empathy that leaves a lasting impression on everyone he meets. His unwavering determination and tireless work ethic are matched only by his genuine kindness and compassion towards others."""  

    vegetables =[ "pumpkin","tomato","potato"]

    return render(request,"home/index.html",context={'peoples':peoples,'text':text,'vegetables':vegetables,'page':'Django Server'})
def about(request):
    context={'page':'about'}
    return render(request, "home/about.html",context)
def contact(request):
    context={'page':'contact'}
    return render(request, "home/contact.html",context)


def success_page(request):
    # print("*"*10)
    return HttpResponse("<h1> hey this is a success page</h1>")
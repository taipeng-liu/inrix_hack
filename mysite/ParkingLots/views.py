from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def say_hello(request):
    return render(request, 'hello.html')
    # return HttpResponse("hello")


def check(request):
    # u_name is the name of the input tag
    name = request.POST.get('u_name', None)
    print(name)
    #age = request.POST['age']
    #address = request.POST['address']
    return render(request, 'hello.html')


def detail(request):
    first_name = 'a'
    context = {'name': first_name}
    return render(request, 'hello.html', context)

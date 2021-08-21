from datetime import datetime
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


def home(request):
    return HttpResponse("<h1>Hello Chandan</h1>")


def profile(request):
    return HttpResponse('This is my profile')


def content(request):
    return render(request, 'first.html')


def dynamiccontent(request):
    return render(request, 'second.html', {'Name': 'Chandan H'})


def bootstrap_add(request):
    return render(request, 'index.html')


def dateandtime(request):
    today = datetime.now()
    return render(request, 'date.html', {'d': today})


def add(request):
    return render(request, 'input.html', {'name': "Chandan H"})


def addresult(request):
    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    res = val1 + val2
    return render(request, 'result.html', {"Answer": res})


def arithmetic(request):
    return render(request, 'arithinput.html')


def arithresult(request):
    a = int(request.GET['a'])
    b = int(request.GET['b'])
    but = request.GET['bt']
    r = 0
    if but == "+":
        r = a + b
    elif but == "-":
        r = a - b
    elif but == "*":
        r = a * b
    elif but == "/":
        r = a / b
    return render(request, 'arithresult.html', {"Answer": r})


def hyperlink(request):
    return render(request, 'link.html')


def reginput(request):
    return render(request, 'reginput.html')


def regpreview(request):
    a = request.GET['na']
    b = request.GET['ag']
    c = request.GET['la']
    d = request.GET['em']
    e = request.GET['cp']
    dic = {"name": a, "age": b, "lang": c, "email": d, "pass": e}
    return render(request, 'regpreview.html', dic)


def signup(request):
    if request.method == 'POST':
        uname = request.POST['un']
        fname = request.POST['fn']
        lname = request.POST['ln']
        mailid = request.POST['email']
        passwd = request.POST['pwd']
        x = User.objects.create_user(username=uname, first_name=fname, last_name=lname, email=mailid, password=passwd)
        x.save()
        print("User created")
        return redirect('/')
    else:
        return render(request, 'signup.html')

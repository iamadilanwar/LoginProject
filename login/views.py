import pyautogui
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username1=request.POST['username']
        password1=request.POST['password']
        from django.contrib import auth
        user=auth.authenticate(username=username1, password=password1)

        if user is not None:
            auth.login(request,user)
            from .models import uploads
            d = uploads.objects.all()
            # p=d [len(d)-1].pic
            return render(request,'login.html',{'d': d})
            #return redirect('/')
        else:
            pyautogui.alert("Wrong Username and Password")
            return render(request,'loginpage.html')
            #return redirect(login)
    else:
        return render(request,'loginpage.html')

def upload (request):
    p=request.FILES['image']
    from.models import uploads
    d= uploads(pic=p)
    d.save
    pyautogui.alert("Uplode Done")
    d= uploads.objects.all()
    #p = d[len(d)-1].pic
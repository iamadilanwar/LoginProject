

# Create your views here.
def home(request):
    from django.shortcuts import render
    return render(request,'index.html')
from django.shortcuts import render
from isbat.forms import UserRegistrationForm

# Create your views here.
def indexpage(request):
    return render(request, 'app/index.html')

def usersignup(request):
    myform=UserRegistrationForm()
    return render(request, 'app/signup.html',{'form':myform})

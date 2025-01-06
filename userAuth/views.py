from django.shortcuts import render 
from django.http import HttpResponse
from .forms import UserForm
from .models import User
from django.shortcuts import redirect



from django.db import connection ##new line



is_authenticated = False 

def checkAuthentication():
    return is_authenticated


def login(request):
    
    global is_authenticated 
    message = "Please login"
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid(): 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password'] # todo: need to handle password field seperately.
            

            user_obj = User.objects.filter(username=username, password=password)
            if user_obj.exists():
                message = "Login Request successful"
                is_authenticated = True 
                return render(request, 'homepage.html')

            else:
                message = "Login Request fail. Please try again or register for a new account"

        
    return render(request, 'login_homepage.html', {'message': message})


def register(request):
    
    message = "Please Register"
    global is_authenticated 
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid(): 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password'] # todo: need to handle password field seperately.
            print(username, password) 
            newUser = User()
            newUser.username = username 
            newUser.password = password
            
            newUser.save()
            message = 'Successfully registered'
            is_authenticated = True 
            return render(request, 'homepage.html')
            # return HttpResponse("<h1>successful login request</h1>")

        
    return render(request, 'register_homepage.html', {'message': message})
    

# Create your views here.

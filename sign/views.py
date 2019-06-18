from django.shortcuts import render, HttpResponse, redirect
from .forms import Custom_user_form
import requests
# Create your views here.

def register_view(request, *args, **kwargs):
    if(request.method == "GET"):
        custom_user_form = Custom_user_form()
        return render(request, 'register.html', {'form': custom_user_form})
    else:
        print("###################")
        print(request.POST)
        print(request.FILES)
        print("###################")
        user = Custom_user_form(request.POST, request.FILES)
        if user.is_valid():
            # user = user.save()
            #user.set_password(user.password)
            # user.save()
            # user.is_staff =True
            # user.is_superuser = True
            uname = request.POST['username']
            fname = request.POST['first_name']
            email = request.POST['email']
            password = request.POST['password']
            print('############### >>> ',password)
            output = requests.post('http://127.0.0.1:3000/api/CreateUser', data={"$class": "com.pax.signature.CreateUser", "emailId": email, "name": uname,  "password": password})
            if(output.status_code == 200):
                return HttpResponse ('You are registered')
            else:
                return HttpResponse('Something Error')
        else:
            return HttpResponse('User not valid')
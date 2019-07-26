from django.shortcuts import render, HttpResponse, redirect
from user.models import Custom_user
from django.contrib import messages
from user.forms import Custom_user_form
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def register(request):
    if request.method == 'GET':
        custom_user_form = Custom_user_form()
        return render(request, 'user/register.html', {'form':custom_user_form})
    else:
        print("###################")
        print(request.POST)
        print(request.FILES)
        print("###################")
        user = Custom_user_form(request.POST, request.FILES)
        if user.is_valid():
            user = user.save()
            user.set_password(user.password)
            user.save()
            user.is_staff =True
            # user.is_superuser = True
            messages.success(request, 'Login Successful')
            return redirect(request, 'home:home')
        else:
            return HttpResponse('Error during submission')


@csrf_exempt
def user_login(request):
    if request.method == 'GET':
        custom_user_form = Custom_user_form()
        return render(request, 'user/login.html', {'form':custom_user_form})

    else:

        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        user = authenticate(username=username, password=password, email=email)


        if user:
            if user.is_active:
                login(request, user)
                messages.success(request, 'Login Successful')
                return redirect('home:home')
            else:
                messages.warning(request, 'Sorry, You are not active.')
                return redirect('user:register')

        else:
            messages.error(request, 'Sorry Recheck your username or password')
            return redirect('user:register')


def user_logout(request):
    logout(request)
    return redirect("user:login")
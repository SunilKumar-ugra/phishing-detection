# importing required packages
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from phishApp import phishing_detection
from django.http import HttpResponse
from phishApp.PhishingSiteDetection import loadModel


# disabling csrf (cross site request forgery)
@csrf_exempt
def getResult(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    # if post request came
    if request.method == 'POST':
        # getting values from post
        url = request.POST.get('url')
        response = phishing_detection.resolve(url)
        print(response)
        # return render(request, 'index.html', {"r": response})
        return render(request, 'index.html', {"success_msg": response})


@csrf_exempt
def API(request):
    # if post request came
    if request.method == 'POST':
        # getting values from post
        url = request.POST.get('url')
        print("URL = " + url)
        response = phishing_detection.resolve(url)
        return HttpResponse(response, status=200)


@csrf_exempt
def screenshot(request):
    if request.method == 'POST':
        image = request.POST.get('image')
        url = request.POST.get('url')
        print("Image = " + image)
        print("Url = " + url)
        response = loadModel.testCase(image, url)
        return HttpResponse(response, status=200)


# from here




# Create your views here.
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Auth
from django.http import JsonResponse, HttpResponse
import uuid
from django.contrib.auth import authenticate, login
from django.template.context import RequestContext
import os
import glob


@csrf_exempt
def home(request):
    if request.method == 'GET':
        return render(request, 'login.html')


@csrf_exempt
def login(request,):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            # login(request)
            return render(request, 'index.html') # Redirect to a success page.
        else:
            return render(request, 'login.html', {"error_msg": "Username and password does not match!!..."})
            # Return a 'disabled account' error message
    else:
        return render(request, 'login.html', {"error_msg": "Invalid login!!..."})
        # Return an 'invalid login' error message.


@csrf_exempt
def dashboard(request):
    if request.method == 'GET':
        return render(request, 'index.html')


@csrf_exempt
def logout(request):
    # if request.method == 'POST':
    return render(request, 'login.html', {"logout_msg": "Logout Successful!!..."})

@csrf_exempt
def reset(request):
    if request.method == 'POST':
        username = request.POST['reset-username']
        new_password = request.POST['reset-password']

        try:
            info = Auth.objects.get(user_name=username)
            info.password = new_password
            info.save()

            return render(request, 'login.html', {"reset_success_msg": "Password Updated"})
        except:
            return render(request, 'login.html', {"reset_error_msg": "User does not exists!!..."})





from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout as django_logout
import datetime
from .models import Contact,Profile
from .forms import ProfileForm

def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return render(request,'users/signup.html')
            elif len(password) <8:
                messages.info(request,'ATLEAST 8 CHARACTER PASSWORD NEEDED')
                return render(request,'users/signup.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return render(request,'users/signup.html')
            else:
                entry=User.objects.create_user(username=username,email=email,password=password)
                entry.save()
                messages.success(request,'Account Created!')
                return HttpResponseRedirect(reverse('login'))
        else:
            messages.info(request,'Password and confirm password didn"t match')
    return render(request,'users/signup.html')


@login_required
def contact(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        contacted_by=request.user
        contacted_on=datetime.datetime.now()
        contact_entry=Contact(name=name,subject=subject,message=message,contacted_by=contacted_by,contacted_on=contacted_on)
        contact_entry.save()
        messages.success(request,'THANKS FOR CONTACTING US! WE WILL REACH TO U ASAP')
        return HttpResponseRedirect(reverse('index:index'))
    return render(request,'users/contact.html')


@login_required
def profile(request):
    pqueryset=Profile.objects.filter(user=request.user)
    return render(request,'users/profile.html',{'pqueryset':pqueryset})

@login_required
def profile_update(request):
    queryset_update=Profile.objects.get(user=request.user)
    form = ProfileForm(request.POST or None, instance = queryset_update)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('users:profile'))
    return render(request,'index/profile_update.html',{'queryset_update':queryset_update,'form':form})

@login_required
def logout(request):
    django_logout(request)
    messages.info(request,'You have been logged out')
    return HttpResponseRedirect(reverse('login'))
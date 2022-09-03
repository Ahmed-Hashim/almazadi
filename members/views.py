from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .forms import ProfileForm,UserUpdateForm,PasswordChangingForm
from django.contrib.auth.decorators import login_required


class PasswordsChangeView(SuccessMessageMixin,PasswordChangeView):
    form_class=PasswordChangingForm
    success_url= reverse_lazy('settings')
    success_message= "Your password has been changed."

def login_user(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,"Welcome")
            return redirect('dashboard')
        else:
            return redirect('login')
    return render(request,'login.html')
@login_required
def logout_user(request):
    logout(request)
    messages.success(request,"You are logged out..")
    return redirect('login')

@login_required
def profile(request):

    profile=request.user.profile
    context={'profile':profile,
    }
    form=ProfileForm(instance=profile)

    if request.method =='POST':
        form= ProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
        
        return redirect("profile")
    context={'update_profile':profile,'form':form,'profile':profile,
                
    }
    return render(request,'registration/profile.html',context)
@login_required
def settings(request):
    user=request.user
    context={'profile':user,
    }
    form=UserUpdateForm(instance=request.user)

    if request.method =='POST':
        form= UserUpdateForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
        
        return redirect("settings")
    context={'settings':settings,'form':form,
                
    }
    return render(request,'registration/settings.html',context)

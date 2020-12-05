from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from account.forms.change_profile_img import ProfileForm
from account.forms.sign_up import SignUpForm
from account.models import UserProfile


def user_profile(req, pk=None):
    try:
        user = User.objects.get(pk=pk)
    except:
        user = req.user

    if req.method == 'GET':
        context = {
            'profile_user': user,
            'pets': user.userprofile.pet_set.all(),
            'form': ProfileForm()
        }
        return render(req, 'accounts/user_profile.html', context=context)
    else:
        form = ProfileForm(req.POST, req.FILES, instance=user.userprofile)
        if form.is_valid():
            form.save()
            redirect('current user profile')

        return redirect('current user profile')



def user_signup(req):
    if req.method == 'GET':
        context = {
            'form': SignUpForm(),
        }

        return render(req, 'accounts/signup.html', context=context)
    else:
        form = SignUpForm(req.POST)
        if form.is_valid():
            user = form.save()
            profile = UserProfile(
                user=user,
            )
            profile.save()
            login(req, user)
            return redirect('index')

        context = {
            'form': form
        }

        return render(req, 'accounts/signup.html', context=context)


def user_signout(req):
    logout(req)
    return redirect('index')
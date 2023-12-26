from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm, UserUpdateForm, ProfileUpdateform
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from .models import Profile
from forum.models import Post
from django.contrib.auth.models import User
from forum.views import PostListView
from django.core.paginator import Paginator

# django message
"""
messages.debug
messages.success
messages.warning
messages.error
messages.info
"""

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}!")
            return redirect('login')
            
    else:
        form = RegisterForm()
    
    print(form)
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request, pk):
    # For profile
    profile = Profile.objects.get(user_id=pk)
    post = Post.objects.all().order_by('-date_posted')
    paginator = Paginator(post, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"profile": profile, "page_obj": page_obj}
    return render(request, 'users/profile.html', context)

def edit_profile(request, pk):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateform(request.POST, 
                                   request.FILES, 
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Your account has been updated!")
            return redirect('profile', request.user.id)

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateform(instance=request.user.profile)
    
    context = {'u_form': u_form, 'p_form': p_form}
    return render(request, 'users/edit_profile.html', context)


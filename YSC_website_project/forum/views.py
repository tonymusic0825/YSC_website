from django.shortcuts import render, redirect
from .models import Post
from django.views.generic import CreateView, ListView
from .forms import CreateForumPostForm
from django.contrib.auth.decorators import login_required

def forum(request):
    return render(request, 'forum/forum.html', {'posts': Post.objects.all()})

class PostListView(ListView):
    model = Post
    template_name = 'forum/forum.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

def show_post(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'forum/post.html', {"post":post})

@login_required
def create_post(request):
    if request.method == 'POST':
        c_p_form = CreateForumPostForm(request.POST)
        if c_p_form.is_valid():
            post_obj = c_p_form.save(commit=False)
            post_obj.author = request.user
            post_obj.save()
            return redirect('forum')

    else:
        c_p_form = CreateForumPostForm()

    context = {'c_p_form' : c_p_form }
    return render(request, 'forum/create_post.html', context)

def edit_post(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        c_p_form = CreateForumPostForm(request.POST, instance=post)
        if c_p_form.is_valid():
            post_obj = c_p_form.save(commit=False)
            post_obj.author = request.user
            post_obj.save()
            return redirect('show_post', pk)
    else:
        c_p_form = CreateForumPostForm(instance=post)

    context = {'c_p_form' : c_p_form }
    return render(request, 'forum/edit_post.html', context)
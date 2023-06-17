from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator


def contact_us(requset):
    return render(requset, 'posts/contact.html') # just for render contact page

def about(requset):
    return render(requset, 'posts/about.html')  # just for render about page


def post_list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 4)  # Show 4 posts per page
    page = request.GET.get('page')
    paginated_posts = paginator.get_page(page)
    return render(request, 'posts/post_list.html', {'posts': paginated_posts})


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'posts/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'posts/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/post_edit.html', {'form': form})

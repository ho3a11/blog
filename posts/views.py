from django.shortcuts import render, redirect,get_object_or_404
from .models import Post , Category
from .forms import PostForm , CategoryForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required


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

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts:post_detail', pk=post.pk)
    else:
        # categories = Category.objects.all()
     
        form = PostForm()
        
    return render(request, 'posts/post_edit.html', {'form': form  })


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/post_edit.html', {'form': form})



def search(request):
    query = request.GET.get('query')
    if query:
        results = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
    else:
        results = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': results})

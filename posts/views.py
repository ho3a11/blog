from django.shortcuts import render, redirect,get_object_or_404
from .models import Post , Category ,Comment
from .forms import PostForm , CategoryForm ,CommentForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from taggit.models import Tag


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


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    tags = post.tags.all()
    similar_posts = Post.objects.filter(tags__in=post.tags.all()).exclude(id=post.id).distinct()[:3]
    comments = post.comments.filter(active=True)
    return render(request, 'posts/post_detail.html', {'post': post,
                                                      'comments':comments, 
                                                      'tags': tags, 
                                                      'similar_posts':similar_posts})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts:index')
    else:

        form = PostForm()
        
    return render(request, 'posts/post_edit.html', {'form': form  })


@login_required
def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts:post_detail', slug=post.slug)
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



#--------------Commenitig-----------------------------

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            if request.user.username == 'admin': # active comment for admin 
                comment.active=True
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('posts:post_detail', slug=post.slug)
    else:
        form = CommentForm()
    return render(request, 'posts/post_detail.html', {'form': form})

def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('posts:post_detail', slug=post_pk.slug)

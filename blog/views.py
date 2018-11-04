from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here.
def post_list(request):
    qs = Post.objects.all()
    qs = qs.filter(published_date__lte=timezone.now())
    qs = qs.order_by('published_date')

    return render(request, 'blog/post_list.html', {'post_list': qs})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    # user가 form에 입력하고 save를 누르면 request.POST에 내용이 저장, request.FILES에 첨부한 파일저장? 이 된다.
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid(): # 유효성 검사 (빠진 값 같은게 있는지)
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save() # db에 저장
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()

    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid(): # 유효성 검사 (빠진 값 같은게 있는지)
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save() # db에 저장
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_edit.html', {'form': form})
from django.shortcuts import render,redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

def voca_list(request):
    voca_set = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    if request.method=='POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.creaed_date = timezone.now()
            form.save()
        return redirect('/')
    else:
        form = PostForm()
    return render(request, 'memo/voca_list.html', {'voca_set':voca_set, 'form':form})

def voca_del(request,word):
    query = Post.objects.get(vocabulary=word)
    query.delete()
    return voca_list

from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts1 = Post.objects.all().order_by('-pk')
    return render(request, 'blog/index.html', {'posts2': posts1}) #오른쪽 posts는 위에서 선언한 posts!


def single_post_page(request, pk):
    post2 = Post.objects.get(pk=pk) #왼쪽 pk는 post가 가지고 있는 field 이름
    return render(request, 'blog/single_post_page.html', {'post': post2})
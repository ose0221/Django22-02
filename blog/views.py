from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.
class PostList(ListView):
    model = Post
    ordering = '-pk'
    #템플릿 모델명_list.html : post_list.html (자동 생성>>템플릿 이름 명시 필요 없음)
    #파라미터 모델명_list : post_list


class PostDetail(DetailView):
    model = Post
    #템플릿 모델명_detail.html : post_detail.html (템플릿 이름을 자동으로 부름)
    #파라미터 모델명 : post

#def index(request):
#    posts1 = Post.objects.all().order_by('-pk')
#    return render(request, 'blog/index.html', {'posts2': posts1}) #오른쪽 posts는 위에서 선언한 posts!


#def single_post_page(request, pk):
#    post2 = Post.objects.get(pk=pk) #왼쪽 pk는 post가 가지고 있는 field 이름
#    return render(request, 'blog/single_post_page.html', {'post': post2})
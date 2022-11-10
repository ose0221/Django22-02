from django.shortcuts import render, redirect
from .models import Post, Category, Tag
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied

# Create your views here.
class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'hook_text', 'content', 'head_image', 'file_upload', 'category','tags']

    template_name = 'blog/post_update_form.html'
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(PostUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostUpdate, self).get_context_data() ##템플릿에서 필요한 거 담아서 전달
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count
        return context

class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model=Post
    fields = ['title','hook_text','content','head_image','file_upload','category']

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_superuser or current_user.is_staff):
            form.instance.author = current_user #form의 author값을 현재 로그인된 값으로 설정해줌
            return super(PostCreate,self).form_valid(form)
        else:
            return redirect('/blog/')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostCreate, self).get_context_data() ##템플릿에서 필요한 거 담아서 전달
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count
        return context

    # 템플릿 모델명_form.html : post_form.html (자동 생성>>템플릿 이름 명시 필요 없음)

class PostList(ListView):
    model = Post
    ordering = '-pk'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostList, self).get_context_data() ##템플릿에서 필요한 거 담아서 전달
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count
        return context

    #템플릿 모델명_list.html : post_list.html (자동 생성>>템플릿 이름 명시 필요 없음)
    #파라미터 모델명_list : post_list

class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail,self).get_context_data()
        context['categories']=Category.objects.all()
        context['no_category_post_count']=Post.objects.filter(category=None).count
        return context

    #템플릿 모델명_detail.html : post_detail.html (템플릿 이름을 자동으로 부름)
    #파라미터 모델명 : post

def category_page(request,slug):
    if slug=='no_category':
        category='미분류'
        post_list=Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug) #왼쪽 필드명, 오른쪽 url을 통해 전달된 slug값
        post_list=Post.objects.filter(category=category)
    return render(request, 'blog/post_list.html',
                  {'category' : category,
                   'post_list' : post_list, #Post.objects.filter(category=category)
                   'categories' : Category.objects.all(),
                   'no_category_post_count' : Post.objects.filter(category=None).count
                   })


def tag_page(request, slug):
    tag = Tag.objects.get(slug=slug)
    post_list = tag.post_set.all()

    return render(request, 'blog/post_list.html', {
        'tag' : tag,
        'post_list' : post_list,
        'categories': Category.objects.all(),
        'no_category_post_count': Post.objects.filter(category=None).count

    })

#def index(request):
#    posts1 = Post.objects.all().order_by('-pk')
#    return render(request, 'blog/index.html', {'posts2': posts1}) #오른쪽 posts는 위에서 선언한 posts!


#def single_post_page(request, pk):
#    post2 = Post.objects.get(pk=pk) #왼쪽 pk는 post가 가지고 있는 field 이름
#    return render(request, 'blog/single_post_page.html', {'post': post2})
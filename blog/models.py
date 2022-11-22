from django.db import models
from django.contrib.auth.models import User
import os

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/tag/{self.slug}/'

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/category/{self.slug}/'

    class Meta:
        verbose_name_plural = 'Categories'

class Post(models.Model):
    title = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=100, blank=True) #콘텐츠 내용 미리보기
    content = models.TextField()

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True) #blog 앞에 _media가 생략됨
    # %Y 2022, %y 22
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)

    created_at = models.DateTimeField(auto_now_add=True) #처음 생성 시간
    updated_at = models.DateTimeField(auto_now=True) #수정 후 저장할 때마다 갱신

    #추후 author 작성
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL) #CASCADE - 탈퇴 시, 게시물 삭제

    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    tags=models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return f'[{self.pk}]{self.title}:: {self.author}  : {self.created_at}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]
        #a.txt -> a txt //2개의 string이 배열 형태로 전달됨
        # b.docx -> b docx
        # c.xlsx -> c xlsx
        # a.b.c.txt -> a b c txt 인 경우도 있음 //즉, 확장자는 배열의 마지막 요소! => [-1]로 확장자 get

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author} : {self.content}'

    def get_absolute_url(self):
        return f'{self.post.get_absolute_url()}#comment-{self.pk}'
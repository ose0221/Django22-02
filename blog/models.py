from django.db import models
import os

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=100, blank=True) #콘텐츠 내용 미리보기
    content = models.TextField()

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True) #blog 앞에 _media가 생략됨
    # %Y 2022, %y 22
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #추후 outhor 작성

    def __str__(self):
        return f'[{self.pk}]{self.title} : {self.created_at}'

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
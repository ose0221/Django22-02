from django.contrib import admin
from .models import Post, Category, Tag, Comment

# Register your models here.
admin.site.register(Post)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name', )} #처음에는 slug를 name으로 하겠다는 뜻

admin.site.register(Category, CategoryAdmin)

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name', )}

admin.site.register(Tag, TagAdmin)

admin.site.register(Comment)
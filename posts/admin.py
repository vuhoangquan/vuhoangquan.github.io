from django.contrib import admin
from .models import Post, Category, Author, SubCategory

class PostAdmin(admin.ModelAdmin):
    list_display = ("id","title", "description")
    
class CategoryAdmin(admin.ModelAdmin):
    filter_horizontal = ("posts",)

    
# Register your models here.
admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Author)
admin.site.register(SubCategory)
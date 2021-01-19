from django.contrib import admin
from .models import Post, Category, Author, SubCategory

class PostAdmin(admin.ModelAdmin):
    list_display = ("id","title", "description")
    filter_horizontal = ("categories",)

    
# class CategoryAdmin(admin.ModelAdmin):
#     filter_horizontal = ("posts",)
    
# class AuthorAdmin(admin.ModelAdmin):
#     filter_horizontal = ("writes",)

admin.site.site_url ="../posts/"
# Register your models here.
admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(SubCategory)

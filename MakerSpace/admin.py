from django.contrib import admin
# from .models import MakerSpace
from .models import * #* 代表import全部



# class MakerSpaceAdmin(admin.ModelAdmin):
#     list_display = ('prompt',)
# # Register your models here.
# admin.site.register(MakerSpace,MakerSpaceAdmin)  #註冊至Administration(管理員後台)


# class Member_SpaceAdmin(admin.ModelAdmin):
#      list_display = ('prompt')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Category, CategoryAdmin)


class PromptBaseAdmin(admin.ModelAdmin):
    list_display = ['category','keyword']
    list_filter = ['category','keyword']
    list_editable = ['keyword']
admin.site.register(PromptBase, PromptBaseAdmin)



class ImageInline(admin.TabularInline):
    model = Image
    raw_id_fields = ['picturebook']

class PicturebookAdmin(admin.ModelAdmin):
     list_display = ('title','outline', 'date') # list
     # fields = ('picturebook_ID','title','outline','date')
     inlines = [ImageInline]


# admin.site.register(Member_space)
admin.site.register(Picturebook,PicturebookAdmin)
admin.site.register(Image)



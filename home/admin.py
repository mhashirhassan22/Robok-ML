from django.contrib import admin
from .models import ImageRequest, User
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html

# Register your models here.

class UserAdmins(UserAdmin):
    list_display = ('email','company','business_case','is_active')
    list_editable = ('is_active',)

class ImageAdmin(admin.ModelAdmin):
    list_filter = ('user',)
    list_display = ('id','user', 'get_uploaded_image','get_result','created_at')
    fields = ['user','get_uploaded_image', 'get_result','created_at']
    readonly_fields = ['get_uploaded_image','get_result','created_at','user']

    def order_items(self, obj):
        obj_list = list(OrderItems.objects.filter(order=obj))
        if not obj_list:
            return ""
        l=len(obj_list)
        if l==1:
            return format_html('&#x2022;&nbsp;' + str(obj_list[0]))
        else:
            return f

    def get_uploaded_image(self, obj):
        return format_html("<img src='"+obj.uploaded_image.url+"' style='max-width:300px;' />")
    get_uploaded_image.allow_tags = True

    def get_result(self, obj):
        if obj.result:
            return format_html("<img src='"+obj.result.url+"' style='max-width:300px;' />")
        else:
            return "No result fors this"
    get_result.allow_tags = True


admin.site.register(ImageRequest,ImageAdmin)
admin.site.register(User,UserAdmins)
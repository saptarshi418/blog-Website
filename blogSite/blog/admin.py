from django.contrib import admin
from blog.models import Categories , WriteBlog
# Register your models here.


class CatagoryAdmin (admin.ModelAdmin):
    list_display =('category_name',)

admin.site.register(Categories,CatagoryAdmin)



# regester blog wite
admin.site.register(WriteBlog)
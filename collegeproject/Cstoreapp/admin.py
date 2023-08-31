from django.contrib import admin
from . models import Department,Courses,Product,Register


# Register your models here
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Department,DepartmentAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = ['cname','slug']
    prepopulated_fields = {'slug':('cname',)}
admin.site.register(Courses,CourseAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['pname','stock','available']
    list_editable = ['stock','available']
    prepopulated_fields ={'slug':('pname',)}
    list_per_page = 20
admin.site.register(Product,ProductAdmin)


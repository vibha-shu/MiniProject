from django.contrib import admin

# Register your models here.
from.models import *


class contactAdmin(admin.ModelAdmin):
  list_display=("name","contact","email","address","message")
admin.site.register(contact,contactAdmin)

class categoryAdmin(admin.ModelAdmin):
   list_display=("cname","cpic","cdate")
admin.site.register(category,categoryAdmin)

class registrationAdmin(admin.ModelAdmin):
   list_display=("name","mobile","email","passwd","ppic","address")
admin.site.register(registration,registrationAdmin)

class galleryAdmin(admin.ModelAdmin):
   list_display=("pdes","gpic","gdate")
admin.site.register(gallery,galleryAdmin)

class recuitersAdmin(admin.ModelAdmin):
   list_display=("rname","rpic","rdate")
admin.site.register(recuiters,recuitersAdmin)

class coursesAdmin(admin.ModelAdmin):
   list_display=("id","cname","cpic","cfee","cdate")
admin.site.register(courses,coursesAdmin)

class placementsAdmin(admin.ModelAdmin):
   list_display=("id","name","pcourse","branch","cmpname","cmplogo","city","pyear","designation","stupic","pdate")
admin.site.register(placements,placementsAdmin)






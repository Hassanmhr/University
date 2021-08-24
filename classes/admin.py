from django.contrib import admin

from .models import گروه_اموزشی,درس,کلاس

class گروه_اموزشیAdmin(admin.ModelAdmin):
    list_display = ('id','code_groh','name','modir_groh','status')
    list_display_links = ('id', 'name','modir_groh')

class درسAdmin(admin.ModelAdmin):
    list_display = ('id','cd_dars', 'name','count_vahed' ,'class_bargozari','for_group',)
    list_display_links =('id','name','for_group')
    list_filter = ('for_group','class_bargozari','count_vahed')
    search_fields = ('name','for_group','cd_dars')

admin.site.register(گروه_اموزشی ,گروه_اموزشیAdmin)
admin.site.register(درس,درسAdmin)
admin.site.register(کلاس)
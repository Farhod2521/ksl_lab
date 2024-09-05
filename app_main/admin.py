from django.contrib import admin
from .models import Menu, Page, File, Partners
from django.utils.html import format_html

class MenuAdmin(admin.ModelAdmin):
    list_display = ["title", "status"]
admin.site.register(Menu, MenuAdmin)



admin.site.register(Page)
class FileAdmin(admin.ModelAdmin):
    list_display = ["name", "file_link"]

    def file_link(self, obj):
        if obj.file:
            return format_html('<a href="{}" target="_blank">{}</a>', obj.file.url, obj.file.name)
        return "-"
    file_link.short_description = 'File'
admin.site.register(File, FileAdmin)



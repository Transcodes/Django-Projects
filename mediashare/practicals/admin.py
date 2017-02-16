from django.contrib import admin

from .models import Subject, MenuItem, Objective

# admin.site.register(Subject)
# admin.site.register(MenuItem)
# admin.site.register(Objective)


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject_name')

admin.site.register(Subject, SubjectAdmin)


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'menu_item', 'subject')

@admin.register(Objective)
class ObjectiveAdmin(admin.ModelAdmin):
    list_display = ('objective', 'menu_item', 'display_subject')
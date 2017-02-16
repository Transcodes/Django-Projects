from django.contrib import admin

from .models import Torrent

# admin.site.register(Subject)
# admin.site.register(MenuItem)
# admin.site.register(Objective)


class TorrentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category')

admin.site.register(Torrent, TorrentAdmin)

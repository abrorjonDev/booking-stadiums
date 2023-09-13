from django.contrib import admin

from stadiums.models import Stadium, StadiumImage


class ImageInline(admin.TabularInline):
    model = StadiumImage
    fields = ('media',)
    extra = 0


@admin.register(Stadium)
class StadiumAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'address', 'price_readable', 'status')
    list_filter = ('_status',)
    search_fields = ('name', 'contact', 'address')

    list_per_page = 25

    inlines = [ImageInline]

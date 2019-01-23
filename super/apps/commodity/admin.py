from django.contrib import admin

# Register your models here.
from commodity.models import ComClassModel, UnitModel, ComSpuModel, GalleryModel, ComSkuModel, BannerModel, \
    ActivityModel, ActivityZoneModel


@admin.register(ComClassModel)
class ComClassModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'class_name', 'class_intro', 'update_time']
    list_display_links = ['id', 'class_name', 'update_time']


admin.site.register(UnitModel)
admin.site.register(ComSpuModel)


class GalleryInline(admin.TabularInline):
    model = GalleryModel
    extra = 2


@admin.register(ComSkuModel)
class ComSkuModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'Sku_name', 'comintro', 'price', 'stock', 'sales', 'logo', 'is_on_sale']
    list_display_links = ['id', 'Sku_name', 'price']
    search_fields = ['Sku_name', 'price', 'sales']
    inlines = [
        GalleryInline
    ]


admin.site.register(BannerModel)
admin.site.register(ActivityModel)
admin.site.register(ActivityZoneModel)

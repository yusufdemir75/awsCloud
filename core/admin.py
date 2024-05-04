from django.contrib import admin
from core.models import *
# Register your models here.
@admin.register(GeneralSetting)

class GeneralSettingAdmin(admin.ModelAdmin):
    list_display=['id','name','description','parameter','updated_date','created_date']

    search_fields=['name','description','parameter']
    list_editable=['description','parameter']
    class meta:
        model= GeneralSetting

@admin.register(ImageSetting)
class ImageSettingAdmin(admin.ModelAdmin):
    list_display=['id','name','description','file','updated_date','created_date']

    search_fields=['name','description','file']
    list_editable=['description','file']
    class meta:
        model= ImageSetting

@admin.register(ProductImageSetting)
class ProductImageSettingAdmin(admin.ModelAdmin):
    list_display=['id','name','description','file','updated_date','created_date']

    search_fields=['name','description','file']
    list_editable=['description','file']
    class meta:
        model= ProductImageSetting

@admin.register(blogPageSetting)
class blogPageSettingAdmin(admin.ModelAdmin):
    list_display=['id','name','department','description','description1','description2','description3','comment','detail1','detail2','file','fileSmall','updated_date','created_date']

    search_fields=['name','description','file']
    list_editable=['name','department','description','description1','description2','description3','comment','detail1','detail2','file','fileSmall']
    class meta:
        model= blogPageSetting


@admin.register(commentSetting)

class commentSettingAdmin(admin.ModelAdmin):
    list_display=['id','file','comment','name','department','updated_date','created_date']

    search_fields=['file','comment','name','department']
    list_editable=['file','comment','name','department']
    class meta:
        model= commentSetting


@admin.register(contactSetting)
class contactSettingAdmin(admin.ModelAdmin):
    list_display=['id','address','tel','email','calisma_week','calisma_weekend','updated_date','created_date']

    search_fields=['address','tel','email','calisma_week','calisma_weekend']
    list_editable=['address','tel','email','calisma_week','calisma_weekend']
    class meta:
        model= contactSetting

@admin.register(message)
class MessageSettingAdmin(admin.ModelAdmin):
    list_display=['id','name','email','subject','message','updated_date','created_date']

    search_fields=['name','email','subject','message','updated_date','created_date']
    class meta:
        model= message
from django.contrib import admin
from django.conf import settings
from django import forms
from .models import *
from django.utils.safestring import mark_safe
from ckeditor.widgets import CKEditorWidget
from django.http import Http404, HttpResponseRedirect





#admin.site.unregister(Group)
admin.site.site_header = 'WEBCATcms'


class CategoryAdmin(admin.ModelAdmin):
    pass
    #fieldsets = [
    #    (None, {'fields':['title', 'image' ,'description', ]}),
    #    ('SEO налаштування', {'fields':['meta_keywords', 'meta_description']}),
    #            ]
    #list_display = ('description')
    #list_filter = ('title',)
    #actions_selection_counter = False
    #actions_on_top = True
    #actions_on_bottom = True


#class ObjectPropertyAdmin(admin.ModelAdmin):
#    pass
    #def image_tag(self,obj):

        #return mark_safe('<a href="#" ><img src="{}" width="50" height="50" /></a>'.format(obj.images.url))


    #image_tag.short_description = 'Зображення'
    #list_display = ('title','image_tag','object_type' ,'published', 'status')
    #date_hierarchy = 'published'
    #fields = ('title','description')
    #readonly_fields = ['image_tag']

    #fieldsets = [
    #    (None, {'fields':['title', 'description', 'object_type', 'locality', 'area', 'street', 'rooms', 'space', 'price', 'image_tag', 'image',]}),
    #    ('SEO налаштування', {'fields':['meta_keywords', 'meta_description']}),
    #]

def image_tag(obj):

    return mark_safe('<img src="{}" width="50" height="50" />'.format(obj.image.url))

class ObjectPropertyImageAdmin(admin.ModelAdmin):
  pass

class ObjectPropertyImageInline(admin.StackedInline):
  model = ObjectPropertyImage
  max_num = 10
  extra = 0
  fields = ['image']


class PageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ['title', 'image', 'description', 'status', ]}),
        ('SEO налаштування', {'fields': ['meta_description']}),
        ('Розміщення', {'fields': [('menu', 'information', 'about_as')]}),
    ]

class ObjectPropertyAdmin(admin.ModelAdmin):

    def image_tag(self,obj):

        return mark_safe('<img src="{}" width="50" height="50" />'.format(obj.image.url))

    image_tag.short_description = 'Зображення'
    list_display = ('title', 'category_object','image_tag','object_type' ,'published', 'status')

    inlines = [ObjectPropertyImageInline]


    fieldsets = [
        (None, {'fields':['title', 'category_object', 'image' ,'description', 'object_type', 'locality', 'area', 'street', 'rooms', 'total_space', 'living_space', 'kitchen_space', 'height', 'floor', 'storeys', 'price', 'recommended', 'status', ]}),
        ('SEO налаштування', {'fields':['meta_description']}),
        ]

class DontLog:
    def log_addition(self, *args):
        return ''

class SettingAdmin(DontLog,admin.ModelAdmin):

    fieldsets = [
        (None, {'fields':['title', 'base_url', 'phone_1', 'phone_2' ,'link_facebook', 'link_instagram', 'link_telegram', 'site_image',]}),
        ('SEO налаштування', {'fields':['meta_description']}),
        ]

    def response_change(self, request, obj):
        return HttpResponseRedirect('/admin')

    def has_add_permission(cls, request):
        ''' remove add and save and add another button '''
        return False

    def change_view(self, request, object_id, extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = False
        extra_context['show_save'] = True
        extra_context['show_delete'] = False
        extra_context['show_history'] = False
        return super(SettingAdmin, self).change_view(request, object_id, extra_context=extra_context)



admin.site.register(Page, PageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ObjectProperty, ObjectPropertyAdmin)
admin.site.register(ObjectPropertyImage, ObjectPropertyImageAdmin)
admin.site.register(Setting, SettingAdmin)

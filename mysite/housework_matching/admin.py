from django.contrib import admin

from .models import Housework


class HouseworkAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ['housework_text']
        }),
    ]
    list_display = ('housework_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['housework_text']


admin.site.register(Housework, HouseworkAdmin)

from rates.models import Rate, Choice
from django.contrib import admin


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra =3
admin.site.register(Choice)

class RateAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['library']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
inlines = [ChoiceInline]
admin.site.register(Rate, RateAdmin)

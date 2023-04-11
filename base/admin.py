from django.contrib import admin
# from modeltranslation.admin import TranslationAdmin
from .models import Team, Portfolio, Testimonials, Stats
# Register your models here.


# class TeamsAdmin(TranslationAdmin):
#     pass
admin.site.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'position']

admin.site.register(Portfolio)
class PorrfolioAdmin(admin.ModelAdmin):

    list_display = ['title', 'desc']

admin.site.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ['position', 'advice']


admin.site.register(Stats)
class StatsAdmin(admin.ModelAdmin):
    list_display = ['happy_clients']

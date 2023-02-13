from django.contrib import admin

from .models import *

@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = ['ip_address']

@admin.register(HomePageCarousel)
class HomePageAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'heading']

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'heading']

@admin.register(Expertise)
class ExpertiseAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'heading']

@admin.register(ServiceCard)
class CardAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'heading']

@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'heading']

@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ['id', 'logo']

@admin.register(WhyUsImage)
class ExpImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'image']

@admin.register(WhyUsSectionHeading)
class ExpHeadingAdmin(admin.ModelAdmin):
    list_display = ['id', 'heading']

@admin.register(WhyUsPoints)
class ExpPointAdmin(admin.ModelAdmin):
    list_display = ['id', 'serial', 'heading']

@admin.register(PhoneNumbers)
class NumberAdmin(admin.ModelAdmin):
    list_display = ['id', 'number']

@admin.register(ContactInfo)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'email_address', 'full_address']

@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ['id', 'facebook_link', 'twitter_link', 'instagram_link', 'youtube_link']

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['id', 'subscriber']

@admin.register(AboutPageMission)
class About_page_mission_admin(admin.ModelAdmin):
    list_display = ['id', 'image', 'heading']

@admin.register(AboutPageBanner)
class About_page_banner_admin(admin.ModelAdmin):
    list_display = ['id', 'image', 'heading']

@admin.register(ServicePageBanner)
class Service_page_banner_admin(admin.ModelAdmin):
    list_display = ['id', 'image', 'heading']

@admin.register(ContactPageBanner)
class Contact_page_banner_admin(admin.ModelAdmin):
    list_display = ['id', 'image', 'heading']

@admin.register(AboutPageVision)
class About_page_vision_admin(admin.ModelAdmin):
    list_display = ['id', 'image', 'heading']
from django.db import models


class HomePageCarousel(models.Model):
    image = models.ImageField(upload_to="home_page_carousel_images", verbose_name="Recommended image resulation is 1440 X 680 pixels")
    heading = models.CharField(max_length=200, null=True, blank=True)
    short_brief = models.CharField(max_length=200, null=True, blank=True)

class Experience(models.Model):
    heading = models.CharField(max_length=200, null=True, blank=True)
    text = models.TextField()
    image = models.ImageField(upload_to="common_pictures", verbose_name="Recommended image resulation is 480 X 380 pixels")

class Clients(models.Model):
    logo = models.FileField(upload_to="clients_logos")

class Expertise(models.Model):
    heading = models.CharField(max_length=200, null=True, blank=True)
    text = models.TextField()
    image = models.ImageField(upload_to="common_pictures", verbose_name="Recommended image resulation is 480 X 380 pixels")

class ServiceCard(models.Model):
    image = models.ImageField(upload_to="service_card_images", verbose_name="Recommended image resulation is 480 X 380 pixels")
    heading = models.CharField(max_length=200, null=True, blank=True)
    text = models.TextField()

class Mission(models.Model):
    image = models.ImageField(upload_to="common_pictures", verbose_name="Recommended image resulation is 480 X 380 pixels")
    heading = models.CharField(max_length=200, null=True, blank=True)
    text = models.TextField()

class WhyUsImage(models.Model):
    image = models.ImageField(upload_to="common_pictures", verbose_name="Recommended image resulation is 480 X 380 pixels")

class WhyUsSectionHeading(models.Model)    :
    heading = models.CharField(max_length=200, null=True, blank=True)

class WhyUsPoints(models.Model):
    serial = models.IntegerField(default=0, null=True, blank=True)
    heading = models.CharField(max_length=200, null=True, blank=True)
    text = models.TextField()

class PhoneNumbers(models.Model):
    number = models.CharField(max_length=200, null=True, blank=True)

class ContactInfo(models.Model):
    email_address = models.CharField(max_length=200, null=True, blank=True)
    full_address = models.TextField()

class Footer(models.Model):
    footer_text = models.TextField()
    facebook_link = models.URLField()
    twitter_link = models.URLField()
    instagram_link = models.URLField()
    youtube_link = models.URLField()

class Subscription(models.Model):
    subscriber = models.CharField(max_length=200, null=True, blank=True)

class AboutPageBanner(models.Model):
    image = models.ImageField(upload_to="common_pictures", verbose_name="Recommended image resulation is 1440 X 380 pixels")
    heading = models.CharField(max_length=200, null=True, blank=True)
    text = models.TextField()

class AboutPageMission(models.Model):
    image = models.ImageField(upload_to="common_pictures", verbose_name="Recommended image resulation is 480 X 380 pixels")
    heading = models.CharField(max_length=200, null=True, blank=True)
    text = models.TextField()

class AboutPageVision(models.Model):
    image = models.ImageField(upload_to="common_pictures", verbose_name="Recommended image resulation is 480 X 380 pixels")
    heading = models.CharField(max_length=200, null=True, blank=True)
    text = models.TextField()

class ServicePageBanner(models.Model):
    image = models.ImageField(upload_to="common_pictures", verbose_name="Recommended image resulation is 1440 X 380 pixels")
    heading = models.CharField(max_length=200, null=True, blank=True)
    text = models.TextField()

class ContactPageBanner(models.Model):
    image = models.ImageField(upload_to="common_pictures", verbose_name="Recommended image resulation is 1440 X 380 pixels")
    heading = models.CharField(max_length=200, null=True, blank=True)
    text = models.TextField()
from django.db import models


# Create your models here.

CATEGORY_CHOICES = (
    ('APP','APP'),
    ('CARD','CARD'),
    ('WEB','WEB'),
    ('BOT', 'BOT'),
)

class Team(models.Model):
    full_name = models.CharField(max_length=100, help_text="Enter your fullname")
    position = models.CharField(max_length=50, help_text="Occupation")
    image = models.FileField(null=True,upload_to='teams')
    linkedin = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.full_name



class Portfolio(models.Model):
    title = models.CharField(max_length=10, help_text="Ex: Web1, Web2, App1, Bot1, Card1")
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=4)
    image = models.FileField(upload_to='portfolio', blank=True)

    name = models.CharField(max_length=100, help_text="Category name, Web design, Graphic")
    client = models.CharField(max_length=50, help_text="Client name or organisation")
    project_date = models.DateField(auto_now_add=True)
    project_url = models.URLField(null=True, blank=True)
    project_title = models.CharField(max_length=100, blank=True)
    imag1 = models.FileField(upload_to="portfolio", blank=True, null=True)
    imag2 = models.FileField(upload_to="portfolio", blank=True, null=True)
    imag3 = models.FileField(upload_to="portfolio", blank=True, null=True)
    desc = models.TextField(null=True, help_text='about project')

    def __str__(self):
        return self.name


class Testimonials(models.Model):
    full_name = models.CharField(max_length=40, help_text='Clien name')
    position = models.CharField(max_length=40, help_text="Occupation")
    advice = models.TextField(help_text="description")
    image = models.FileField(upload_to='clients', blank=True, null=True)
    def __str__(self) -> str:
        return self.full_name




class Stats(models.Model):
    happy_clients = models.PositiveIntegerField()
    projects = models.PositiveIntegerField()
    hours_of_support = models.CharField(max_length=20)
    hard_work = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.happy_clients

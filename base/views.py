from django.core.mail import EmailMessage
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect

from base.models import *


def index(request):
    teams = Team.objects.all()
    stats = Stats.objects.filter()
    supports = Testimonials.objects.all()
    works = Portfolio.objects.all()
    context = {
        'active': 'index',
        'supports': supports,
        'teams':teams,
        'works':works,
        'stats':stats,

    }
    if request.method == "POST":
        name = request.POST['name']
        sender_email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        email = EmailMessage(
            f'Message from {sender_email}',
            f"Name: {name}\n\n Phone number: {phone}\n\n Left message: {message}\n\nEmail: {sender_email}\n\n",
            settings.EMAIL_HOST_USER,
            ['itis1info@gmail.com'],
        )


        email.fail_silently = True
        email.send()


        return HttpResponse("Sent successfully")


    return render(request, 'index.html', context)

def portfolio(request, pk):
    works = Portfolio.objects.all()
    work = Portfolio.objects.get(id=pk)


    context = {
        'active': 'portfolio',
        'works': works,
        'work':work,

    }
    return render(request, 'portfolio-details.html', context)

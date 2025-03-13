from django.shortcuts import render
from .models import AboutPage

def about_view(request):
    about = AboutPage.objects.first()
    context = {
        "title": "О нас",
        "content": about.content if about else "Информация скоро появится."
    }
    return render(request, "about.html", context)
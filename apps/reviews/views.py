from django.shortcuts import render
from .models import Review

def review_list(request):
    reviews = Review.objects.select_related('user', 'product').all()
    return render(request, 'reviews/reviews.html', {'reviews': reviews})
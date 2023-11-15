from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Advertisement
from .forms import AdvertisementsForm
import os


def index(request):
    advertisement = Advertisement.objects.all()
    context = {'advertisement': advertisement}
    return render(request, 'index.html', context)


def top_sellers(request):
    return render(request, 'top-sellers.html')


def advertisement_post(request):
    {% advertisement-post.html %}
    form = AdvertisementsForm()
    if request.method == 'POST':
        form = AdvertisementsForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = Advertisement(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('main-page')
            return redirect(url)
    context = {'form': form}
    return render(request, 'advertisement-post.html', context)

from django.shortcuts import render
from django.http import HttpResponse
from newsapi import NewsApiClient
from .models import Profile, News
from .forms import ProfileForm, NewsForm
from .utils import password_validation
from django.shortcuts import redirect


# Create your views here.

def index(request):
    form = NewsForm(request.GET)

    return render(
        request,
        'index.html',
        {'form': form}
    )


def index_view(request):
    message = None
    form = ProfileForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('news_etis:main')
        
    
    return render(
        request,
        'login.html', 
        {'form': form}
    )
    
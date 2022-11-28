from django.shortcuts import render
from django.http import HttpResponse
from newsapi import NewsApiClient
from .models import Profile
from .forms import ProfileForm
from .utils import password_validation
from django.shortcuts import redirect


# Create your views here.

def index(request):

    newsapi = NewsApiClient(api_key ='581afaeacaac42dea128bdf256215c87')
    top = newsapi.get_top_headlines(language='ru', country='ru')

    l = top['articles']
    dsc =[]
    nws =[]
    im =[]

    for i in range(len(l)):
      f = l[i]
      nws.append(f['title'])
      dsc.append(f['description'])
      im.append(f['urlToImage'])
      mylist = zip(nws, dsc, im)

    return render(request, 'index.html', context ={"mylist":mylist})


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
    
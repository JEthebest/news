from django import forms
from .models import Profile, News
from newsapi import NewsApiClient
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse


class ProfileForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Profile
        fields = ('login', 'password')
        
    def clean(self):
        cleaned_data = super(ProfileForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )
        if len(password) <= 8:
            raise forms.ValidationError(
                "password too short"
            )


class NewsForm(forms.ModelForm):
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

    # return render(request, 'index.html', context ={"mylist":mylist})
from shortner.forms import UrlForm
from django.shortcuts import render, redirect
from shortner.models import Url
import uuid


def home(request):
    form = UrlForm()
    if request.method == "POST":
        form = UrlForm(request.POST)
        if form.is_valid():
            link = form.cleaned_data['link']
            if ("http://" not in link) and ("https://" not in link) :
                link = "http://" + link 
            uid = str(uuid.uuid4())[:5]
            new_url = Url(link=link, uuid =uid)
            new_url.save()
            context = {
                "uid": uid
            }
            return  render(request, 'final.html', context)
    context  = {
        "form": form
    }
    return render(request, 'index.html', context)

def final(request, pk):
    url_details = Url.objects.get(uuid=pk)
    return redirect(url_details.link)
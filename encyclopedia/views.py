from re import S
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from . import util
from django import forms

# class SearchForm(forms.Form):
#     query = forms.CharField(
#         widget=forms.TextInput(attrs={'placeholder': 'Search'})
    # )

def index(request):
    # form = SearchForm()
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        # "form": form
    })

def entry(request, caption):
    caption = caption.upper()
    entry_body = util.get_entry(caption)
    if entry_body:
        return render(request, "encyclopedia/entry.html", {
            "caption": caption,
            "entry_body": entry_body,
        })
    else:
        return render(request, "encyclopedia/not_found.html")


def search(request):
    entries  = util.list_entries()
    entries = [entry.lower() for entry in entries]
    q = (request.POST.get('q')).lower()

    if q in entries:
        return HttpResponseRedirect(reverse("entry", kwargs={'caption': q}))
    else: 
        search_res = []
        for entry in entries:
            if q in entry:
                search_res.append(entry)
        return render(request, "encyclopedia/search.html", {
            "q": q,
            "search_res": search_res,
        })
from re import L, S
from django.http import request
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from . import util
from django import forms

import random as rand
from markdown2 import Markdown


def index(request):
    # form = SearchForm()
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        # "form": form
    })

def entry(request, caption):
    markdowner = Markdown()
    caption = caption
    entry_body = util.get_entry(caption)
    if entry_body:
        html = markdowner.convert(entry_body)
        return render(request, "encyclopedia/entry.html", {
            "caption": caption,
            "entry_body": html,
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


def validate_caption(value):
    if util.get_entry(value):
        raise ValidationError(
            _('%(value)s already exists.'),
            params={'value': value},
        )

 
class NewPageForm(forms.Form):
    caption = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Caption',
        'required': True,}),
        validators=[validate_caption], label="")
    body = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Body',
        'required': True}),
        label="")

def new_page(request):
    if request.method == "POST":
        form = NewPageForm(request.POST)
        if form.is_valid():
            caption = form.cleaned_data["caption"]
            body = form.cleaned_data["body"]
            util.save_entry(caption, body)
            return HttpResponseRedirect(reverse("entry", kwargs={'caption': caption}))
        return render(request, "encyclopedia/new_page.html", {
            "form": form,
        })
    return render(request, "encyclopedia/new_page.html",{
        "form": NewPageForm(),
    })

class EditPageForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Body',
        'required': True}), 
        label="")

def edit_page(request, caption):
    if request.method == "POST":
        form = EditPageForm(request.POST)
        if form.is_valid():
            body = form.cleaned_data["body"]
            util.save_entry(caption, body)
            return HttpResponseRedirect(reverse('entry', kwargs={"caption": caption}))
        return render(request, "encyclopedia/edit_page.html", {
            "form": form,
        })
    entry = util.get_entry(caption)
    if not entry:
        return render(request, "encyclopedia/not_found.html")
    # entry = entry.split("\n\n",1)[1]
    data = {
        "body": entry,
    }
    form = EditPageForm(data)
    return render(request, "encyclopedia/edit_page.html", {
        "form": form,
        "caption": caption,
    })

def random(request):
    entries = util.list_entries()
    caption = rand.choice(entries)
    return HttpResponseRedirect(reverse("entry", kwargs={"caption": caption}))

def tips(request):
    return render(request, "encyclopedia/formatting.html")
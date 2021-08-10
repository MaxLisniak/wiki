from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
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
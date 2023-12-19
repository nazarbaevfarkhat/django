from django.http import HttpResponse
from django.shortcuts import render

def first_page(request):
    a = '<h1> Hello World </h1>'
    text = "New text in line"

    return render(request, './index.html', {
        'a': a,
        'text': text
    })
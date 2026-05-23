from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect


def index(request):
    return HttpResponse('Главная страница')

def category(request, id=None, category_slug=None):
    if id is not None:
        if id==2:
            raise Http404()
        elif id==3:
            return redirect('main')
        return HttpResponse(f"Category Id {id}")
    elif category_slug is not None:
        return HttpResponse(f"Category slug {category_slug}")
    return HttpResponse("Category Page")

def page_not_found(request, exception):
    return render(request, 'myapp/not_found.html', status=404)
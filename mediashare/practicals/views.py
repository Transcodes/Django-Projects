from django.shortcuts import render
from .models import Subject, MenuItem, Objective
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

def index(request):
    subjects = Subject.objects.order_by('id')
    template = loader.get_template('practicals/index.html')
    context = {
        'subjects': subjects,
        }
    return HttpResponse(template.render(context, request))


def disqus(request):
    template = loader.get_template('practicals/disqus.html')
    return HttpResponse(template.render({}, request))



def detail(request, subject_name):
    try:
        subjects = Subject.objects.get(subject_name=subject_name)
    except Subject.DoesNotExist:
        raise Http404("Subject does not exist")
    menu_items = MenuItem.objects.filter(subject=subjects)
    objectives = Objective.objects.order_by('id')

    context = {
        'subjects': subjects,
        'menu_items': menu_items,
        'objectives': objectives,
    }
    template = loader.get_template('practicals/menuitem.html')
    return HttpResponse(template.render(context, request))


def objectives(request, subject_name, menu_item):
    try:
        subjects = Subject.objects.get(subject_name=subject_name)
    except Subject.DoesNotExist:
        raise Http404("Subject does not exists")
    try:
        menu_items = MenuItem.objects.get(menu_item=menu_item)
    except:
        raise Http404("This topic doesn't exist")
    objectives = Objective.objects.filter(menu_item=menu_items)
    context= {
        'subjects': subjects,
        'menu_items': menu_items,
        'objectives': objectives,
    }
    template = loader.get_template('practicals/objective.html')
    return HttpResponse(template.render(context, request))
from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse

from .models import Area, Sight

# Create your views here.
def sight_list(request):
    area_list = Area.objects.all()

    template = loader.get_template('sights/area_list.html')
    context = RequestContext(request, {'area_list':area_list,})

    return HttpResponse(template.render(context))

def sight_detail(request, sight_slug):
    template = loader.get_template('sights/sight_detail.html')
    sight = Sight.objects.get(slug=sight_slug)
    ctx={}
    ctx['sight'] = sight
    context = RequestContext(request, ctx)

    return HttpResponse(template.render(context))

def area_list(request):
    area_list = Area.objects.all()

    template = loader.get_template('sights/area_list.html')
    context = RequestContext(request, {'area_list':area_list,})

    return HttpResponse(template.render(context))

def area_detail(request, area_name):
    return HttpResponse('area_detail, area_name: %s' % area_name)
    return HttpResponse('sight_detail, sight_slug: %s' % sight_slug)

def area_list(request):
    area_list = Area.objects.all()

    template = loader.get_template('sights/area_list.html')
    context = RequestContext(request, {'area_list':area_list,})

    return HttpResponse(template.render(context))

def area_detail(request, area_name):
    return HttpResponse('area_detail, area_name: %s' % area_name)

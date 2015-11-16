from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse

# Create your views here.
def baidu_map(request):
    template = loader.get_template('map/baidu_map.html')
    ctx = {}
    ctx['name'] = 'meng'
    context = RequestContext(request, ctx)
    return HttpResponse(template.render(context))

def gg_map(request):
    template = loader.get_template('map/gg_map.html')
    ctx = {}
    ctx['name'] = 'meng'
    context = RequestContext(request, ctx)
    return HttpResponse(template.render(context))

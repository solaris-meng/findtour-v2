from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse

from .forms import PrivateTourForm, TestForm
from django.core.mail import send_mail
from django.core import serializers
from .config import *

# Create your views here.
def index_view(request):
    flog.info("PV, index, ")
    ctx = {}
    ctx['name'] = 'Meng'
    context = RequestContext(request, ctx)
    template = loader.get_template('index/index.html')

    return HttpResponse(template.render(context))
def about_view(request):
    flog.info("PV, about, ")
    ctx = {}
    ctx['name'] = 'Meng'
    context = RequestContext(request, ctx)
    template = loader.get_template('index/about.html')

    return HttpResponse(template.render(context))

def private_tour_view(request):
    flog.info("PV, index, ")
    ctx = {}
    ctx['name'] = 'Meng'
    context = RequestContext(request, ctx)
    template = loader.get_template('index/private_tour.html')

    return HttpResponse(template.render(context))

def form_to_text(form):
    form_dict = form.cleaned_data
    rv = str(form_dict)
    return rv

def private_tour_handler(request):
    if request.method == 'POST':
        flog.info("RQ, private_tour_handler")

        # save form
        form = PrivateTourForm(request.POST)
        if not form.is_valid():
            err = form.errors
            return HttpResponse('form is not valid:\n %s' % err)

        try:
            form.save()
        except:
            flog.error("save form failed")
            return HttpResponse("Failed, please contact info@findtour.co")

        # send mail
        from_email,to = 'isolate000@sina.cn','113153207@qq.com'
        subject = "Tour Order"
        data = form_to_text(form)
        text_content = 'hello'
        text_content = data
        print data
        #try:
        send_mail(subject, text_content, from_email, [to,],fail_silently=False)
        #except:
        #    flog.error("send email failed")

        # response
        template = loader.get_template('index/private_tour_handler.html')
        flog.info(form.is_valid())
        args = {}
        args['form'] = form
        context = RequestContext(request, args)

        return HttpResponse(template.render(context)) 

def form_test(request):
    flog.info("PV, form_test, ")
    form = TestForm('')
    ctx = {}
    ctx['form'] = form

    context = RequestContext(request, ctx)
    #template = loader.get_template('index/form_test2.html')
    template = loader.get_template('index/form_test.html')

    return HttpResponse(template.render(context))
def form_test_handler(request):
    if request.method == 'POST':
        flog.info("RQ, form_test_handler")

        form = TestForm(request.POST)
        if not form.is_valid():
            err = form.errors
            return HttpResponse('form is not valid:\n %s' % err)

        form.save()
        ctx = {}
        ctx['name'] = 'Meng'
        context = RequestContext(request, ctx)
        template = loader.get_template('index/form_test_handler.html')
        return HttpResponse(template.render(context)) 

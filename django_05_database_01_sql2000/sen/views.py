from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from sen.models import Jfxx
from sen.models import Jfxx as Question
from django.template import loader


def foo(request):
    return HttpResponse('姓名：{}'.format('name'))


def index(request):
    query = Jfxx.objects.all()
    template = loader.get_template('index.html')
    context = {
        'query': query,
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    try:
        question = Question.objects.all()
        # question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        from django.http import Http404
        raise Http404("Question does not exist")
    return render(request, 'detail.html', {'question': question})

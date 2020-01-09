from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse


def index(request):
    return render(request, 'app_ajax_index.html')
    
def add(request):
    a = request.GET['a']
    b = request.GET['b']
    a = int(a)
    b = int(b)
    return HttpResponse(str(a+b))

def ajax_list(request):
    a = range(100)
    return JsonResponse(list(a), safe=False)


def ajax_dict(request):
    name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
    return JsonResponse(name_dict)

def ajax_url_to_json(request):
    # person_info_dict = [
    #    {"name":"xiaoming", "age":20},
    #    {"name":"tuweizhong", "age":24},
    #    {"name":"xiaoli", "age":33}
    # ]
    person_info_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
    return JsonResponse(person_info_dict)

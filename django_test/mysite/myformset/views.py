from django.http import HttpResponse
from django.shortcuts import render,render_to_response
from django.views.generic import ListView
import datetime
# Create your views here.
from django.forms import formset_factory
from .forms import *
def test(request):
	
	# ArticleFormSet = formset_factory(ArticleForm, extra=2)
	ArticleFormSet = formset_factory(ArticleForm, extra=2, max_num=1)
	# formset = ArticleFormSet()
	formset = ArticleFormSet(initial=[
     {'title': 'Django is now open source',
      'pub_date': datetime.date.today(),}])
	for form in formset:
	    (form.as_table())

	return render(request, 'test.html', {'formset' : formset})

def manage_articles(request):
    ArticleFormSet = formset_factory(ArticleForm,can_delete=True)
    if request.method == 'POST':
        formset = ArticleFormSet(request.POST, request.FILES)
        if formset.is_valid():
            # do something with the formset.cleaned_data
            pass
    else:
        formset = ArticleFormSet()
    return render(request, 'manage_articles.html', {'formset': formset})
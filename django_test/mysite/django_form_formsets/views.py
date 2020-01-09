from django.forms import formset_factory, modelformset_factory
from django.shortcuts import render, Http404
from django.utils import timezone
# Create your views here.

from .forms import TestForm, PostModelForm
from .models import Post

def formset_view(request):
	if request.user.is_authenticated():
		PostModelFormset = modelformset_factory(Post, form=PostModelForm)
		# PostModelFormset = modelformset_factory(Post, fields=['user', 'title', 'slug'])
		# PostModelFormset = modelform_factory(Post, fields=['user', 'title'])
		# formset = PostModelFormset(request.POST or None)
		# formset = PostModelFormset(request.POST or None, queryset=Post.objects.filter(id__gt=2))
		formset = PostModelFormset(request.POST or None, queryset=Post.objects.filter(user__username=request.user.username))
		if formset.is_valid():
			#formset.save(commit=False)
			for form in formset:
				print(form.cleaned_data)
				obj = form.save(commit=False)
				if form.cleaned_data.get('title'):
					obj.title = "This title %s" % (obj.id)
					if not form.cleaned_data.get("publish"):
						obj.publish = timezone.now()
					obj.save()
				# print(form.cleaned_data)
			# return redirect("/")
		context = {
			"formset" : formset,
		}
		return render(request, "formset_view.html", context)
	else:
		raise Http404


# def formset_view(request):
# 	TestFormset = formset_factory(TestForm, extra=2)
# 	formset = TestFormset(request.POST or None)
# 	if formset.is_valid():
# 		for form in formset:
# 			print(form.cleaned_data)
# 	context = {
# 		"formset" : formset,
# 	}
# 	return render(request, "formset_view.html", context)





def home(request):
	form = PostModelForm(request.POST or None)
	if form.is_valid():
		obj = form.save(commit=False)
		print(obj.title)
		obj.title = "Some random title"
		obj.publish = timezone.now()
		obj.save()
	if form.has_error:
		print(form.errors.as_json())
		print(form.errors.as_text())
		data = form.errors.items()
		for key,value in data:
			# print(dir(value))
			# print(key, value)
			error_str = "{field}: {error}".format(
				field=key, 
				error=value.as_text()
				)
			#print(error_str)
		# print(dir(form.errors))
		# print(form.non_field_errors)

	# initial_dict = {
	# 	# "some_text" : "Text",
	# 	"boolean" : True,
	# 	# "integer" : "123",
	# 	# "integer" : 123, # same as above
	# }
	# form = TestForm(request.POST or None, initial=initial_dict)
	# if form.is_valid():
	# 	print(form.cleaned_data)
	# 	print(form.cleaned_data.get("some_text"))
	# 	print(form.cleaned_data.get("email"))
	# 	print(form.cleaned_data.get("email2"))

	# if request.method == "POST":
	# 	# form = TestForm(request.POST) # AttributeError: 'QueryDict' object has no attribute 'username' , 不写 data 则把 request.POST 当作user了，因为没有 request.POST.username 所以报错
	# 	form = TestForm(data=request.POST)
	# 	if form.is_valid():
	# 		print(form.cleaned_data)
	# 		print(form.cleaned_data.get("some_text"))
	# 	# print(request.POST)
	# 	# print(request.POST.get("username")) # None
	#  	# print(request.POST["username2"]) # Raise error
	# elif request.method == "GET":
	# 	form = TestForm(user=request.user)
	# 	print(request.GET)
	return render(request, "djforms.html", {"form": form})

	
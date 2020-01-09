from django import forms

class ArticleForm(forms.Form):
     title = forms.CharField()
     pub_date = forms.DateField()

# from django.forms import formset_factory
# ArticleFormSet = formset_factory(ArticleForm)
# formset = ArticleFormSet()
# for form in formset:
#     print(form.as_table())


from django.forms import BaseFormSet
from django.forms import formset_factory
from myformset.forms import ArticleForm

class BaseArticleFormSet(BaseFormSet):
    def clean(self):
        """Checks that no two articles have the same title."""
        if any(self.errors):
            # Don't bother validating the formset unless each form is valid on its own
            return
        titles = []
        for form in self.forms:
            title = form.cleaned_data['title']
            if title in titles:
                raise forms.ValidationError("Articles in a set must have distinct titles.")
            titles.append(title)

    def add_fields(self, form, index):
        super(BaseArticleFormSet, self).add_fields(form, index)
        form.fields["my_field"] = forms.CharField()

    def get_form_kwargs(self, index):
        kwargs = super(BaseArticleFormSet, self).get_form_kwargs(index)
        kwargs['custom_kwarg'] = index
        return kwargs

class MyArticleForm(ArticleForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(MyArticleForm, self).__init__(*args, **kwargs)
        # >>> ArticleFormSet = formset_factory(MyArticleForm)
        # >>> formset = ArticleFormSet(form_kwargs={'user': request.user})
import datetime

from django.forms import formset_factory
from django.test import TestCase
from myformset.forms import ArticleForm
from myformset.forms import BaseArticleFormSet


class ArticleFormsTests(TestCase):
        
    # python manage.py test myformset.tests.ArticleFormsTests.test_was_true_with_forms
    def test_was_true_with_forms(self):
        ArticleFormSet = formset_factory(ArticleForm)
        data = {
            'form-TOTAL_FORMS': '1',
            'form-INITIAL_FORMS': '0',
            'form-MAX_NUM_FORMS': '',
        }
        formset = ArticleFormSet(data)
        formvalid = formset.is_valid()
        self.assertIs(formvalid, True)

    def test_from_with_blank_field(self):
        ArticleFormSet = formset_factory(ArticleForm)
        data = {
            'form-TOTAL_FORMS': '2',
            'form-INITIAL_FORMS': '0',
            'form-MAX_NUM_FORMS': '',
            'form-0-title': 'Test',
            'form-0-pub_date': '1904-06-16',
            'form-1-title': 'Test',
            'form-1-pub_date': '', # <-- this date is missing but required
        }
        formset = ArticleFormSet(data)
        formvalid = formset.is_valid()
        message = formset.errors
        print("------\nlen error is %i,\nformset.total_error_count is %i .\n------" % (len(formset.errors),formset.total_error_count()))
        self.assertIs(formvalid, True, msg = message)
        

    def test_from_with_custome_vaildation(self):
        from myformset.forms import BaseArticleFormSet
        ArticleFormSet = formset_factory(ArticleForm, formset=BaseArticleFormSet)
        data = {
            'form-TOTAL_FORMS': '2',
            'form-INITIAL_FORMS': '0',
            'form-MAX_NUM_FORMS': '',
            'form-0-title': 'Test',
            'form-0-pub_date': '1904-06-16',
            'form-1-title': 'Test',
            'form-1-pub_date': '1912-06-23',
        }
        formset = ArticleFormSet(data)
        formvalid = formset.is_valid()
        message = formset.errors + formset.non_form_errors()
        self.assertIs(formvalid, True, msg = message)
    
    def test_validating_max(self):
        '''validate_max=True validates against max_num strictly even if max_num 
        was exceeded because the amount of initial data supplied was excessive.
        validate_max=True validates 将会对max_num 严格限制，即使提供的初始数据超过 max_num 而导致其无效'''
        from django.forms import formset_factory
        from myformset.forms import ArticleForm
        ArticleFormSet = formset_factory(ArticleForm, max_num=1, validate_max=True)
        data = {
            'form-TOTAL_FORMS': '2',
            'form-INITIAL_FORMS': '0',
            'form-MIN_NUM_FORMS': '',
            'form-MAX_NUM_FORMS': '',
            'form-0-title': 'Test',
            'form-0-pub_date': '1904-06-16',
            'form-1-title': 'Test 2',
            'form-1-pub_date': '1912-06-23',
        }
        formset = ArticleFormSet(data)
        b = formset.is_valid()
        message = formset.errors + formset.non_form_errors()
        self.assertIs(b,True, msg = message)

    def test_validating_min(self):
        from django.forms import formset_factory
        from myformset.forms import ArticleForm
        ArticleFormSet = formset_factory(ArticleForm, min_num=3, validate_min=True)
        data = {
            'form-TOTAL_FORMS': '2',
            'form-INITIAL_FORMS': '0',
            'form-MIN_NUM_FORMS': '',
            'form-MAX_NUM_FORMS': '',
            'form-0-title': 'Test',
            'form-0-pub_date': '1904-06-16',
            'form-1-title': 'Test 2',
            'form-1-pub_date': '1912-06-23',
        }
        formset = ArticleFormSet(data)
        self.assertIs(formset.is_valid(),True, msg = formset.errors + formset.non_form_errors())
    
    # python manage.py test myformset.tests.ArticleFormsTests.test_can_order
    def test_can_order(self):
        from django.forms import formset_factory
        from myformset.forms import ArticleForm
        import datetime
        ArticleFormSet = formset_factory(ArticleForm, can_order=True)
        formset = ArticleFormSet(initial=[
            {'title': 'Article #1', 'pub_date': datetime.date(2008, 5, 10)},
            {'title': 'Article #2', 'pub_date': datetime.date(2008, 5, 11)},
        ])
        for form in formset:
            print(form.as_table())

    def test_can_order2(self):
        ArticleFormSet = formset_factory(ArticleForm, can_order=True)
        data = {
            'form-TOTAL_FORMS': '3',
            'form-INITIAL_FORMS': '2',
            'form-MAX_NUM_FORMS': '',
            'form-0-title': 'Article #1',
            'form-0-pub_date': '2008-05-10',
            'form-0-ORDER': '2',
            'form-1-title': 'Article #2',
            'form-1-pub_date': '2008-05-11',
            'form-1-ORDER': '1',
            'form-2-title': 'Article #3',
            'form-2-pub_date': '2008-05-01',
            'form-2-ORDER': '0',
        }

        formset = ArticleFormSet(data, initial=[
            {'title': 'Article #1', 'pub_date': datetime.date(2008, 5, 10)},
            {'title': 'Article #2', 'pub_date': datetime.date(2008, 5, 11)},
        ])
        formset.is_valid()
        
        for form in formset.ordered_forms:
            print(form.cleaned_data)

    def test_can_delete(self):
        ArticleFormSet = formset_factory(ArticleForm, can_delete=True)
        formset = ArticleFormSet(initial=[
            {'title': 'Article #1', 'pub_date': datetime.date(2008, 5, 10)},
            {'title': 'Article #2', 'pub_date': datetime.date(2008, 5, 11)},
        ])
        for form in formset:
            print(form.as_table())

    def test_can_delete2(self):
        ArticleFormSet = formset_factory(ArticleForm, can_delete=True)
        data = {
            'form-TOTAL_FORMS': '3',
            'form-INITIAL_FORMS': '2',
            'form-MAX_NUM_FORMS': '',
            'form-0-title': 'Article #1',
            'form-0-pub_date': '2008-05-10',
            'form-0-DELETE': 'on',
            'form-1-title': 'Article #2',
            'form-1-pub_date': '2008-05-11',
            'form-1-DELETE': '',
            'form-2-title': '',
            'form-2-pub_date': '',
            'form-2-DELETE': '',
        }

        formset = ArticleFormSet(data, initial=[
            {'title': 'Article #1', 'pub_date': datetime.date(2008, 5, 10)},
            {'title': 'Article #2', 'pub_date': datetime.date(2008, 5, 11)},
        ])
        print([form.cleaned_data for form in formset.deleted_forms])
        '''If you call formset.save(commit=False), objects will not be deleted automatically.
        You’ll need to call delete() 
        on each of the formset.deleted_objects to actually delete them:

        >>> instances = formset.save(commit=False)
        >>> for obj in formset.deleted_objects:
        ...     obj.delete()
        '''

    def test_add_fields(self):
        ArticleFormSet = formset_factory(ArticleForm, formset=BaseArticleFormSet)
        formset = ArticleFormSet()
        for form in formset:
            print(form.as_table())
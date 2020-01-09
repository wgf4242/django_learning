from django.utils import timezone
from django.test import TestCase

# python manage.py test polls
from django.db.models import *
from app_querysetapi.models import *


class MethodTests(TestCase):

    def test_was_published_recently_with_future_question(self):
    	pass
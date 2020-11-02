# 独立使用 django 的 model
import sys
import os


pwd = os.path.dirname(os.path.relpath(__file__))
sys.path.append(pwd + "../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ups.settings")

import django

django.setup()

from sen.models import Jfxx
Jfxx.objects.all()

# 独立使用 django 的 model
import sys
import os

pwd = os.path.dirname(os.path.relpath(__file__))
sys.path.append(pwd + "../")

from pathlib import Path

module_name = ''
for filename in Path('../').rglob('settings.py'):
    if 'venv' in str(filename): continue
    module_name = filename.resolve().parent.name
    print(module_name)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", module_name + ".settings")  # edit this

import django

django.setup()

import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from serializer_api.serializers import ArticleSerializer

data = {
    "title": "a" * 30,
    "description": "b",
    "body": "d",
    "location": "e",
    "publication_date": "2019-01-01",
    "active": True,
    "created_at": None,
    "updated_at": None,
    "author": 1
}
serializer = ArticleSerializer(data=data)
serializer.is_valid()
print(serializer.validated_data)
serializer.save()
json = JSONRenderer().render(serializer.data)

stream = io.BytesIO(json)
data = JSONParser().parse(stream)
print(data)

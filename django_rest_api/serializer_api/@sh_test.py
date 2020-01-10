# 独立使用 django 的 model
import sys
import os

pwd = os.path.dirname(os.path.relpath(__file__))
sys.path.append(pwd + "../")

from pathlib import Path
from pathlib.Path import rglob

# TODO not done
module_name = ''
# for filename in Path('../').rglob('settings.py'):
#     if filename == 'settings.py':
#         module_name = filename.parent.name
#         print(filename)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", module_name + ".settings") # edit this

import django

django.setup()


import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from serializer_api.serializers import ArticleSerializer

data = {}
serializer = ArticleSerializer(data=data)
serializer.is_valid()
print(serializer.validated_data)
serializer.save()
json = JSONRenderer().render(serializer.data)

stream = io.BytesIO(json)
data = JSONParser().parse(stream)
print(data)

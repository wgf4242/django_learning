from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer


class FileView(APIView):
    parser_classes = (FileUploadParser,)

    def post(self, request, *args, **kwargs):

        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileUploadView(APIView):
    parser_classes = (FileUploadParser,)

    def put(self, request, filename=None, format=None):
        file_obj = request.FILES['file']
        # do some stuff with uploaded file
        return Response(status=204)


class FileUploadDefaultView(APIView):

    def post(self, request, filename=None, format=None):
        file_obj = request.FILES['file']
        # do some stuff with uploaded file
        return Response(status=204)


class ExampleView(APIView):
    """
    A view that can accept POST requests with JSON content.
    """
    parser_classes = (MultiPartParser,)

    def post(self, request, format=None):
        # to access files
        print(request.FILES)
        # to access data
        print(request.data)
        return Response({'received data': request.data})


class ExampleExcelView(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request, format=None):
        # to access files
        # print(request.FILES)
        file_obj = request.FILES
        file = file_obj.get('file')
        if file:
            pass

        import pandas as pd
        s = pd.read_excel(file)
        # to access data
        # print(request.data)
        return Response({'received data': request.data})

# class FileView(APIView):
#     parser_classes = (FileUploadParser)
#
#     def post(self, request, *args, **kwargs):
#         file_serializer = FileSerializer(data=request.data)
#         if file_serializer.is_valid():
#             file_serializer.save()
#             return Response(file_serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

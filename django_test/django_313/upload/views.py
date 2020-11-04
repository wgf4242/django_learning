from django.shortcuts import render


# Create your views here.
def upload0(request):
    params = {'app': 'My app',
              'user': request.user,
              'ip_address': request.META['REMOTE_ADDR'],
              }
    image = request.FILES.get('image')
    content = image.read()
    return render(request, 'upload.html', params)

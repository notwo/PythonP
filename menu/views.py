from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def download(req):
    return render(req, 'download.html', {})

def download_by_ver(req):
    response = HttpResponse(open('dist/main.exe', 'rb').read(), content_type='application/x-exe')
    response['Content-Disposition'] = 'filename="ver01.exe"'
    return response


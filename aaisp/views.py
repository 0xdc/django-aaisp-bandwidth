from django.http import HttpResponse
from .models import Line

def update_lines(self, request=None):
    for line in Line.objects.all():
        line.save_new()
    return HttpResponse("OK")

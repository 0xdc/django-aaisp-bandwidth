from django.http import HttpResponse
from djangae.deferred import defer
from .models import Line

def _update_line(line_pk):
    line = Line.objects.get(pk=line_pk)
    line.save_new()

def update_lines(self, request=None):
    for line in Line.objects.all():
        defer(_update_line, line.pk)
    return HttpResponse("OK")

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Line

@login_required
def update_lines(self, request=None):
    for line in Line.objects.all():
        line.save_new()
    return HttpResponse("OK")

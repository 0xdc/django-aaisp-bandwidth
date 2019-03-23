try:
    from django.urls import path
except ImportError:
    from django.conf.urls import url as path

from . import views

app_name = "aaisp"
urlpatterns = [
    path(r'update_lines/?', views.update_lines, name="update_lines"),
]

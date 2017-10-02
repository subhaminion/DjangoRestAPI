from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

from todo.views import TodoView
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='todo/index.html')),
    url(r'^todo/api/', TodoView.as_view()),
]
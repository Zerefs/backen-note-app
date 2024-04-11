from django.urls import path,include
from Api import view
from rest_framework.urlpatterns import format_suffix_patterns
from .view import NoteViewApi

app_name = "Api"

urlpatterns = [
    path("Api/data", NoteViewApi.as_view()),
    path("Api/data/<int:id>", NoteViewApi.as_view()),
]

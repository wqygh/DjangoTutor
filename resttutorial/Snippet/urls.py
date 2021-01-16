from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Snippet import views

urlpatterns = [
    path('Snippet/', views.SnippetList.as_view()),
    path('Snippet/<int:pk>/', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
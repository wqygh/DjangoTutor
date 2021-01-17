from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Snippet import views

urlpatterns = [
    path('Snippet/', views.SnippetList.as_view(), name='snippet-list'),
    path('Snippet/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
    path('Snippet/<int:pk>/highlight/', 
         views.SnippetHighlight.as_view(), name='snippet-highlight'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user-detail'),
    path('', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)
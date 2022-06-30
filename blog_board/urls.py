from django.template.defaulttags import url
from django.urls import path

import blog_board.views

app_name='blog_board'

urlpatterns = [
    path('list/', blog_board.views.board_list, name="board_list"),
    path('<int:pk>/', blog_board.views.board_topics, name="board_topic"),
]
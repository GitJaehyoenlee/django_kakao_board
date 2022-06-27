from django.urls import path

import blog_board.views

app_name='blog_board'

urlpatterns = [
    path('list/', blog_board.views.board_list, name="board_list"),
]
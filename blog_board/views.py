from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from blog_board.models import Board


# @login_required()
def board_list(request):
    boards = Board.objects.all()
    return render(request, 'blog_board/home.html', {'boards': boards})

def board_topics(request, pk):
    board = Board.objects.get(pk=pk)
    return render(request, 'blog_board/topics.html', {'board': board})
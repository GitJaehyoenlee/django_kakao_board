from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
@login_required()
def board_list(request):
    return render(request, 'blog_board/post_list.html', {})
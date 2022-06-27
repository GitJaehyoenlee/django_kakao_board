from django.shortcuts import render

# Create your views here.
def board_list(request):
    return render(request, 'blog_board/post_list.html', {})
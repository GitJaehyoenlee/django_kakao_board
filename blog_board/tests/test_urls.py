from django.test import TestCase
from django.urls import reverse, resolve

from blog_board.views import board_list


class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('blog_board:board_list')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, board_list)
from django.test import Client
from django.test import TestCase

from apps.education.views import IndexView


class Test(TestCase):
    def setUp(self) -> None:
        self.cli = Client()

    def test_get(self):
        resp = self.cli.get("/education/")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.templates), 2)
        self.assertEqual(
            [_t.name for _t in resp.templates], ["education/all_posts.html", "base.html"]
        )
        self.assertEqual(
            resp.resolver_match.func.__name__, IndexView.as_view().__name__
        )
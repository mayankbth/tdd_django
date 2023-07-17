from django.test import TestCase
from model_bakery import baker
from posts.models import Post
from http import HTTPStatus


class HomePageTestCase(TestCase):
    def setUp(self) -> None:
        # post1 = Post.objects.create(
        #     title="sample post 1",
        #     body="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor.",
        # )

        # post2 = Post.objects.create(
        #     title="sample post 2",
        #     body="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor.",
        # )
        self.post1 = baker.make(Post)
        self.post2 = baker.make(Post)

    def test_homepage_returns_correct_response(self):
        response = self.client.get("/")

        self.assertTemplateUsed(response, "posts/index.html")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_homepage_returns_post_list(self):
        response = self.client.get("/")

        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post2.title)
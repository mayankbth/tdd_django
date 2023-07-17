from django.test import TestCase
from model_bakery import baker
from posts.models import Post
from http import HTTPStatus


class DetailPageTest(TestCase):
    def setUp(self) -> None:
        # self.post = Post.objects.create(
        #     title="Learn Javascript in this 23 hour course",
        #     body="This is a beginner course on JS"
        # )
        self.post = baker.make(Post)

    def test_detail_page_return_correct_response(self):
        response = self.client.get(self.post.get_absolute_url())

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "posts/detail.html")

    def test_detail_page_returns_correct_content(self):        
        response = self.client.get(self.post.get_absolute_url())
        
        self.assertContains(response, self.post.title)
        self.assertContains(response, self.post.body)

        # import json
        # content_json = json.dumps(response.content.decode())
        # content_dict = json.loads(content_json)
        # pdb.set_trace()
        # self.assertContains(response, self.post.created_at)
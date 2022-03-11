from rest_framework import status
from rest_framework.test import APITestCase
from apps.parse.api import views as apiviews
from django.urls import reverse

from apps.parse.models import Manga


class TestView(APITestCase):
    def SetUp(self):
        self.sample_manga = Manga.objects.create(
            pk=1,
            source_url="https://cdn.com/some_source_url/",
            title="some_manga",
            alt_title="some_manga_in_japanese",
            rating=9.32,
            thumbnail="https://cdn.com/some_image_compressed/",
            image="https://cdn.com/some_image_full/",
            description="another isekai",
            genres="comedy",
            categories="steampunk",
            status="",
            year="2000",
            updated_detail="2021-07-01T18:07:16.272237Z",
        )

    def test_manga_exists(self):

        resp = self.client.get(reverse("manga-detail", kwargs={"pk": 1}))

        self.assertEqual(resp.status_code, 400)

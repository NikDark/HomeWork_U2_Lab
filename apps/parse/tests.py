from turtle import title
from rest_framework import status
from rest_framework.test import APITestCase
from apps.parse.api import views
from django.urls import reverse
from rest_framework.decorators import action

from apps.parse.models import Manga
from apps.parse.models import Chapter


class MangaTest(APITestCase):
    def setUp(self) -> None:

        self.first_manga = Manga.objects.create(
            title="Стальной алхимик",
            rating=9.32,
            source_url="https://readmanga.io/stalnoi_alhimik__A5327",
            image="https://staticrm.rmr.rocks/uploads/pics/01/41/774.jpg",
        )
        self.first_manga.save()
        manga_obj = Manga.objects.get(pk=1)

        self.first_chapter = Chapter.objects.create(
            manga=manga_obj,
            title="Бросившие вызов солнцу",
            link="https://readmanga.io/stalnoi_alhimik__A5327_ch_1",
            number=1,
            volume=1,
        )
        self.first_chapter.save()
        return super().setUp()

    def test_manga_fetch(self):
        url = reverse("manga-list")
        data = {"title": self.first_manga.title}
        r = self.client.get(url, data)
        r_body = r.json()

        self.assertEqual(r.status_code, 200)
        self.assertIsInstance(r_body["results"], list)
        self.assertEqual(r_body["results"][0]["title"], self.first_manga.title)

    def test_manga_id(self):
        url = reverse("manga-detail", kwargs={"pk": self.first_manga.pk})

        r = self.client.get(url)
        r = self.client.get(url)
        r_body = r.json()
        # print(r_body)

        self.assertEqual(r.status_code, 200)
        self.assertEqual(r_body["id"], self.first_manga.id)

    def test_get_chapter_id(self):

        url = reverse("manga-chapters-list", kwargs={"pk": self.first_manga.pk})
        r = self.client.get(url)

        print(r.json())
        r_body = r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r_body[0]["id"], self.first_manga.id)
        self.assertEqual(r_body[0]["title"], self.first_chapter.title)

    def test_get_image_by_chapterid(self):
        pass

"""
Tests module contains the tests for the Django project
"""
from django.test import TestCase

# Create your tests here.
from story.models import Story


class StoryModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        print("Set up test data")
        Story.objects.create(artist='Bob', title='My Burger', genre='Food', text='They are tasty')

    def test_artist_label(self):
        story = Story.objects.get(id=1)
        field_label = story._meta.get_field('artist').verbose_name
        self.assertEquals(field_label, 'artist')

    def test_title_label(self):
        story = Story.objects.get(id=1)
        field_label = story._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_genre_label(self):
        story = Story.objects.get(id=1)
        field_label = story._meta.get_field('genre').verbose_name
        self.assertEquals(field_label, 'genre')

    def test_text_label(self):
        story = Story.objects.get(id=1)
        field_label = story._meta.get_field('text').verbose_name
        self.assertEquals(field_label, 'text')

    def test_genre_length(self):
        story = Story.objects.get(id=1)
        max_length = story._meta.get_field('genre').max_length
        self.assertEquals(max_length, 100)

    def test_artist_length(self):
        story = Story.objects.get(id=1)
        max_length = story._meta.get_field('artist').max_length
        self.assertEquals(max_length, 250)

    def test_title_length(self):
        story = Story.objects.get(id=1)
        max_length = story._meta.get_field('title').max_length
        self.assertEquals(max_length, 500)

    def test_text_length(self):
        story = Story.objects.get(id=1)
        max_length = story._meta.get_field('text').max_length
        self.assertEquals(max_length, 10000)

    def test_story_string(self):
        story = Story.objects.get(id=1)
        string_rep = 'My Burger'
        self.assertEquals(string_rep, str(story))

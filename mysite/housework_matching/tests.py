import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Housework


def create_housework(housework_text):
    """
    Create a housework with the given `housework_text`.
    """
    return Housework.objects.create(housework_text=housework_text)


class HouseworkIndexViewTests(TestCase):

    def test_no_housework(self):
        """
        If no housework exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('housework_matching:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['object_list'], [])
        self.assertContains(response, "No housework is available.")


class HouseworkDetailViewTest(TestCase):

    def test_past_housework(self):
        """
        The detail view of a housework with a pub_date in the past displays the housework's text. 
        """
        past_housework = create_housework('past housework')
        url = reverse('housework_matching:detail', args=(past_housework.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, past_housework.housework_text)


class HouseworkModelTests(TestCase):

    def test_is_accepted_should_be_false_by_default(self):
        housework = create_housework('sample housework')
        self.assertFalse(housework.is_accepted)

    def test_is_done_should_be_false_by_default(self):
        housework = create_housework('sample housework')
        self.assertFalse(housework.is_done)

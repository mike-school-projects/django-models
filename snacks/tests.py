from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Snack

class SnackTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester",
            email='tester@gmail.com',
            password='pass'
        )
        self.snack = Snack.objects.create(
            name='KitKat',
            description='KitKat Description',
            purchaser=self.user,
        )

    def test_string_representation(self):
        self.assertEqual(str(self.snack), 'KitKat')

    def test_snack_name(self):
        self.assertEqual(f'{self.snack.name}', 'KitKat')

    def test_list_page_status_code(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "snack_list.html")
        self.assertTemplateUsed(response, "base.html")

    def test_404(self):
        response = self.client.get('/badURL')
        self.assertEqual(response.status_code,404)
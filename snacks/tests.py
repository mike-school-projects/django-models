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

    def test_404(self):
        pass
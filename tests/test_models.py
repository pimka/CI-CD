from django.test import TestCase
from users.models import UserModel


class UserModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        UserModel.objects.create(username='test_user')

    def test_username_label(self):
        user = UserModel.objects.get(id=1)
        field_label = user._meta.get_field('username').verbose_name
        self.assertEquals(field_label, 'username')

    def test_username_max_length(self):
        user = UserModel.objects.get(id=1)
        max_length = user._meta.get_field('username').max_length
        self.assertEquals(max_length, 50)
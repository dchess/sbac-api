from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from api.views import TypeViewSet, EntityViewSet
from api.models import Type, Entity


class TypeViewSetTest(TestCase):
    fixtures = ['testing']

    def setUp(self):
        self.client = APIClient()
        self.types = Type.objects.all()
        self.type = self.types.first()
        self.user = User.objects.get(username='some_user')

    def test_get_returns_all(self):
        response = self.client.get('/api/types/')
        self.assertEqual(response.status_code, 200)
        results = response.json()['results']
        self.assertEqual(len(results), self.types.count())

    def test_get_returns_specified_type(self):
        response = self.client.get('/api/types/{}/'.format(self.type.id))
        self.assertEqual(response.status_code, 200)
        results = response.json()
        self.assertEqual(results['description'], self.type.description)

    def test_unauthorized_cannot_post(self):
        original_count = self.types.count()
        response = self.client.post(
            '/api/types/',
            {'type_id': 6, 'description': 'District'}
        )
        self.assertEqual(response.status_code, 401)
        new_count = Type.objects.all().count()
        self.assertEqual(original_count, new_count)

    def test_authorized_can_post(self):
        self.client.force_authenticate(user=self.user)
        original_count = self.types.count()
        response = self.client.post(
            '/api/types/',
            {'type_id': 6, 'description': 'District'}
        )
        self.assertEqual(response.status_code, 201)
        new_count = Type.objects.all().count()
        self.assertEqual(original_count + 1, new_count)

    def test_unauthorized_cannot_update(self):
        original_description = self.type.description
        response = self.client.put(
            '/api/types/{}/'.format(self.type.id),
            {'type_id': self.type.type_id, 'description': 'New Description'}
        )
        self.assertEqual(response.status_code, 401)
        new_description = Type.objects.all().first().description
        self.assertEqual(original_description, new_description)

    def test_authorized_can_update(self):
        self.client.force_authenticate(user=self.user)
        original_description = self.type.description
        response = self.client.put(
            '/api/types/{}/'.format(self.type.id),
            {'type_id': self.type.type_id, 'description': 'New Description'}
        )
        self.assertEqual(response.status_code, 200)
        new_description = Type.objects.all().first().description
        self.assertNotEqual(original_description, new_description)


    def test_unauthorized_cannot_delete(self):
        original_count = self.types.count()
        response = self.client.delete('/api/types/{}/'.format(self.type.id))
        self.assertEqual(response.status_code, 401)
        new_count = Type.objects.all().count()
        self.assertEqual(original_count, new_count)

    def test_authorized_can_delete(self):
        self.client.force_authenticate(user=self.user)
        original_count = self.types.count()
        response = self.client.delete('/api/types/{}/'.format(self.type.id))
        self.assertEqual(response.status_code, 204)
        new_count = Type.objects.all().count()
        self.assertEqual(original_count - 1, new_count)

from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from api.views import TypeViewSet, EntityViewSet, TestViewSet, GradeViewSet
from api.models import Type, Entity, Test, Grade


class TypeViewSetTest(TestCase):
    fixtures = ['testing']

    def setUp(self):
        self.client = APIClient()
        self.types = Type.objects.all()
        self.type = self.types.first()
        self.user = User.objects.get(username='some_user')
        self.new_type = Type.objects.create(
            type_id=99,
            description="Test Type"
        )

    def test_get_returns_all(self):
        response = self.client.get('/api/types/')
        self.assertEqual(response.status_code, 200)
        results = response.json()['results']
        self.assertEqual(len(results), self.types.count())

    def test_get_returns_specified(self):
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
        response = self.client.delete('/api/types/{}/'.format(self.new_type.id))
        self.assertEqual(response.status_code, 204)
        new_count = Type.objects.all().count()
        self.assertEqual(original_count - 1, new_count)


class EntityViewSetTest(TestCase):
    fixtures = ['testing']

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.get(username='some_user')
        self.entities = Entity.objects.all()
        self.entity = self.entities.first()

    def test_get_returns_all(self):
        response = self.client.get('/api/entities/')
        self.assertEqual(response.status_code, 200)
        results = response.json()['results']
        self.assertEqual(len(results), self.entities.count())

    def test_get_returns_specified(self):
        response = self.client.get('/api/entities/{}/'.format(self.entity.id))
        self.assertEqual(response.status_code, 200)
        results = response.json()
        self.assertEqual(results['county_name'], self.entity.county_name)

    def test_unauthorized_cannot_post(self):
        original_count = self.entities.count()
        response = self.client.post(
            '/api/entities/',
            {
                'county_code': '99',
                'district_code': '99999',
                'school_code': '9999999',
                'test_year': 2016,
                'entity_type': 5,
                'county_name': 'Test County'
            }
        )
        self.assertEqual(response.status_code, 401)
        new_count = Entity.objects.all().count()
        self.assertEqual(original_count, new_count)

    def test_authorized_can_post(self):
        self.client.force_authenticate(user=self.user)
        original_count = self.entities.count()
        response = self.client.post(
            '/api/entities/',
            {
                'county_code': '99',
                'district_code': '99999',
                'school_code': '9999999',
                'test_year': 2016,
                'entity_type': 5,
                'county_name': 'Test County'
            }
        )
        self.assertEqual(response.status_code, 201)
        new_count = Entity.objects.all().count()
        self.assertEqual(original_count + 1, new_count)

    def test_unauthorized_cannot_update(self):
        original_county_name = self.entity.county_name
        response = self.client.put(
            '/api/entities/{}/'.format(self.entity.id),
            {
                'county_code': '99',
                'district_code': '99999',
                'school_code': '9999999',
                'test_year': 2016,
                'entity_type': 5,
                'county_name': 'New Test County'
            }
        )
        self.assertEqual(response.status_code, 401)
        new_county_name = Entity.objects.all().first().county_name
        self.assertEqual(original_county_name, new_county_name)

    def test_authorized_can_update(self):
        self.client.force_authenticate(user=self.user)
        original_county_name = self.entity.county_name
        response = self.client.put(
            '/api/entities/{}/'.format(self.entity.id),
            {
                'county_code': '99',
                'district_code': '99999',
                'school_code': '9999999',
                'test_year': 2016,
                'entity_type': 5,
                'county_name': 'Test County'
            }
        )
        self.assertEqual(response.status_code, 200)
        new_county_name = Entity.objects.all().first().county_name
        self.assertNotEqual(original_county_name, new_county_name)

    def test_unauthorized_cannot_delete(self):
        original_count = self.entities.count()
        response = self.client.delete('/api/entities/{}/'.format(self.entity.id))
        self.assertEqual(response.status_code, 401)
        new_count = Entity.objects.all().count()
        self.assertEqual(original_count, new_count)

    def test_authorized_can_delete(self):
        self.client.force_authenticate(user=self.user)
        original_count = self.entities.count()
        response = self.client.delete('/api/entities/{}/'.format(self.entity.id))
        self.assertEqual(response.status_code, 204)
        new_count = Entity.objects.all().count()
        self.assertEqual(original_count - 1, new_count)


class TestViewSetTest(TestCase):
    fixtures = ['testing']

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.get(username='some_user')
        self.tests = Test.objects.all()
        self.test = self.tests.first()

    def test_get_returns_all(self):
        response = self.client.get('/api/tests/')
        self.assertEqual(response.status_code, 200)
        results = response.json()['results']
        self.assertEqual(len(results), self.tests.count())

    def test_get_returns_specified(self):
        response = self.client.get('/api/tests/{}/'.format(self.test.id))
        self.assertEqual(response.status_code, 200)
        results = response.json()
        self.assertEqual(results['name'], self.test.name)

    def test_unauthorized_cannot_post(self):
        original_count = self.tests.count()
        response = self.client.post(
            '/api/tests/',
            {'test_id': '99', 'name': 'Fake Test'}
        )
        self.assertEqual(response.status_code, 401)
        new_count = Test.objects.all().count()
        self.assertEqual(original_count, new_count)

    def test_authorized_can_post(self):
        self.client.force_authenticate(user=self.user)
        original_count = self.tests.count()
        response = self.client.post(
            '/api/tests/',
            {'test_id': '99', 'name': 'Fake Test'}
        )
        self.assertEqual(response.status_code, 201)
        new_count = Test.objects.all().count()
        self.assertEqual(original_count + 1, new_count)

    def test_unauthorized_cannot_update(self):
        original_name = self.test.name
        response = self.client.put(
            '/api/tests/{}/'.format(self.test.id),
            {'test_id': self.test.test_id, 'name': 'Fake Test'}
        )
        self.assertEqual(response.status_code, 401)
        new_name = Test.objects.all().first().name
        self.assertEqual(original_name, new_name)

    def test_authorized_can_update(self):
        self.client.force_authenticate(user=self.user)
        original_name = self.test.name
        response = self.client.put(
            '/api/tests/{}/'.format(self.test.id),
            {'test_id': self.test.test_id, 'name': 'Fake Test'}
        )
        self.assertEqual(response.status_code, 200)
        new_name = Test.objects.all().first().name
        self.assertNotEqual(original_name, new_name)

    def test_unauthorized_cannot_delete(self):
        original_count = self.tests.count()
        response = self.client.delete('/api/tests/{}/'.format(self.test.id))
        self.assertEqual(response.status_code, 401)
        new_count = Test.objects.all().count()
        self.assertEqual(original_count, new_count)

    def test_authorized_can_delete(self):
        self.client.force_authenticate(user=self.user)
        original_count = self.tests.count()
        response = self.client.delete('/api/tests/{}/'.format(self.test.id))
        self.assertEqual(response.status_code, 204)
        new_count = Test.objects.all().count()
        self.assertEqual(original_count - 1, new_count)


class GradeViewSetTest(TestCase):
    fixtures = ['testing']

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.get(username='some_user')
        self.grades = Grade.objects.all()
        self.grade = self.grades.first()

    def test_get_returns_all(self):
        response = self.client.get('/api/grades/')
        self.assertEqual(response.status_code, 200)
        results = response.json()['results']
        self.assertEqual(len(results), self.grades.count())

    def test_get_returns_specified(self):
        response = self.client.get('/api/grades/{}/'.format(self.grade.id))
        self.assertEqual(response.status_code, 200)
        results = response.json()
        self.assertEqual(results['description'], self.grade.description)

    def test_unauthorized_cannot_post(self):
        original_count = self.grades.count()
        response = self.client.post(
            '/api/grades/',
            {'num': '99', 'description': 'Fake Grade'}
        )
        self.assertEqual(response.status_code, 401)
        new_count = Grade.objects.all().count()
        self.assertEqual(original_count, new_count)

    def test_authorized_can_post(self):
        self.client.force_authenticate(user=self.user)
        original_count = self.grades.count()
        response = self.client.post(
            '/api/grades/',
            {'num': '99', 'description': 'Fake Grade'}
        )
        self.assertEqual(response.status_code, 201)
        new_count = Grade.objects.all().count()
        self.assertEqual(original_count + 1, new_count)

    def test_unauthorized_cannot_update(self):
        original_description = self.grade.description
        response = self.client.put(
            '/api/grades/{}/'.format(self.grade.id),
            {'num': self.grade.num, 'description': 'Fake Grade'}
        )
        self.assertEqual(response.status_code, 401)
        new_description = Grade.objects.all().first().description
        self.assertEqual(original_description, new_description)

    def test_authorized_can_update(self):
        self.client.force_authenticate(user=self.user)
        original_description = self.grade.description
        response = self.client.put(
            '/api/grades/{}/'.format(self.grade.id),
            {'num': self.grade.num, 'description': 'Fake Grade'}
        )
        self.assertEqual(response.status_code, 200)
        new_description = Grade.objects.all().first().description
        self.assertNotEqual(original_description, new_description)

    def test_unauthorized_cannot_delete(self):
        original_count = self.grades.count()
        response = self.client.delete('/api/grades/{}/'.format(self.grade.id))
        self.assertEqual(response.status_code, 401)
        new_count = Grade.objects.all().count()
        self.assertEqual(original_count, new_count)

    def test_authorized_can_delete(self):
        self.client.force_authenticate(user=self.user)
        original_count = self.grades.count()
        response = self.client.delete('/api/grades/{}/'.format(self.grade.id))
        self.assertEqual(response.status_code, 204)
        new_count = Grade.objects.all().count()
        self.assertEqual(original_count - 1, new_count)

from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from api.models import Entity, Type, Test, Grade, SubGroup


class EntityModelTest(TestCase):

    def setUp(self):
        self.type = Type.objects.create(type_id=4, description='State')
        self.entity = Entity.objects.create(
            county_code = '00',
            district_code = '00000',
            school_code = '0000000',
            test_year = '2016',
            entity_type = self.type,
            county_name = 'State of California'
        )

    def test_string_representation(self):
        self.assertEqual(
            str(self.entity),
            '00-00000-0000000 State of California'
        )

    def test_verbose_name_plural(self):
        self.assertEqual(str(Entity._meta.verbose_name_plural), 'entities')

    def test_county_code_max_length(self):
        with self.assertRaises(ValidationError):
            self.entity.county_code = '0' * 3
            self.entity.full_clean()

    def test_district_code_max_length(self):
        with self.assertRaises(ValidationError):
            self.entity.district_code = '0' * 6
            self.entity.full_clean()

    def test_school_code_max_length(self):
        with self.assertRaises(ValidationError):
            self.entity.school_code = '0' * 8
            self.entity.full_clean()

    def test_county_name_max_length(self):
        with self.assertRaises(ValidationError):
            self.entity.county_name = 'a' * 201
            self.entity.full_clean()

    def test_district_name_max_length(self):
        with self.assertRaises(ValidationError):
            self.entity.district_name = 'a' * 1001
            self.entity.full_clean()

    def test_school_name_max_length(self):
        with self.assertRaises(ValidationError):
            self.entity.school_name = 'a' * 1001
            self.entity.full_clean()

    def test_zipcode_max_length(self):
        with self.assertRaises(ValidationError):
            self.entity.zipcode = '1' * 13
            self.entity.full_clean()

    def test_district_name_can_be_blank(self):
        self.entity.district_name = ''
        try:
            self.entity.save()
            self.entity.full_clean()
        except Error:
            print('Blank district name should not throw error.')

    def test_school_name_can_be_blank(self):
        self.entity.school_name = ''
        try:
            self.entity.save()
            self.entity.full_clean()
        except Error:
            print('Blank school name should not throw error.')

    def test_zipcode_can_be_blank(self):
        self.entity.zipcode = ''
        try:
            self.entity.save()
            self.entity.full_clean()
        except Error:
            print('Blank zipcode should not throw error.')


class TypeModelTest(TestCase):

    def setUp(self):
        self.entity_type = Type.objects.create(
            type_id=1,
            description='Test Entity Type'
        )

    def test_string_representation(self):
        self.assertEqual(str(self.entity_type), 'Test Entity Type')

    def test_type_id_must_be_unique(self):
        with self.assertRaises(IntegrityError):
            duplicate = Type.objects.create(
                type_id=1,
                description='Duplicate Entity Type'
            )

    def test_description_max_length(self):
        with self.assertRaises(ValidationError):
            self.entity_type.description = 'a' * 31
            self.entity_type.full_clean()


class TestModelTest(TestCase):

    def setUp(self):
        self.test = Test.objects.create(
            test_id=1,
            name='SB - English Language Arts/Literacy'
        )

    def test_string_representation(self):
        self.assertEqual(str(self.test), 'SB - English Language Arts/Literacy')

    def test_test_id_must_be_unique(self):
        with self.assertRaises(IntegrityError):
            duplicate = Test.objects.create(
                test_id=1,
                name='Duplicate ELA Test'
            )

    def test_name_max_length(self):
        with self.assertRaises(ValidationError):
            self.test.name = 'a' * 51
            self.test.full_clean()


class GradeModelTest(TestCase):

    def setUp(self):
        self.grade = Grade.objects.create(
            num = "03",
            description = "3rd Grade"
        )

    def test_string_representation(self):
        self.assertEqual(str(self.grade), '3rd Grade')

    def test_num_max_length(self):
        with self.assertRaises(ValidationError):
            self.grade.num = '0' * 3
            self.grade.full_clean()

    def test_description_max_length(self):
        with self.assertRaises(ValidationError):
            self.grade.description = 'a' * 11
            self.grade.full_clean()


class SubGroupModelTest(TestCase):

    def setUp(self):
        self.subgroup = SubGroup.objects.create(
            subgroup_id = 999,
            description = "Test SubGroup"
        )

    def test_string_representation(self):
        self.assertEqual(str(self.subgroup), 'Test SubGroup')

    def test_subgroup_id_must_be_unique(self):
        with self.assertRaises(IntegrityError):
            duplicate = SubGroup.objects.create(
                subgroup_id=999,
                description="Fake SubGroup"
            )

    def test_description_max_length(self):
        with self.assertRaises(ValidationError):
            self.subgroup.description = 'a' * 101
            self.subgroup.full_clean()

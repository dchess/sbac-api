from django.db import models


class Entity(models.Model):

    county_code = models.CharField(max_length=2)
    district_code = models.CharField(max_length=5)
    school_code = models.CharField(max_length=7)
    test_year = models.IntegerField()
    entity_type = models.ForeignKey('Type', on_delete=models.PROTECT, to_field='type_id')
    county_name = models.CharField(max_length=200)
    district_name = models.CharField(max_length=1000, blank=True)
    school_name = models.CharField(max_length=1000, blank=True)
    zipcode = models.CharField(max_length=12, blank=True)

    def __str__(self):
        if self.school_name:
            name = self.school_name
        elif self.district_name:
            name = self.district_name
        else:
            name = self.county_name
        return "{}-{}-{} {}".format(
            self.county_code,
            self.district_code,
            self.school_code,
            name
        )

    class Meta:
        verbose_name_plural = 'entities'

class Type(models.Model):
    type_id = models.IntegerField(unique=True)
    description = models.CharField(max_length=30)

    def __str__(self):
        return self.description


class Test(models.Model):
    test_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Grade(models.Model):
    num = models.CharField(max_length=2)
    description = models.CharField(max_length=10)

    def __str__(self):
        return self.description

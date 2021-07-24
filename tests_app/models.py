from django.db import models
from django.urls import reverse

class TestType(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Тип испытаний'
        verbose_name_plural = 'Типы испытаний'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tests_app:test_list', kwargs={'pk': self.pk})

class Test(models.Model):
    type_test = models.ForeignKey(TestType, related_name='tests_app', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    base_unit = models.CharField(max_length=50)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Испытание'
        verbose_name_plural = 'Испытания'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tests_app:test_list', kwargs={'pk': self.pk})

from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name



class Cable(models.Model):
    category = models.ForeignKey(Category, related_name='cables', on_delete=models.CASCADE)
    mark = models.CharField(max_length=100, null=True, blank=True)
    elem_group_name = models.CharField(max_length=100, null=True, blank=True)
    elem_group_count = models.IntegerField(default=0)
    count_elem = models.IntegerField(default=0)
    size_elem = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ('mark',)
        verbose_name = 'Кабель'
        verbose_name_plural = 'Кабели'


    def __str__(self):
        return self.mark
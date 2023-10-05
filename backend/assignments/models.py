from django.db import models


class Assignment(models.Model):
    first_term = models.DecimalField(
        max_digits=5, decimal_places=2, null=False, blank=False
    )
    second_term = models.DecimalField(
        max_digits=5, decimal_places=2, null=False, blank=False
    )
    sum = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

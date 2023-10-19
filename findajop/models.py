from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

JOP_TYPE = [
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
    ('Remote','Remote'),
    ('Freelance','Freelance'),
]


class Jop(models.Model):
    user = models.ForeignKey(User, related_name='job_author',on_delete=models.SET_NULL, null=True )
    jop_title = models.CharField(max_length=50)
    image = models.ImageField('photos/%y%m%d')
    company_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    salary = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now())
    jop_nature = models.CharField(max_length=20,choices=JOP_TYPE)

    def __str__(self):
        return self.jop_title
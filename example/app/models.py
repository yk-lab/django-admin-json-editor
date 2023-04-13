from django.db import models
from django.db.models import JSONField


class JSONModel(models.Model):
    data = JSONField(default={
        'text': 'some text',
        'status': False,
        'html': '<h1>Default</h1>',
    })


class ArrayJSONModel(models.Model):
    roles = JSONField(default=list)


class Tag(models.Model):
    name = models.CharField('name', max_length=10)

from django.db import models
import uuid


class Plate(models.Model):
    uuid = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    plate = models.CharField(max_length=6, unique=True)

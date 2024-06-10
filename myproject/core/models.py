import uuid

from django.db import models


class BaseModel(models.Model):
    """
    Abstract base model with basic fields.
    - ID: UUID (unique)
    - created: Date time when entry was created
    - updated: Date time when entry was last updated
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

from django.db import models
from django.contrib.auth import get_user_model
from safedelete.models import SafeDeleteModel, SOFT_DELETE_CASCADE

User = get_user_model()

# Create your models here.
class BaseModel(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta(object):
        abstract = True  # this is an abstract model

    def is_deleted(self, *args, **kwargs):
        return self.deleted is not None

class UserAlert(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='alert')
    price = models.PositiveIntegerField()
    triggered = models.BooleanField(default=False)

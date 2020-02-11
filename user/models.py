from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import Group, Permission, AbstractUser
import logging
from .utils import *
# Create your models here.

logger = logging.getLogger(__name__)

def image_upload_path(instance, filename):
    return "user{0}/{1}".format(instance.id, filename)

class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey("user.User", null=True, editable=False, related_name="%(app_label)s_%(class)s_created",on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey("user.User", null=True, editable=False, related_name="%(app_label)s_%(class)s_updated",on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and user.is_authenticated:
            self.updated_by = user
            if self._state.adding:
                self.created_by = user
        super(Base, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class Department(Base):
    name = models.CharField(_("Department Name"), max_length=50)

    def __str__(self):
        return self.name



class User(AbstractUser, Base):
    height = models.IntegerField(_("Height"), blank=True, null=True)
    width = models.IntegerField(_("Width"), blank=True, null=True)
    image = models.ImageField(
        _("Image"),
        upload_to=image_upload_path,
        height_field="height",
        width_field="width",
        blank=True,
        null=True,
        max_length=500,
    )

class Profile(Base):
    user = models.OneToOneField(User, verbose_name=_("User"),related_name='uprofile', on_delete=models.CASCADE)
    department = models.ForeignKey(Department, verbose_name=_("Department"), related_name='profiles', on_delete=models.CASCADE)
    session = models.CharField(_("Seesion"), max_length=50)

    def __str__(self):
        return self.user.username
        
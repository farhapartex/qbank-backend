from django.db import models
from django.utils.translation import ugettext as _
from django.conf import settings
# Create your models here.

def image_upload_path(instance, filename):
    return "{0}/{1}".format(instance.course.code, filename)

class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Department(Base):
    name = models.CharField(_("Department Name"), max_length=50)

    def __str__(self):
        return self.name


class Course(Base):
    department = models.ForeignKey(Department, verbose_name=_("Department"), related_name="courses", on_delete=models.CASCADE)
    code = models.CharField(_("Code"), max_length=10)
    name = models.CharField(_("Name"), max_length=100)

    def __str__(self):
        return self.code


SEMESTER_CHOICE = (('1','First'),('2','Second'))
class Question(Base):
    year = models.CharField(_("Year"), max_length=10)
    department = models.ForeignKey(Department, verbose_name=_("Department"),related_name="dquestions", on_delete=models.CASCADE)
    semester = models.CharField(_("Semester"),choices=SEMESTER_CHOICE, default='1', max_length=10)
    course = models.ForeignKey(Course, verbose_name=_("Course"),related_name="cquestions", on_delete=models.CASCADE)
    height = models.IntegerField(_("Height"), blank=True, null=True)
    width = models.IntegerField(_("Width"), blank=True, null=True)
    image = models.ImageField(
        _("Image"),
        upload_to=image_upload_path,
        height_field="height",
        width_field="width",
        max_length=500,
    )


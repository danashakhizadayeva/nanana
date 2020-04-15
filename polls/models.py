from django.db import models
from django.core.validators import int_list_validator
import uuid
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# Create your models here.



class Video(models.Model):
    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular video across whole database')
    name = models.CharField(max_length=500, help_text='The number of the video (e.g. Video1)')
    location = models.CharField(max_length=500, help_text='folder location in the server (e.g. media/1)',default=None)
    MLresults = models.OneToOneField('theBase', on_delete=models.SET_NULL, null=True)
    text = models.CharField(max_length=500, help_text='Which text was demonstrated on video (e.g. "1")')
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    def __str__(self):
         return self.name


class theBase(models.Model):

    name = models.CharField(max_length=500, help_text='The number of the base based on video number (e.g. Base1)')
    results = models.CharField(default=None,blank=True, null=True, max_length=500, help_text='ML check results here (e.g. "6 5 11 1 10")', validators=[int_list_validator(sep=' ')])
    usersprovided = models.TextField(default="", blank=True, null=True, help_text='Users that provided the check results')
    check1 = models.TextField(default=None, blank=True, null=True, validators=[int_list_validator(sep=' ')], help_text='Do not touch, check results here in form "1 0 0 1 1 0 1')
    check2 = models.TextField(default=None, blank=True, null=True, validators=[int_list_validator(sep=' ')], help_text='Do not touch, check results here in form "1 0 0 1 1 0 1')
    check3 = models.TextField(default=None, blank=True, null=True, validators=[int_list_validator(sep=' ')], help_text='Do not touch, check results here in form "1 0 0 1 1 0 1')
    check4 = models.TextField(default=None, blank=True, null=True, validators=[int_list_validator(sep=' ')], help_text='Do not touch, check results here in form "1 0 0 1 1 0 1')
    check5 = models.TextField(default=None, blank=True, null=True, validators=[int_list_validator(sep=' ')], help_text='Do not touch, check results here in form "1 0 0 1 1 0 1')
    check6 = models.TextField(default=None, blank=True, null=True, validators=[int_list_validator(sep=' ')], help_text='Do not touch, check results here in form "1 0 0 1 1 0 1')
    check7 = models.TextField(default=None, blank=True, null=True, validators=[int_list_validator(sep=' ')], help_text='Do not touch, check results here in form "1 0 0 1 1 0 1')
    check8 = models.TextField(default=None, blank=True, null=True, validators=[int_list_validator(sep=' ')], help_text='Do not touch, check results here in form "1 0 0 1 1 0 1')
    check9 = models.TextField(default=None, blank=True, null=True, validators=[int_list_validator(sep=' ')], help_text='Do not touch, check results here in form "1 0 0 1 1 0 1')
    check10 = models.TextField(default=None,blank=True, null=True, validators=[int_list_validator(sep=' ')], help_text='Do not touch, check results here in form "1 0 0 1 1 0 1')
    check11 = models.TextField(default=None,blank=True, null=True, validators=[int_list_validator(sep=' ')], help_text='Do not touch, check results here in form "1 0 0 1 1 0 1')

    def __str__(self):
        return self.name

class numberOfVideos(models.Model):
    name = models.CharField(max_length=500, help_text='number')
    number = models.CharField(max_length=500, help_text='The number of the videos in the Database')

    def save(self, *args, **kwargs):
        if not self.pk and numberOfVideos.objects.exists():
        # if you'll not check for self.pk 
        # then error will also raised in update of exists model
            raise ValidationError('There is can be only one numberOfVideos instance')
        return super(numberOfVideos, self).save(*args, **kwargs)
    def __str__(self):
        return 'number'
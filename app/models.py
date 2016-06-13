# encoding: utf-8
"""
Definition of models.
"""

from django.db import models
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    photo = models.URLField(blank=True)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Document(models.Model):
    docfile = models.FileField(upload_to='uploadfile')



class MRAPP(models.Model):
    name = models.CharField(max_length=20) #APP name
    apptype = models.CharField(max_length=15) #apptype: matlab, python, bash, docker
    cmd = models.CharField(max_length=100)
    shorttext = models.CharField(max_length=100) #APP name
    OS = models.CharField(max_length=30,default='Linux') # Windows, Linux
    info_html1 = models.TextField(blank=True)
    info_html2 = models.TextField(blank=True)
    info_html3 = models.TextField(blank=True)
    basic_option_html = models.TextField(blank=True) #放置基本選項
    adv_option_html = models.TextField(blank=True) #放置額外選項
    enable = models.BooleanField(default=False)


    def __unicode__(self):
        """
        :returns: name string

        """
        return self.name


class file_log(models.Model):
    fname = models.CharField(max_length=50)
    inp_time = models.DateTimeField(auto_now_add=True)
    out_time = models.DateTimeField(blank=True,null = True)
    com_time = models.DecimalField(max_digits=3, decimal_places=0,default=0) #computation time in minutes
    status = models.CharField(max_length=30, blank=True,default='init')
    percent = models.DecimalField(max_digits=3, decimal_places=0,default=0)
    result_url = models.URLField(blank=True)
    MRAPP = models.ForeignKey(MRAPP)
    from django.contrib.auth.models import User
    user = models.ForeignKey(User)
    #user = models.CharField(max_length=20,default='not set')   

    def __unicode__(self):
        """
        :returns: name string

        """
        return self.fname

    class Meta:

        """Meta: attribute, options"""

        ordering = ['inp_time']
        '''permissions = (
            ("can_comment", "Can comment"),
        )'''

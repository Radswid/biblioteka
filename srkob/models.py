# -*- coding: utf-8 -*-
from django.db import models
#from srkob.models import Profile
from django.contrib.auth.models import User
from django import forms

class author(models.Model):
    first_name = models.CharField('Imię', max_length=50)
    last_name = models.CharField('Nazwisko', max_length=50)

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autorzy"

    def __unicode__(self):
        return self.last_name
    
class books(models.Model):
    title = models.CharField('Tytuł', max_length=50)
    slug = models.SlugField('Odnośnik', unique=True, max_length=100)
    author = models.ForeignKey(author)
    about = models.TextField('Opis')
    state = models.BooleanField('Wypożyczona')

    class Meta:
        verbose_name = "Książka"
        verbose_name_plural = "Książki"

    def __unicode__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User)
    address = models.TextField('Adres')
    p_number = models.CharField('Pesel', max_length=11)
    
    class Meta:
        verbose_name = "Profil"
        verbose_name_plural = "Profile"

    def __unicode__(self):
        return self.user.username
    
    

'''
Created on 22 Oct 2013

@author: michael
'''
from django.contrib import admin

from app.newsfeed import models

admin.site.register(models.FeedItem)
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..app_reglogin.models import User
from django.db import models
from datetime import date
from datetime import datetime
import time 
import bcrypt
 
class tripscheduleManager(models.Manager):
    def addtravelplan(request,postData,sessiondata):
        print postData
        print " In addtravelplan %%%%%%%%%%%"
        
        results = {'status': True, 'errors': []}
        if not postData['destination'] or len(postData['destination'])<1:
            print "In destination "
            results['status'] = False
            results['errors'].append("Please enter a destination")

        if not postData['description'] or len(postData['description'])<1:
            print "In description "
            results['status'] = False
            results['errors'].append("Please enter a description")

        if not postData['plan'] or len(postData['plan'])<1:
            print "In plan "
            results['status'] = False
            results['errors'].append("Please enter a plan")
        
        if not postData['startdate'] or len(postData['startdate'])<1:
            print "In startdate "
            results['status'] = False
            results['errors'].append("Please enter a Travel Date From")



        if not postData['returndate'] or len(postData['returndate'])<1:
            print "In returndate "
            results['status'] = False
            results['errors'].append("Please enter a Travel Date To")

        if results['status']:   
            today = datetime.now().date()
            start = datetime.strptime(postData['startdate'], '%Y-%m-%d').date()
            end = datetime.strptime(postData['returndate'], '%Y-%m-%d').date()
       
            if start < today:  
                results['status'] = False
                results['errors'].append('Travel Date From must be in the future.')
            if end < today:
                results['status'] = False
                results['errors'].append('Travel Date To must be in the future.')
            # #validate date to not before date from
            if end < start:
                results['status'] = False
                results['errors'].append('Travel Date To is before Travel Date From')

        if results['status']:
            user1 = User.objects.get(id = sessiondata['userid'])
            Travelplan1 = Tripschedule.objects.create(destination=postData['destination'],
            tripdesc=postData['description'],plan=postData['plan'],
            startdate=postData['startdate'],
            returndate=postData['returndate'],tripuser = user1)
        
          
            results['status'] = True
            print "Successfully done!!!!!!!!!"
       
        return results            

    def addlike(request,context):
        print context
        results = {'status': True, 'errors': []}

        trip1=Tripschedule.objects.get(id=context["tripid"])
        user1=User.objects.get(id=context["userid"])
        if trip1.tripuser == user1:
            print "In validation1 "
            results['status'] = False
            results['errors'].append("You cannot join your own trip!")
        else:
            trip1.joinpeople.add(user1)
            print "join done!!!!!!!!!"
            results['status'] = True
        return results 


class Tripschedule(models.Model):
    destination = models.TextField(max_length=1000)
    tripdesc = models.TextField(max_length=1000)
    plan=models.TextField(max_length=1000)
    startdate = models.DateField()
    returndate = models.DateField()
    tripuser= models.ForeignKey('app_reglogin.User', related_name="tripusers")
    joinpeople = models.ManyToManyField('app_reglogin.User', related_name="joinpeoples")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
     
    objects=tripscheduleManager()
    #bookauthors
    #bookreviews
 
    


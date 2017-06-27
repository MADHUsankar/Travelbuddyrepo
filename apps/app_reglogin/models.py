# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import bcrypt
 
class UserManager(models.Manager):
    def register(self, postData):
        print postData
        results = {'status': True, 'errors': [],'user':None}
        if not postData['name'] or len(postData['name']) <1:
            print "name error"
            results['status'] = False
            results['errors'].append("Please enter name")

        elif len(postData['name']) <3:
            print "name length error"
            results['status'] = False
            results['errors'].append("Name should be atleast three characters long")

         

        if not postData['username'] or len(postData['username']) <1:
            results['status'] = False
            results['errors'].append("Please enter Username")
        
        elif not postData['username'] or len(postData['username']) <3:
            results['status'] = False
            results['errors'].append("UserName should be atleast three characters long")

        if not postData['password'] or len(postData['password']) <8:
            results['status'] = False
            results['errors'].append("Password must be atleast 8 characters long")
        
        elif not postData['confirmpassword'] or len(postData['confirmpassword']) <1:
            results['status'] = False
            results['errors'].append("Please enter password in Confirm PW")
        
        if postData['confirmpassword'] != postData['password']:
            results['status'] = False
            results['errors'].append("Passwords do not match")

        if not results['status']:
            return results
       
        x = User.objects.filter(username = postData['username'])

        try:
            if x[0]:
                results['errors'].append("User already exists")
                results['status'] = False
        except:
            if results['status']:
                password = postData['password'].encode() # to get from unicode to string
                hashed = bcrypt.hashpw(password, bcrypt.gensalt())
                print hashed
                y = User.objects.create(name=postData['name'], username=postData['username'], password=hashed)
                y.save()
                results['user'] = y
        return results

    def loginval(self, postData):
        results = {'status': True, 'errors': [],'user':None}

        print postData
        if not postData['username'] or len(postData['username']) <1:
            results['status'] = False
            results['errors'].append("Please enter Username")
        
        elif not postData['username'] or len(postData['username']) <3:
            results['status'] = False
            results['errors'].append("UserName should be atleast three characters long")

        if not postData['password'] or len(postData['password']) <1:
            results['status'] = False
            results['errors'].append("Please enter Password")

        elif not postData['password'] or len(postData['password']) <8:
            results['status'] = False
            results['errors'].append("Password must be atleast 8 characters long")
        
        if results['status'] == True:
            x = User.objects.filter(username = postData['username'])
        #print x
        
            try:
                if x[0]:
                    print "password testing"
                    password = postData['password'].encode()
                    y = x[0].password.encode()
                    if bcrypt.hashpw(password,y) == y:
                        results['status'] = True
                        print ("*****It matches**********")
                        results['user'] = x[0]
                    else:
                        results['status'] =False
                        results['errors'].append("Invalid credentials")
 
            except:
                results['status'] =False
                print "please regitser"
                results['errors'].append("Please Register")
        return results

        


class User(models.Model):
    name = models.CharField(max_length=38)
    username = models.CharField(max_length=38)
    password = models.CharField(max_length=38)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    #tripusers
"""from django.db import models

class testrun(models.Model):
    movieID = models.IntegerField(primary_key=True)
    #imdbPictureURL = models.CharField(max_length=300, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    genre = models.CharField(max_length=200, null=True, blank=True)
    #AddressSpace1 = models.CharField(max_length=200, null=True, blank=True)
   # AddressSpace2 = models.CharField(max_length=200, null=True, blank=True)
    #directorID = models.CharField(max_length=100, null=True, blank=True)
    directorName = models.CharField(max_length=100, null=True, blank=True)
    

    def __str__(self):
        return self.title
"""
'''
class Movie(models.Model):
    movieID = models.IntegerField(primary_key=True)
    year = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    genre = models.CharField(max_length=200, null=True, blank=True)
    directorName = models.CharField(max_length=100, null=True, blank=True)
    imdbPictureURL = models.CharField(max_length=300, null=True, blank=True)
    rating = models.CharField(max_length=6, null=True, blank=True)
    tag1 = models.CharField(max_length=100, null=True, blank=True)
    tag2 = models.CharField(max_length=100, null=True, blank=True)
    tag3 = models.CharField(max_length=100, null=True, blank=True)
    tag4 = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return self.title
   '''
'''
class Movieproject(models.Model):
    movieID = models.IntegerField(primary_key=True)
    imdbPictureURL = models.CharField(max_length=300,null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=200,null=True, blank=True)
    genre = models.CharField(max_length=200,null=True, blank=True)
    AddressSpace1 = models.CharField(max_length=200,null=True, blank=True)
    AddressSpace2 = models.CharField(max_length=200,null=True, blank=True)
    directorID = models.CharField(max_length=100,null=True, blank=True)
    

    def __str__(self):
        return self.title
    
    def __str__(self):
        return self.genre
    
    def __str__(self):
        return self.AddressSpace1

    def __str__(self):
        return self.AddressSpace2
 '''
    

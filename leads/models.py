from django.db import models

class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

class covid1(models.Model):
	place = models.CharField(max_length = 200,)
	number = models.CharField(max_length = 200,)

class technews(models.Model):
	
	headlines = models.CharField(max_length = 500,primary_key = True)
	description = models.CharField(max_length = 2500,)
	hyperlink = models.URLField(max_length=2000,)
	source = models.CharField(max_length = 2000,)

class worldnews(models.Model):
	
	headlines = models.CharField(max_length = 500,primary_key = True)
	description = models.CharField(max_length = 2500,)
	hyperlink = models.URLField(max_length=2000,)
	source = models.CharField(max_length = 2000,)

class fullmore(models.Model):
	
	headlines = models.CharField(max_length = 500,primary_key = True)
	description = models.CharField(max_length = 2500,)
	hyperlink = models.URLField(max_length=2000,)
	source = models.CharField(max_length = 2000,)

class sportsnews(models.Model):
	
	headlines = models.CharField(max_length = 500,primary_key = True)
	description = models.CharField(max_length = 2500,)
	hyperlink = models.URLField(max_length=2000,)
	source = models.CharField(max_length = 2000,)

class weatherdetails(models.Model):
	
	city = models.CharField(max_length = 500,primary_key = True)
	temperature = models.CharField(max_length = 2500,)
	pressure = models.CharField(max_length=2000,)
	humidity = models.CharField(max_length = 2000,)
	description=models.CharField(max_length=2000,)

class Post(models.Model):
    city = models.CharField(max_length=100)
   
    
    def __str__(self):
        return self.title
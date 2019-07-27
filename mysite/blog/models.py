from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.urls import reverse


class BlogAuthor(models.Model):
    authorName = models.ForeignKey(User, on_delete=models.CASCADE)
    authorBio = models.CharField(max_length=200)

    class Meta:
        ordering = ["authorName"]

    def __str__(self):
        return self.authorName.username
    
    def get_absolute_url(self):
        return reverse('blogger-details', args= [str(self.id)] )

    

class Blog(models.Model):
    blogtitle = models.CharField(max_length=100)
    blogdate = models.DateField(default = date.today)
    blogauthor = models.ForeignKey(BlogAuthor, on_delete = models.SET_NULL, null = True)
    blogtext = models.TextField()

    class Meta:
        ordering = ["blogdate"]

    def __str__(self):
        return self.blogtitle 

    def get_absolute_url(self):
        return reverse('blog-detail', args= [str(self.id)])   
    
            



class BlogComment(models.Model):
    commentDate = models.DateTimeField(auto_now_add=True)    
    commentUser = models.ForeignKey(User, on_delete= models.CASCADE)
    comment = models.CharField(max_length=100)
    blog = models.ForeignKey(Blog, on_delete= models.SET_NULL, null = True)

    class Meta:
        ordering = ["commentDate"]

    def __str__(self):
        return self.comment   

    def get_absolute_url(self):
        return reverse('blog-newcomment', args = [str(self.id)]) 


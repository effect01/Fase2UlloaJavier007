from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=35)

    content = models.TextField(blank=True)
    genre = models.ManyToManyField('GenBook')
    author = models.ForeignKey('Author', on_delete=models.CASCADE  )
    previewContent = models.CharField(blank=True , max_length=120)
    year = models.CharField(max_length=11)
    publisher = models.CharField(max_length=65)
    country = models.CharField(max_length=65)
    image = models.URLField('Image Address')
    postedBy = models.ForeignKey(User , on_delete=models.CASCADE )
    data_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    def pointCount(self):
        return self.star_set.all().count()
    def pointMedia(self):
        star2=0
        for star in self.star_set.all():
            star2= star2+ round(float(star.vote),1)
        if star2 != 0:
            return star2/self.pointCount()
        else:
            return 0
    def pointMediaPercent(self):
        if self.pointMedia() != 0:      
            return round( self.pointMedia()*20)
        else:
            return 0


class Star(models.Model):
    VOTE_POINT = (
            ('1',1),
            ('2',2),
            ('3',3),
            ('4',4),
            ('5',5),
        )
    post = models.ForeignKey('Post' , on_delete=models.CASCADE )
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    vote = models.CharField(max_length=1, choices=VOTE_POINT )
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'post'], name='Solo 1 voto')
        ]
    def __str__(self):
        return self.vote

class Comment(models.Model):
    post = models.ForeignKey('Post' , on_delete=models.CASCADE )
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    comment = models.TextField(blank=True )
    def __str__(self):
        return "%s/%s" % (self.user, self.post)




class GenBook(models.Model):
    nameGen = models.CharField(max_length=65)
    def get_absolute_url(self):
        return reverse('book-gen', args=[str(self.id)])
    def __str__(self):
        return self.nameGen

class Author(models.Model):
    first_name = models.CharField(max_length=65)
    last_name = models.CharField(max_length=65)
    class Meta:
        ordering = ['last_name', 'first_name']
    def __str__(self):
        return "%s/%s" % (self.last_name, self.first_name)


class UserBook(models.Model):
    post = models.ForeignKey('Post' , on_delete=models.CASCADE)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    class Meta:
        constraints = [  models.UniqueConstraint(fields=['user', 'post'], name='1 virtual book')]
    def __str__(self):
        return "User: %s, Book: %s" % (self.user, self.post)
    def et(self):
        return f'self.user.username'
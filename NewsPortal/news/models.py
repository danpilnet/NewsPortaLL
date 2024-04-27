from django.db import models
from django.contrib.auth.models import User
from django.db.models.functions import Coalesce
from django.db.models import Sum


class Author(models.Model):
    user = models.OneToOneField(User,on_delete= models.CASCADE)
    rating = models.IntegerField(default= 0)

    def uptade_rating(self):
        posts_rating = self.post_set.aggregate(pr=Coalesce(Sum('rating'), 0)).get('pr')
        comments_rating = self.user.comment_set.aggregate(cr=Coalesce(Sum('rating_comment'), 0)).get('cr')
        posts_comments_raring = self.post_set.aggregate(pcr=Coalesce(Sum('rating'), 0)).get('pcr')

        self.rating = posts_rating * 3 + comments_rating + posts_comments_raring
        self.save()

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length= 100, unique=True)
    subscribers = models.ManyToManyField(User, related_name='categories', through='Subscribe')


    def __str__(self):
        return self.name


class Post(models.Model):

    article ='AR'
    news = 'NE'

    POSITION = [(article, 'Статья'),
                (news, 'Новости')
                ]

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    pole_ar_ne = models.CharField(max_length=2, choices=POSITION, default=news)
    add_time = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through='PostCategory')
    zagolovok = models.CharField(max_length=200)
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.pole_ar_ne}: {self.text}'




    def like(self):
        self.rating += 1
        self.save()


    def dislike(self):
        self.rating -= 1
        self.save()


    def preview(self):
        return f'{self.text[:124]}...'



class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)



class Comment(models.Model):
    post_comment = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.ForeignKey(User, on_delete=models.CASCADE)
    text_comment = models.TextField()
    time_comment = models.DateTimeField(auto_now_add=True)
    rating_comment = models.IntegerField(default=0)


    def like(self):
        self.rating_comment += 1
        self.save()


    def dislike(self):
        self.rating_comment -= 1
        self.save()



class Subscribe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category_sb = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}{self.category_sb}'
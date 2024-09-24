from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=300)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='liked_tweets', blank=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f'{self.user.username} - {self.text[:10]}'

class Comment(models.Model):
    tweet = models.ForeignKey(Tweet, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.text[:50]}'

class FriendRequest(models.Model):
    from_user = models.ForeignKey(User, related_name='sent_requests', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='received_requests', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.from_user} -> {self.to_user}"

class Friend(models.Model):
    user1 = models.ForeignKey(User, related_name='friends_with', on_delete=models.CASCADE,null=True)
    user2 = models.ForeignKey(User, related_name='friends_with_user', on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f"{self.user1.username} is friends with {self.user2.username}"

    @classmethod
    def make_friend(cls, user1, user2):
        friend, created = cls.objects.get_or_create(user1=user1, user2=user2)

    @classmethod
    def lose_friend(cls, user1, user2):
        cls.objects.filter(user1=user1, user2=user2).delete()

from django.core.management.base import BaseCommand
from tweet_beginner_app.models import Friend

class Command(BaseCommand):
    help = 'Remove duplicate friend relationships'

    def handle(self, *args, **kwargs):
        # Get all current users
        current_users = Friend.objects.values_list('user1', flat=True).distinct()

        for current_user in current_users:
            # Get duplicates for this current_user
            duplicate_friends = Friend.objects.filter(user1=current_user)
            
            # If duplicates exist, keep one and delete the others
            if duplicate_friends.count() > 1:
                # Keep one and delete the others
                keep_friend = duplicate_friends.first()
                duplicate_friends.exclude(id=keep_friend.id).delete()

        self.stdout.write(self.style.SUCCESS('Duplicate friends cleaned up successfully.'))

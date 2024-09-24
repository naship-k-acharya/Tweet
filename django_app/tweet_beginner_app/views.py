from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Tweet, FriendRequest, Friend
from .forms import TweetForm, UserRegistrationForm, CommentForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def friend_request(request):
    friend_ids = Friend.objects.filter(user1=request.user).values_list('user2_id', flat=True)
    
    # Fetch User objects for the friends
    friends = User.objects.filter(id__in=friend_ids)

    # Paginate the friends list (optional, with 5 users per page)
    paginator = Paginator(friends, 5)  # Show 5 friends per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'friends': page_obj,  # Pass paginated friends to template
    }
    return render(request, 'friend_request.html', context)
    
    

@login_required
def tweet_list(request):
    random_users = User.objects.exclude(id=request.user.id).order_by('?')[:5]
    tweets = Tweet.objects.all().order_by('-created_at')
    comment = Tweet.objects.all().prefetch_related('comments')

    # Get friend requests and friends for the authenticated user
    sent_requests = request.user.sent_requests.values_list('to_user', flat=True)

    # Update to filter by user1 and user2 and convert to list
    friends_user1 = list(Friend.objects.filter(user1=request.user).values_list('user2', flat=True))
    friends_user2 = list(Friend.objects.filter(user2=request.user).values_list('user1', flat=True))
    
    # Combine the two lists
    friends = friends_user1 + friends_user2

    context = {
        'random_users': random_users,
        'comment_forms': comment,
        'tweets': tweets,
        'sent_requests': sent_requests,
        'friends': friends,
    }
    return render(request, 'tweet_list.html', context)


@login_required
def tweet_create(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm()
    return render(request, 'tweet_form.html', {'form': form})

@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)
    return render(request, 'tweet_form.html', {'form': form})

@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request, 'tweet_confirm_delete.html', {'tweet': tweet})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('tweet_list')
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})

@login_required
def like_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    if request.user in tweet.likes.all():
        tweet.likes.remove(request.user)  # Unlike the tweet
    else:
        tweet.likes.add(request.user)  # Like the tweet
    return redirect('tweet_list')

@login_required
def comment_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.tweet = tweet
            comment.user = request.user
            comment.save()
            return redirect('tweet_list')
    else:
        form = CommentForm()
    return render(request, 'tweet_list.html', {'tweet': tweet, 'form': form})

def send_friend_request(request, user_id):
    user = get_object_or_404(User, id=user_id)
    
    # Check if the user is trying to send a request to themselves
    if user == request.user:
        messages.error(request, "You cannot send a friend request to yourself.")
        return redirect('tweet_list')  # Redirect to the tweet list or any other page

    # Proceed with friend request if it's not the current user
    friend_request, created = FriendRequest.objects.get_or_create(from_user=request.user, to_user=user)
    
    if created:
        messages.success(request, "Friend request sent successfully.")
    else:
        messages.info(request, "Friend request already sent.")

    return redirect('tweet_list')



@login_required
def accept_friend_request(request, request_id):
    friend_request = get_object_or_404(FriendRequest, id=request_id)
    if friend_request.to_user == request.user:
        # Create or retrieve the Friend instance
        friend1, created = Friend.objects.get_or_create(user1=request.user, user2=friend_request.from_user)

        # Create the reverse relationship
        friend2, created = Friend.objects.get_or_create(user1=friend_request.from_user, user2=request.user)

        friend_request.delete()  # Delete the request after acceptance
        return redirect('tweet_list')
    return redirect('tweet_list')


def delete_friend_request(request, request_id):
    friend_request = get_object_or_404(FriendRequest, id=request_id)
    if friend_request.to_user == request.user:
        friend_request.delete()  # Delete the friend request
        return redirect('friend_request')  # Redirect to the friend requests page
    return redirect('friend_request')

# Social Networking Platform

A Twitter-like social networking platform built using Django. This platform allows users to perform various social interactions such as tweeting, liking, commenting, sharing, and managing friend requests.

## Features

- **User Registration & Authentication**: Secure sign-up, login, and logout functionality.
- **Tweeting**: Users can post text-based tweets visible to others.
- **Liking Tweets**: Users can like/unlike tweets.
- **Commenting**: Users can comment on tweets, and the comments appear under the respective tweets.
- **Sharing Tweets**: Users can share tweets to their profile.
- **Friend Requests**: Users can send and accept friend requests, establishing friendships.
- **Friendship-Based Chat System** (Optional): Chat system available only between friends.

## Installation

### Prerequisites
- Python 3.x
- Django 4.x
- Bootstrap (for frontend styling)

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/naship-k-acharya/Tweet.git
   cd Tweet
   ```
2. **Set up a virtual environment:
    >On mac and linux:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
    >On Windows use:
    `venv\Scripts\activate`
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run migrations:
    ```bash
    python manage.py migrate
    ```
5. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```
6. Start the development server:
    ```bash
    python manage.py runserver
    ```
##



## Features in Detail 
- Tweeting
- Users can create short text-based posts.
- Tweet content is displayed on the homepage and profile pages.
- Liking and Commenting
- Tweets can be liked by users, and a like counter is shown.
- Users can comment on tweets, and comments will be displayed beneath each tweet.
- Friend Requests
- Users can send friend requests to others.
- Once accepted, both users become friends and can view each other's posts.
- The system ensures no duplicate friend relationships.
- Sharing Tweets
- Users can share others' tweets on their profiles.
- Chat (Optional Feature)
- A real-time chat system can be integrated, allowing only friends to send messages to each other.

## Future Enhancements
Implement a notification system for friend requests and likes.
Add real-time WebSockets for instant messaging between friends.
# License
This project is licensed under the MIT License - see the **LICENSE file for details.

You can modify the content depending on your specific project structure or additional features. Let me know if you need further changes!
```python
import tweepy

class SocialMediaIntegration:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(self.auth)

    def share_on_twitter(self, content):
        try:
            self.api.update_status(content)
            print("Successfully shared on Twitter.")
        except Exception as e:
            print(f"An error occurred: {e}")

# Replace with your own Twitter API credentials
consumer_key = "your_consumer_key"
consumer_secret = "your_consumer_secret"
access_token = "your_access_token"
access_token_secret = "your_access_token_secret"

social_media = SocialMediaIntegration(consumer_key, consumer_secret, access_token, access_token_secret)

def shareOnSocialMedia(content):
    social_media.share_on_twitter(content)
```

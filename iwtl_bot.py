# Written by Adam Ventura
# This is a program that responds to post on the r/IWantToLearn subreddit
import praw
from bot_replies import replies
from keys import keys

# Use keys to authenticate with reddits API
reddit = praw.Reddit(
     client_id=keys['client_id'],
     client_secret=keys['client_secret'],
     user_agent=keys['user_agent'],
     username=keys['username'],
     password=keys['password'] 
     )
	
print("Logged in.")

# Store keywords for the investing reply in investing_titles variable
# Store replies in investing_reply
investing_titles = ["stock", "invest"]
investing_reply = replies["investing"]

# Store keywords for the learning how to learn reply in learn_titles variable
# Store replies in learn_reply
learn_titles = ["iwtl how to learn", "i want to learn how to learn"]
learn_reply = replies["learn"]

# Store keywords for focus reply in focus_titles variable
# Store replies in focus_reply
focus_titles = ["focus", "attention"]
focus_reply = replies["focus"]

# Store keywords for math reply in math_titles variable
# Store replies in math_reply
math_titles = ["math", "maths", "arithmetic", "mathemetics"]
math_reply = replies["math"]

# Store keywords for english reply in english_titles variable
# Store replies in english_reply
english_titles =["english", "grammar", "vocabulary", "vocab"]
english_reply = replies["english"]

# Use the IWantToLearn subreddit
subreddit = reddit.subreddit("IWantToLearn")
# Use a for loop to iterate through the stream of posts on the subreddit
for submission in subreddit.stream.submissions(skip_existing=True):
	# Make submission titles lowercase to make keywords not case sensitive
	normalized_title = submission.title.lower()

	# Structure of the following nested for loops:
	# Create for loop to iterate the keywords through the submission stream
		# If key words in the lower case submission titles
			# Reply to the submission with an investing reply
			# Upvote the submission
			# Log in the console that investing resources were commented
			# Break the for loop to prevent duplicate replies when multiple key words are found
	
	for investing_title in investing_titles:
		if investing_title in normalized_title:
			submission.reply(investing_reply)
			submission.upvote()
			print("Commented investing resources.")
			break
	
	for learn_title in learn_titles:
		if learn_title in normalized_title:
			submission.reply(learn_reply)
			submission.upvote()
			print("Commented learning how to learn resources.")
			break

	for math_title in math_titles:
		if math_title in normalized_title:
			submission.reply(math_reply)
			submission.upvote()
			print("Commented math resources.")
			break
	
	for focus_title in focus_titles:	
		if focus_title in normalized_title:
			submission.reply(focus_reply)
			submission.upvote()
			print("Commented focus resources.")
			break

	for english_title in english_titles:
		if english_title in normalized_title:
			submission.reply(english_reply)
			submission.upvote()
			print("Commented english resources.")
			break



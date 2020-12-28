import praw
from bot_replies.py import replies
from keys import keys

reddit = praw.Reddit(
     client_id=keys['client_id'],
     client_secret=keys['client_secret'],
     user_agent=keys['user_agent'],
     username=keys['username'],
     password=keys['password'] 
     )
	
print("Logged in.")

investing_titles = ["stock", "invest"]
investing_reply = replies["investing"]

learn_titles = ["iwtl how to learn", "i want to learn how to learn"]
learn_reply = replies["learn"]

tech_title = ["code", "program", "computer"]


focus_titles = ["focus", "attention"]
focus_reply = replies["focus"]

math_titles = ["math", "maths", "arithmetic", "mathemetics"]
math_reply = replies["math"]

english_titles =["english", "grammar", "vocabulary", "vocab"]
english_reply = replies["english"]

subreddit = reddit.subreddit("IWantToLearn")
for submission in subreddit.stream.submissions(skip_existing=True):
	normalized_title = submission.title.lower()

	for investing_title in investing_titles:
		if investing_title in normalized_title:
			submission.reply(investing_reply)
			print("Commented investing resources.")
			break
	
	for learn_title in learn_titles:
		if learn_title in normalized_title:
			submission.reply(learn_reply)
			print("Commented learning how to learn resources.")
			break

	for math_title in math_titles:
		if math_title in normalized_title:
			submission.reply(math_reply)
			print("Commented math resources.")
			break
	
	for focus_title in focus_titles:	
		if focus_title in normalized_title:
			submission.reply(focus_reply)
			print("Commented focus resources.")
			break

	for english_title in english_titles:
		if english_title in normalized_title:
			submission.reply(english_reply)
			print("Commented english resources.")
			break



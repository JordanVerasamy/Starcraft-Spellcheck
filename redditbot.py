import praw
import time

r = praw.Reddit('experimenting with reddit python api')

r.login('starcraftspellcheck', 'swarmhost')

typos = ['swarmhost', 'swarm host']

while True:

	subreddit = r.get_subreddit('starcraft')

	for submission in subreddit.get_hot(limit=5):

		flat_comments = praw.helpers.flatten_tree(submission.comments)
		already_done = set()

		for comment in flat_comments:

			has_typo = False

			for s in typos:
				if s in comment.body:
					has_typo = True

			if has_typo and comment.id not in already_done:
				comment.reply('A typo was detected. Did you accidentally type "swarmhost" when you meant to type "cancer"?')
				already_done.add(comment.id)

	print 'Iteration complete'
	time.sleep(1000)
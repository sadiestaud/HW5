import unittest
import tweepy
import requests
import json

## SI 206 - W17 - HW5
## COMMENT WITH:
## Your section day/time: Friday 9AM
## Any names of people you worked with on this assignment:

######## 500 points total ########

## Write code that uses the tweepy library to search for tweets with a phrase of the user's choice 
# (should use the Python input function), and prints out the Tweet text and the created_at value 
# (note that this will be in GMT time) of the first THREE tweets with at least 1 blank line in between each of them, e.g.

## TEXT: I'm an awesome Python programmer.
## CREATED AT: Sat Feb 11 04:28:19 +0000 2017

## TEXT: Go blue!
## CREATED AT: Sun Feb 12 12::35:19 +0000 2017

## .. plus one more.

## You should cache all of the data from this exercise in a file, and submit the cache file along with your assignment. 

## So, for example, if you submit your assignment files, and you have already searched for tweets 
## about "rock climbing", when we run your code, the code should use CACHED data, and should not  need to make any new request to the Twitter API. 
## But if, for instance, you have never searched for "bicycles" before you submitted your final files, 
## then if we enter "bicycles" when we run your code, it _should_ make a request to the Twitter API.


## We've provided some starter code below, like what is in the class tweepy examples.

## **** For 50 points of extra credit, create another file called twitter_info.py that contains your consumer_key, consumer_secret, access_token, and access_token_secret, import that file here, and use the process we discuss in class to make that information secure! Do NOT add and commit that file to a public GitHub repository.

## **** If you choose not to do that, we strongly advise using authentication information for an 'extra' Twitter account you make just for this class, and not your personal account, because it's not ideal to share your authentication information for a real account that you use frequently.

## Get your secret values to authenticate to Twitter. You may replace each of these with variables rather than filling in the empty strings if you choose to do the secure way for 50 EC points
consumer_key = "0LUQNyJKuJXNFkq1Td9Xd4P6E" 
consumer_secret = "SDcn2VAkt1lmBipDOwrPtyK7pVRR1ykYp9fmtTs3VgS8nmZZ1b"
access_token = "833061822827724800-VEjrEuYbnxb30pf9rPnp1KDzeLLcF6r"
access_token_secret = "cIUQ4wYbjVbaNOPoO2Zmj19bIsISzYHsKKkrltBmug8gG"
## Set up your authentication to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser()) # Set up library to grab stuff from twitter with your authentication, and return it in a JSON-formatted way

## Write the rest of your code here!

#### Recommended order of tasks: ####



## 1. Set up the caching pattern start -- the dictionary and the try/except statement shown in class.
CACHE_FNAME = "cache_file.json"

try:
	cache_file = open(CACHE_FNAME, 'r')
	cache_contents = cache_file.read()
	CACHE_DICT = json.loads(cache_contents)
	cache_file.close()

except:
	CACHE_DICT = {}


## 2. Write a function to get twitter data that works with the caching pattern, so it either gets new data or caches data, 
		# depending upon what the input to search for is. You can model this off the class exercise from Tuesday.
def twitter_info(phrase):

	if phrase in CACHE_DICT:
		print("using cache\n")
		response = CACHE_DICT[phrase]

	else:
		print("fetching\n")
		response = api.search(q=phrase)
		CACHE_DICT[phrase] = response
		# response_text = response.text

		cache_file = open(CACHE_FNAME, 'w')
		cache_file.write(json.dumps(CACHE_DICT))
		cache_file.close()

	return response

	# single_tweet = response[0]
	# return single_tweet
	# for tweet in response['statuses']:
	# 	x = response['statuses'][0]['text']
	
	# return response['statuses'][0]['text']



## 3. Invoke your function, save the return value in a variable, and explore the data you got back!
x = input("Enter something to search twitter!: ")
t_info = twitter_info(x)
# print(t_info)
## 4. With what you learn from the data -- e.g. how exactly to find the text of each tweet 
		# in the big nested structure -- write code to print out content from 3 tweets, as shown above.
tweets = []
times = []
for t in t_info['statuses']:
	tweet = t['text']
	time = t['created_at']
	tweets.append(tweet)
	times.append(time)

for t in range(3):
	print("TEXT: " + tweets[t])
	print("CREATED AT: " + times[t]+"\n")
		


# Import the necessary package to process data in JSON format
try:
	import json
except ImportError:
	import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API
ACCESS_TOKEN = '833855784563847168-Zuv8EULBx7OWlMtwp4GaKpeVVYS3t1N'
ACCESS_SECRET = '6r4k65EG3Ye99SewiRVBBmtQrn4CX6vEdpmIrLcZuhgJL'
CONSUMER_KEY = 'QJ2StRsmktpV7J80dukvXQsmn'
CONSUMER_SECRET = 'qfenZbZzB8G6bW5kg8iU3ZlhWOwRQLjG4arSGykFMI30ITqGt9'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter REST API
twitter = Twitter(auth=oauth)

# Search for latest tweets about "#nlproc"
resp = twitter.search.tweets(q='"University of Portland"', result_type='recent', lang='en', count=100)

#parsed = json.loads(resp)
#print json.dumps(resp, indent=4, sort_keys=True)


import mysql.connector



try:
	cnx = mysql.connector.connect(user='warlen17', password='warlen17',
								  host='egr4.campus.up.edu',
								  database='warlen17')

#for (a, b, c) in cursor:
#print("{}, {} was hired on".format(a,b))

except mysql.connector.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("Something is wrong with your user name or password")
	elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print("Database does not exist")
	else:
		print(err)
#else:
#cnx.close()



for r in resp["statuses"]:
	
	#tweet information
	tweet_id = r["id"]
	print tweet_id
	timestamp = r["created_at"]
	favorite_ct = r["favorite_count"]
	#url = r["expanded_url"]
	place = ""
	if r["place"] != None:
		place = r["place"]["full_name"]
	retweets = r["retweet_count"]
	tweet_text = r["text"]

	#user information
	user = r["user"]
	user_id = user["id"]
	screenname = user["screen_name"]
	followers = user["followers_count"]
	friends = user["friends_count"]
	location = user["location"]
	user_since = user["created_at"]
	user_description = user["description"]
	favorites = user["favourites_count"]
	user_name = user["name"]
	timezone = user["time_zone"]
	num_statuses = user["statuses_count"]
	
	
	#hashtags & user mentions
	if r["entities"] != None:
		#hashtags
		if r["entities"]["hashtags"] != None:
			for h in r["entities"]["hashtags"]:
				if cnx is None:
					print "no connection"
				else:
					cursor = cnx.cursor()
					
					
					hashtag = h["text"]
					query = ("INSERT INTO hashtags"
							 "(tweet_id, user_id, hashtag) "
							 "VALUES (" + str(tweet_id) +", " + str(user_id) + ", \"" + hashtag + "\")")
							 cursor.execute(query)
		#user mentions
	if r["entities"]["user_mentions"] != None:
		for u in r["entities"]["user_mentions"]:
			if cnx is None:
				print "no connection"
			else:
				cursor = cnx.cursor()
					
				screen_name_m = u["screen_name"]
				name_m = u["name"]
				query = ("INSERT INTO user_mentions"
						"(tweet_id, user_name, mentioned_screen_name) "
						"VALUES (" + str(tweet_id) +", \"" + name_m + "\", \"" + screen_name_m + "\")")
				cursor.execute(query)




cnx.close()
'''
	
	import mysql.connector
	
	
	
	try:
	cnx = mysql.connector.connect(user='warlen17', password='warlen17',
	host='egr4.campus.up.edu',
	database='warlen17')
	if cnx is None:
	print "no connection"
	else:
	print cnx
	cursor = cnx.cursor()
	age = 5
	query = ("INSERT INTO test"
	"(name, age, birthday) "
	"VALUES ('dabs', 5,'1994-04-17')")
	
	
	cursor.execute(query)
	#for (a, b, c) in cursor:
	#print("{}, {} was hired on".format(a,b))
	
	except mysql.connector.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
	print("Something is wrong with your user name or password")
	elif err.errno == errorcode.ER_BAD_DB_ERROR:
	print("Database does not exist")
	else:
	print(err)
	else:
	cnx.close()
	
	'''


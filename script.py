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

def add_quotes(str):
	return "\"" + str + "\""

def timestamp_to_str(datetime):
	month = month_to_num(datetime[4:7])
	day = datetime[8:10]
	year = datetime[26:]
	time = datetime[11:19]
	return "\""+ str(year) + "-" + str(month) + "-" + str(day) + " " + str(time) + "\""



def month_to_num(month):
	return {
		'Jan' : 1,
		'Feb' : 2,
		'Mar' : 3,
		'Apr'	 : 4,
		'May' : 5,
		'Jun' : 6,
		'Jul' : 7,
		'Aug' : 8,
		'Sep' : 9,
		'Oct' : 10,
		'Nov' : 11,
		'Dec' : 12 }[month]


try:
	cnx = mysql.connector.connect(user='warlen17', password='warlen17',
								  host='egr4.campus.up.edu',
								  database='warlen17')


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
	tweet_id = r["id_str"]
	print tweet_id
	timestamp = r["created_at"]
	favorite_ct = r["favorite_count"]
	#url = r["expanded_url"]
	place = ""
	if r["place"] != None:
		place = r["place"]["full_name"]
	retweets = r["retweet_count"]
	tweet_text = r["text"]
	tweet_text = tweet_text.encode('ascii', 'ignore').decode('ascii')
	print tweet_text

	#user information
	user = r["user"]
	user_id = user["id_str"]
	if user_id is None:
		user_id = ""
	screenname = user["screen_name"]
	if screenname is None:
		screenname = ""
	followers = user["followers_count"]

	friends = user["friends_count"]
	location = user["location"]
	if location is None:
		location = ""
	user_since = user["created_at"]

	user_description = user["description"]
	if user_description is None:
		user_description = ""
	favorites = user["favourites_count"]

	user_name = user["name"]
	if user_name is None:
		user_name = ""
	timezone = user["time_zone"]
	if timezone is None:
		timezone = ""
	num_statuses = user["statuses_count"]

	#users
	if cnx is None:
		print "no connection"
	else:
		cursor = cnx.cursor()
		query = ("INSERT IGNORE INTO users"
				 "(user_id, screen_name, user_name, followers, friends, location, user_since, description, favorites, timezone, num_statuses) "
				 "VALUES (" + add_quotes(user_id) + ", " + add_quotes(screenname) + ", " + add_quotes(user_name) + ", " + str(followers) + ", " + str(friends) + ", " + add_quotes(location) + ", " + timestamp_to_str(user_since) + ", " + add_quotes(user_description) + ", " + str(favorites) + "," + add_quotes(timezone) + ", " + str(num_statuses) + ")")
		try:
			cursor.execute(query)
		except mysql.connector.Error as err:
			print err
		
	#tweets
	if cnx is None:
		print "no connection"
	else:
		cursor = cnx.cursor()
		query = ("INSERT IGNORE INTO tweets"
				 "(tweet_id, created_at, tweet_text, favorite_count, place, retweets, user_id) "
				 "VALUES (" + add_quotes(tweet_id) + ", " + timestamp_to_str(timestamp) + ", " + (add_quotes(tweet_text)) + ", " + str(favorite_ct) + ", " + add_quotes(place) + ", " + str(retweets) + ", " + add_quotes(user_id) + ")")

		cursor.execute(query)


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
					query = ("INSERT IGNORE INTO hashtags"
							 "(tweet_id, user_id, hashtag) "
							 "VALUES (" + add_quotes(tweet_id) +", " + add_quotes(user_id) + ", " + add_quotes(hashtag) + ")")
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
					query = ("INSERT IGNORE INTO user_mentions"
							"(tweet_id, user_name, mentioned_screen_name) "
							"VALUES (" + add_quotes(tweet_id) +", " + add_quotes(name_m) + ", " + add_quotes(screen_name_m) + ")")
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


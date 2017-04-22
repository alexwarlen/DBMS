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
	cnx = mysql.connector.connect(user='root', password='elvisp', host='localhost', database='teamrocket')
except mysql.connector.Error as err:
	#if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("Something is wrong with your user name or password")
	#elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print("Database does not exist")
	#else:
		print(err)

if cnx is None:
    print "no connection"
else:
    cursor = cnx.cursor()
    query = "INSERT INTO test (name, age) " \
            "VALUES (\"Alexandra\", 22)"

    cursor.execute(query)
  




cnx.close()


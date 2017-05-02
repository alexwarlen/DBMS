use teamrocket;

#create table hashtags(tweet_id varchar(20), user_id varchar(20), hashtag text);
#create table tweets(tweet_id varchar(20), created_at datetime, tweet_text text, favorite_count mediumtext, place text, retweets mediumtext, user_id varchar(20));
#create table user_mentions(tweet_id varchar(20), user_name text, mentioned_screen_name text);
#create table users(user_id varchar(20), screen_name text, user_name text, followers mediumtext, friends mediumtext, location text, user_since datetime, description text, favorities mediumtext, timezone text, num_statuses mediumtext);
#ALTER TABLE tweets ADD PRIMARY KEY(tweet_id);
#ALTER TABLE users ADD PRIMARY KEY(user_id);
#ALTER TABLE hashtags ADD FOREIGN KEY (`user_id`) REFERENCES users(`user_id`);

#ALTER TABLE hashtags ADD FOREIGN KEY (`tweet_id`) REFERENCES tweets(`tweet_id`);
#describe hashtags;
#ALTER TABLE tweets ADD FOREIGN KEY (`user_id`) REFERENCES users(`user_id`);
#ALTER TABLE user_mentions ADD FOREIGN KEY (`tweet_id`) REFERENCES tweets(`tweet_id`);
#describe user_mentions;
#describe users;
select distinct tweets.user_id, users.screen_name, users.user_name, users.location, users.timezone, users.followers, count(*) as count from tweets tweets

left join users users on tweets.user_id=users.user_id

group by user_id order by count desc;


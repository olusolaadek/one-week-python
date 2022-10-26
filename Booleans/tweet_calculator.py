tweet = input("Enter your tweet: ")

tweet_len = len(tweet)

if tweet_len <= 140:
    print(f'That {tweet_len} chars tweet will work!')
else:
    print(f'Your {tweet_len} char tweet is {tweet_len -140} chars too long')

This is what my plan was:

1. Collect all the crypto custodians names from the stie in issue
2. Collect dates from google news when crypto name was most frequent (but unfortunately I'd no time to use it)
3. I chose 3 topics: withdrawal issues, hacker attacks, fraud. For each topic I found a synonyms that can be used in twitter search
4. I've tried to use twitter official API, but timeouts was pain, so I found alternative - **stweet**
5. For each crypto and topic I parse some tweets (and I used OR operator for synonyms from point 3). And save them in individual folder that you can find in data.zip archive
6. Then I used one version of bertweet for sentiment analysis, to find only negative tweets
7. The result dataset is in negative_tweets.txt.zip


P.S. I didn't have much time (because of my current job and "it's small but honest work" meme is applies to this situation) to filter tweets better and use topic modeling for example. But if it will help to pass my application further - I'll try to find some time on the next week to tune this solution
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

sentence_1 = "i had a great time at the movie it was really funny"
sentence_2 = "i had a great time at the movie but the parking was terrible"
sentence_3 = "i had a great time at the movie but the parking wasn't great"
sentence_4 = "i went to see a movie"

vader_sentiment = SentimentIntensityAnalyzer()

print(sentence_1)
print(vader_sentiment.polarity_scores(sentence_1))

print(sentence_2)
print(vader_sentiment.polarity_scores(sentence_2)) 

print(sentence_3)
print(vader_sentiment.polarity_scores(sentence_3)) 

print(sentence_4)
print(vader_sentiment.polarity_scores(sentence_4)) 
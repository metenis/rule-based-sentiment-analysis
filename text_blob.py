from textblob import TextBlob

sentence_1 = "i had a great time at the movie it was really funny"
sentence_2 = "i had a great time at the movie but the parking was terrible"
sentence_3 = "i had a great time at the movie but the parking wasn't great"
sentence_4 = "i went to see a movie"

print(sentence_1)
sentiment_score = TextBlob(sentence_1)
print(sentiment_score.sentiment.polarity)

print(sentence_2)
sentiment_score_2 = TextBlob(sentence_2)
print(sentiment_score_2.sentiment.polarity)

print(sentence_3)
sentiment_score_3 = TextBlob(sentence_3)
print(sentiment_score_3.sentiment.polarity)

print(sentence_4)
sentiment_score_4 = TextBlob(sentence_4)
print(sentiment_score_4.sentiment.polarity)


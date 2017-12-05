import nltk
from textblob import TextBlob
from googletrans import Translator
translator = Translator()

text = input("Enter text: ")

sentence = text.split('।')

en_sent = translator.translate(text).text
en_split = en_sent.split('.')

for i, val in enumerate(sentence):
    print("Sentence [" + str(i+1) + "] = " + val)

for i, val in enumerate(sentence):
    token = nltk.word_tokenize(val)
    print("\nWords of Sentence [" + str(i+1) + "] = ", end="")
    for j in token:
        print(j + ", ", end="")

print("\n")

for i, val in enumerate(en_split):
    tb = TextBlob(val)
    print("Polarity of Sentence [" + str(i+1) + "] = ", end="")
    sentiment = tb.sentiment.polarity
    print(sentiment, end="")

    if (sentiment > 0):
        print("\t\t(Positive sentence)")

    elif (sentiment < 0):
        print("\t\t(Negative sentence)")

    else:
        print("\t\t(It\'s Neutral)")

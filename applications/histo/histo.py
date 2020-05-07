# Implement me.
import re

count = {}
f = open('robin.txt')
text = f.read().lower()
f.close()
text = re.sub('[^a-z\ \']+', " ", text)

words = list(text.split())

word_count = {}

word_set = set(words)


for word in word_set:
    word_count[word] = "#" * words.count(word)

items = list(word_count.items())

items.sort()
items.sort(key=lambda x: x[1], reverse= True)


for item in items:
    print(f'{item[0]:{17}}{item[1]}')
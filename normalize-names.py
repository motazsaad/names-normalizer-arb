import sys, os
from textblob import TextBlob
import textblob

with open('names.list') as file_reader:
    names = file_reader.readlines()
    print(len(names))

normalized_names = set()
for name in names:
    print(name)
    blob = TextBlob(name)
    try:
        trans = blob.translate(from_lang='en', to='ar')
        print(trans)
        normalized_names.add(trans)
    except textblob.exceptions.NotTranslated:
        print('No translation')
        normalized_names.add('No translation')

print(len(normalized_names))

with open('arabic-names.list', mode='w') as file_writer:
    for name in normalized_names:
        file_writer.write(name + '\n')


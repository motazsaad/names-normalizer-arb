import sys, os
import time
import urllib

from textblob import TextBlob
import textblob

with open('names.list') as file_reader:
    names = file_reader.readlines()
    print(len(names))

file_writer = open('arabic-names.list', mode='w', buffering=1)
normalized_names = set()
status = -1
delay = 5
for name in names:
    print(name)
    blob = TextBlob(name)
    while status != 200:
        try:
            trans = blob.translate(from_lang='en', to='ar')
            print(trans)
            normalized_names.add(trans)
            file_writer.write(trans + '\n')
            status = 200
        except textblob.exceptions.NotTranslated:
            print('No translation')
            normalized_names.add('No translation')
            status = 200
        except urllib.error.HTTPError as error:
            print('error: {}'.format(error))
            status = -1
            print('sleep for {} seconds'.format(delay))
            time.sleep(delay)

print(len(normalized_names))




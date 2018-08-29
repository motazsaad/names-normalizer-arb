import sys, os
import time
import urllib

from textblob import TextBlob
import textblob


def do_work(file_name, from_lang, to_lang):
    with open(file_name) as file_reader:
        names = file_reader.readlines()
        print(len(names))

    file_writer = open('out_' + file_name, mode='w', buffering=1)
    normalized_names = set()
    delay = 5
    for name in names:
        print(name)
        blob = TextBlob(name)
        status = -1
        while status != 200:
            try:
                translation = blob.translate(from_lang=from_lang, to=to_lang)
                print(translation)
                normalized_names.add(translation)
                file_writer.write(str(translation) + '\n')
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
    print('done')


def normalize_arabic_names(file_name):
    with open(file_name) as file_reader:
        names = file_reader.readlines()
        print(len(names))

    file_writer = open('out_' + file_name, mode='w', buffering=1)
    normalized_names = set()
    delay = 5
    for name in names:
        print('name: {}'.format(name))
        status = -1
        while status != 200:
            try:
                en_trans = TextBlob(name).translate(from_lang='ar', to='en')
                print('en: {}'.format(en_trans))
                ar_trans = TextBlob(str(en_trans)).translate(from_lang='en', to='ar')
                print('ar: {}'.format(ar_trans))
                l = len(normalized_names)
                normalized_names.add(ar_trans)
                if len(normalized_names) > l:
                    file_writer.write(str(ar_trans) + '\n')
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
    print('done')


if __name__ == '__main__':
    # do_work('names.list', 'en', 'ar')
    normalize_arabic_names('foreign-names.list')


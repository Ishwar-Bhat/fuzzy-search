import re
from django.db import IntegrityError
from django.shortcuts import render
from add_words.models import WordsList


def add_words(req):
    if req.method == "POST":
        words_file = req.FILES['words']
        entries = []
        for line in words_file:
            entries.append(insert_line(line.decode("utf-8")))
        try:
            WordsList.objects.bulk_create(entries)
        except IntegrityError:
            pass
    return render(req, 'add_words.html', {})


def insert_line(line):
    word_info = line.split("\t")
    frequency = int(re.search(r'\d+', word_info[1]).group())
    return WordsList(word=word_info[0], frequency=frequency)

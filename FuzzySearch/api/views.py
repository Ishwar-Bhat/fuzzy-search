import json
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from add_words.models import WordsList


def search_api(req):
    response = []
    input_val = req.GET['word']
    try:
        exact_match = WordsList.objects.get(word=input_val)
        response.append(exact_match.word)
    except ObjectDoesNotExist:
        pass
    # words_list = WordsList.objects.filter(word__contains=input_val)[:25]
    words_list = WordsList.objects.filter(word__startswith=input_val)
    for word in words_list:
        response.append(word.word)
        # response = []
        # words_
        # input_val = req.GET['word']
        # try:
        #     exact_match = WordsList.objects.get(word=input_val)
        # except ObjectDoesNotExist:
        #     exact_match = None
        # # words_list = WordsList.objects.filter(word__contains=input_val)[:25]
        # words_list = WordsList.objects.filter(word__startswith=input_val).order_by('-frequency')
        # for word in words_list:
        #     words_startwith.append(word.word)
        # words_list = WordsList.objects.filter(word__contains=input_val).exclude(words__in=words_startwith).order_by(
        #     '-frequency')
        # for word in words_list:
        #     words_contains.append(word.word)
        # return HttpResponse(json.dumps(response), content_type='application/json')
    return HttpResponse(json.dumps(response[:25]), content_type='application/json')

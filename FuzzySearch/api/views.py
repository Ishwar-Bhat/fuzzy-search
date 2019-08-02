import json
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, Http404
from add_words.models import WordsList


def search_api(req):
    """
    API returns 25 matched words, the words are picked based on below conditions
    1. Exactly matched word is first
    2. Words that starts with the search key are second and sorted based on their length
    3. Words that contains the search key are second and sorted based on their length
    :param req: Request object
    :return: JSON response containing max of 25 words
    """
    response = []
    list1 = []
    list2 = []
    # Get the search key
    input_val = req.GET['word']
    # Validate search key
    if input_val == "":
        raise Http404
    # Try to find the exact macth
    try:
        exact_match = WordsList.objects.get(word=input_val)
        response.append(exact_match.word)
    except ObjectDoesNotExist:
        pass
    # Get words that starts with input value
    words_list1 = WordsList.objects.filter(word__startswith=input_val).exclude(word__in=response).order_by('-frequency')[:25]
    for word in words_list1:
        list1.append(word.word)
    list1.sort(key=len)
    response.extend(list1)
    # Get words that contains input value
    words_list2 = WordsList.objects.filter(word__contains=input_val).exclude(word__in=response).order_by('frequency')[:25]
    for word in words_list2:
        list2.append(word.word)
    list2.sort(key=len)
    response.extend(list2)
    return HttpResponse(json.dumps(response[:25]), content_type='application/json')

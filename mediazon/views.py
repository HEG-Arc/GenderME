# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseNotFound
from mediazon.models import Surname
from django.forms.models import model_to_dict


def gender(request):
    surname = request.GET.get('surname', '')
    if surname:
        try:
            genderme = Surname.objects.get(surname=surname)
            return JsonResponse(model_to_dict(genderme, exclude='id'))
        except:
            return HttpResponseNotFound("Sorry, we don't know this surname :-(")
    else:
        return HttpResponseBadRequest("You need to pass a surname as parameter. Try: http://genderme.xyz/api?surname=luc")

from django.views import View
from rest_framework.authtoken.views import ObtainAuthToken as _DrfObtainAuthToken
import json
from django.http import HttpResponse
import requests
from project import settings

from apps.api.tgbot.matrix import matrix


class ObtainAuthToken(_DrfObtainAuthToken):
    swagger_schema = None


class TelegramView(View):
    def post(self, *args, **kwargs):
        try:
            payload = json.loads(self.request.body)
            message = payload["message"]
            text = message["text"]
            chat_id = message["chat"]["id"]

            if text.isdigit() is True:
                number = int(text)
                output_for_tg = str(matrix(number)) + "matrix"
                r = requests.post(
                    f"https://api.telegram.org/bot{settings.TG}/sendMessage",
                    json={"chat_id": chat_id, "text": output_for_tg})
            else:
                r = requests.post(
                    f"https://api.telegram.org/bot{settings.TG}/sendMessage",
                    json={"chat_id": chat_id, "text": "Type integer"})
        except Exception as err:
            print(err)
        return HttpResponse()


class MatrixTGView(View):
    def post(self, *args, **kwargs):
        try:
            payload = json.loads(self.request.body)
            message = payload["message"]
            text = message["text"]
            chat_id = message["chat"]["id"]

            if text.isdigit():
                number = int(text)
                output_for_tg = str(matrix(number))
                output_for_tg = output_for_tg + "1111"
                r = requests.post(
                    f"https://api.telegram.org/bot{settings.TG_MATRIX}/sendMessage",
                    json={"chat_id": chat_id, "text": output_for_tg})
            else:
                r = requests.post(
                    f"https://api.telegram.org/bot{settings.TG_MATRIX}/sendMessage",
                    json={"chat_id": chat_id, "text": "Type integer"})
        except Exception as err:
            print(err)
        return HttpResponse()

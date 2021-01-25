from django.shortcuts import render
import requests
import telepot
from rest_framework import media

token = '1512163482:AAFYXKHprKR0AXPnRueu43OYtE7JyQB2LM4'
my_id = -1001273460695
telegramBot = telepot.Bot(token)

def send_message(text):
    telegramBot.sendMessage(-1001273460695, text, parse_mode="Markdown")

# def send_telegram(text: str):
#     token = "1512163482:AAFYXKHprKR0AXPnRueu43OYtE7JyQB2LM4"
#     url = "https://api.telegram.org/bot/"+token
#     channel_id = -1001273460695
#     url += token
#     method = url + "/sendMessage"
#
#     r = requests.post(method, data={
#          "chat_id": channel_id,
#          "text": text
#           })
#
#     if r.status_code != 200:
#         raise Exception("post_text error")


from .models import Product


def index(request):
    send_message("pupa i lupa")
    #send_telegram("hello world!")
    products = Product.objects.all()
    return render(request, 'shop/index.html', {'products': products})

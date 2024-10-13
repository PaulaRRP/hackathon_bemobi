from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
import os
import genaiClient
from decouple import config

account_sid = config('ACCOUNT_SID_TWILIO')
auth_token = config('AUTH_TOKEN_TWILIO')
client = Client(account_sid, auth_token)

def sendInitialMessage():
  message = client.messages.create(
    from_=config('TWILIO_PHONE_NUMBER'),
    body='Olá, vimos que há uma pendência em um de seus pagamentos da XXXXX por motivo "Cartão Negado". Gostaria de ver algumas opções para regularizar o seu pagamento?',
    to=config('MY_PHONE_NUMBER')
  )


def onGoingConversation(incoming_msg):
    # pegar infos do cliente a partir de um banco
    dummy_customer = 'Dívida: R$10,00, Motivo de inadimplência: Cartão negado, Dívida existe há 1 dia'
    return genaiClient.runConversationWithAI(incoming_msg, dummy_customer)
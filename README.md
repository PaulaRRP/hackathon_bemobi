PARA RODAR O PROJETO

- pip install -r requirements.txt
- preencher variáveis no .env (é necessário uma conta no Twilio e no Google para conseguir um número e os tokens)
MY_PHONE_NUMBER
TWILIO_PHONE_NUMBER
ACCOUNT_SID_TWILIO
AUTH_TOKEN_TWILIO
GEN_AI_KEY
- usar um tunnel para a porta onde irá rodar sua aplicação localmente https://pinggy.io/ e setá-lo na sua conta do twilio
- rodar no terminal: python3 app.py
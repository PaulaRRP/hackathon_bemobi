from flask import Flask, jsonify, request, redirect
import flow
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

app = Flask(__name__)


# Rota para disparo de mensagem inicial através de algum gatilho
@app.route("/sendInitialMessage", methods=['GET'])
def initialMessage():
    flow.sendInitialMessage()
    return "Mensagem enviada com sucesso!"

# Rota para conversa ser mantida
@app.route("/conversation", methods=['GET', 'POST'])
def whatsapp_reply():
    incoming_msg = request.values.get('Body', '')
    print(incoming_msg)
    return flow.onGoingConversation(incoming_msg)

# Rota para health check
@app.route('/health', methods=['GET'])
def check():
    return "up!"

# Função principal para rodar a aplicação
if __name__ == '__main__':
    app.run(debug=True)

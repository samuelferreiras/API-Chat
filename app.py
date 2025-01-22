from flask import Flask, render_template
from flask_socketio import SocketIO, send

# Configuração inicial
app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY'  
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    print(f"Mensagem recebida: {msg}")
    send(msg, broadcast=True)  

if __name__ == '__main__':
    socketio.run(app, debug=True)

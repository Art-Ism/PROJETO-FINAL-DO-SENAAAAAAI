from flask import Flask
from core.aluno.aluno_controller import aluno_controller

app = Flask(__name__)

# registro das controller
app.register_blueprint(aluno_controller)

if __name__ == "_main_":
    app.run(debug=True)
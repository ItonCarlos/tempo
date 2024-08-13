from flask import Flask
from weather.routes import weather_bp  # Importando o Blueprint

app = Flask(__name__)

# Registrando o Blueprint
app.register_blueprint(weather_bp)




if __name__ == "__main__":
    app.run(debug=True)

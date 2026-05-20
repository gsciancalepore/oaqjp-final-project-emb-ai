"""
Modulo de servidor Flask para la aplicacion de deteccion de emociones.
Proporciona rutas para analizar texto y renderizar la interfaz web.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def emotion_detector_route():
    """
    Ruta que recibe un texto por parametros, invoca al detector de emociones
    y devuelve una cadena formateada con los resultados o un mensaje de error.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    respuesta = emotion_detector(text_to_analyze)

    if respuesta['dominant_emotion'] is None:
        return "¡Texto inválido! ¡Por favor, intenta de nuevo!."

    texto = (f"Para la declaración dada, la respuesta del sistema es 'anger': {respuesta['anger']},"
            f" 'disgust': {respuesta['disgust']}, 'fear': {respuesta['fear']}, "
            f"'joy': {respuesta['joy']}, y 'sadness': {respuesta['sadness']}. "
            f"La emoción dominante es {respuesta['dominant_emotion']}.")    
    return texto

@app.route("/")
def render_index_page():
    """
    Ruta raiz que renderiza la plantilla index.html para la interfaz de usuario.
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

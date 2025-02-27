from flask import Flask, render_template, request, jsonify
import rule_engine

app = Flask(__name__)

# Definir las reglas para la evaluación de riesgo
rules = {
    "bajo_riesgo": rule_engine.Rule("edad < 30 and estado_salud == 'saludable' and estilo_vida == 'activo'"),
    "riesgo_moderado": rule_engine.Rule("edad >= 30 and edad <= 50 and (estado_salud == 'crónico' or historial_familiar == 'sí')"),
    "alto_riesgo": rule_engine.Rule("edad > 50 or (estado_salud == 'crónico' and historial_familiar == 'sí')"),
    "ocupacion_riesgo": rule_engine.Rule("ocupacion in ['bombero', 'minero', 'piloto']"),
    "habitos_riesgo": rule_engine.Rule("fumador == 'sí' or alcohol_excesivo == 'sí'"),
    "historial_seguro_malo": rule_engine.Rule("historial_seguro == 'reclamos frecuentes'"),
    "historial_seguro_bueno": rule_engine.Rule("historial_seguro == 'sin problemas' and estilo_vida == 'activo'")
}

def evaluar_riesgo(cliente):
    if rules["alto_riesgo"].matches(cliente):
        return "Alto Riesgo"
    elif rules["riesgo_moderado"].matches(cliente) or rules["ocupacion_riesgo"].matches(cliente) or rules["habitos_riesgo"].matches(cliente) or rules["historial_seguro_malo"].matches(cliente):
        return "Riesgo Moderado"
    elif rules["bajo_riesgo"].matches(cliente) or rules["historial_seguro_bueno"].matches(cliente):
        return "Bajo Riesgo"
    return "Riesgo Moderado"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/evaluar', methods=['POST'])
def evaluar():
    datos = request.json
    nombre = datos.get("nombre", "Usuario")
    nivel_riesgo = evaluar_riesgo(datos)
    return jsonify({"riesgo": nivel_riesgo, "nombre": nombre})

if __name__ == '__main__':
    app.run(debug=True)

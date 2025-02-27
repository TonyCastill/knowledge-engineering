import rule_engine

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

# Datos de prueba
cliente1 = {
    "edad": 35,
    "estado_salud": "crónico",
    "historial_familiar": "sí",
    "estilo_vida": "sedentario",
    "ocupacion": "oficina",
    "fumador": "no",
    "alcohol_excesivo": "no",
    "historial_seguro": "sin problemas"
}

cliente2 = {
    "edad": 28,
    "estado_salud": "saludable",
    "historial_familiar": "no",
    "estilo_vida": "activo",
    "ocupacion": "oficina",
    "fumador": "no",
    "alcohol_excesivo": "no",
    "historial_seguro": "sin problemas"
}
cliente3 = {
    "edad": 20,
    "estado_salud": "crónico",
    "historial_familiar": "sí",
    "estilo_vida": "activo",
    "ocupacion": "bombero",
    "fumador": "no",
    "alcohol_excesivo": "no",
    "historial_seguro": "reclamos frecuentes"
}
cliente4 = {
    "edad": 40,
    "estado_salud": "saludable",
    "historial_familiar": "sí",
    "estilo_vida": "activo",
    "ocupacion": "piloto",
    "fumador": "sí",
    "alcohol_excesivo": "sí",
    "historial_seguro": "reclamos frecuentes"
}
cliente5 = {
    "edad": 35,
    "estado_salud": "saludable",
    "historial_familiar": "sí",
    "estilo_vida": "activo",
    "ocupacion": "minero",
    "fumador": "no",
    "alcohol_excesivo": "no",
    "historial_seguro": "sin problemas"
}

print("Cliente 1 - Nivel de Riesgo:", evaluar_riesgo(cliente1))
print("Cliente 2 - Nivel de Riesgo:", evaluar_riesgo(cliente2))
print("Cliente 3 - Nivel de Riesgo:", evaluar_riesgo(cliente3))
print("Cliente 4 - Nivel de Riesgo:", evaluar_riesgo(cliente4))
print("Cliente 5 - Nivel de Riesgo:", evaluar_riesgo(cliente5))



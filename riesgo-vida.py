import rule_engine

#Clientes
clientes = [{
    "nombre":"Humberto",
    "edad":23,
    "salud":"saludable",
    "historial_familiar":"false",
    "estilo_vida":"activo",
    "ocupacion":"oficinista",
    "historial_seguro":"bueno"
    },
    {
    "nombre":"Josue",
    "edad":40,
    "salud":"diabetes",
    "historial_familiar":"true",
    "estilo_vida":"activo",
    "ocupacion":"piloto",
    "historial_seguro":"malo"
    },
    {
    "nombre":"Jorge",
    "edad":33,
    "salud":"obesidad",
    "historial_familiar":"false",
    "estilo_vida":"activo",
    "ocupacion":"minero",
    "historial_seguro":"bueno"
    },
     {
    "nombre":"Diana",
    "edad":29,
    "salud":"saludable",
    "historial_familiar":"false",
    "estilo_vida":"activo",
    "ocupacion":"oficinista",
    "historial_seguro":"bueno"
    },
      {
    "nombre":"Humberto",
    "edad":23,
    "salud":"saludable",
    "historial_familiar":"false",
    "estilo_vida":"activo",
    "ocupacion":"oficinista",
    "historial_seguro":"bueno"
    },
        
            ]
#Definir reglas
reglas_riesgo = [
        ("Alto riesgo",rule_engine.Rule)(
            "(edad>50 and (salud in 'diabetes','hipertension','obesidad']
            "historial_familiar":'true',"estilo_vida":'alcoholico',"fumador", ocupacion
        :

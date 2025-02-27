import rule_engine

#Reglas dentro del Engine
productos = [
        {
            "Nombre":"Tiburcio",
            "Edad":25,
            "Salud":"Saludable",
            "Historial_Familiar": "false",
            "Estilo_vida":"Activo",
            "Ocupacion":"Oficinista",
            "Historial_seguro":"Sin problemas"
        },
       {
            "Nombre":"Furcio",
            "Edad":45,
            "Salud":"Obesidad",
            "Historial_Familiar": "false",
            "Estilo_vida":"",
            "Ocupacion":"Oficinista",
            "Historial_seguro":"Sin problemas"
        },
         {
            "Nombre":"Audifono",
            "Precio":"1500",
            "Stock":"4"
        },
        {
            "Nombre":"Teclado",
            "Precio":"500",
            "Stock":"5"
        },
        {
            "Nombre":"Ratón",
            "Precio":"400",
            "Stock":"4"
        },
          {
            "Nombre":"Audifono",
            "Precio":"1500",
            "Stock":"4"
        },
        {
            "Nombre":"Teclado",
            "Precio":"500",
            "Stock":"5"
        },
        {
            "Nombre":"Ratón",
            "Precio":"400",
            "Stock":"4"
        },
       ]
regla = rule_engine.Rule('Precio=="400"')
productos_filtrados = list(regla.filter(productos))
print(f"productos filtrados: {productos_filtrados}")

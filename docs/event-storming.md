# Event Storming - Flujo de reserva de esterilizacion

## Leyenda
- **Command:** accion solicitada por usuario o sistema.
- **Event:** hecho ocurrido y registrado por el flujo.
- **Policy:** regla de decision del negocio.
- **Aggregate/Data:** estado de agenda o entidad relevante.

## Diagrama Mermaid
```mermaid
graph TD
  START((Inicio)) --> C1[Command: Identificar usuario]
  C1 --> E1[Event: Usuario identificado]
  E1 --> P1{Policy: Cuantas mascotas?}

  P1 -->|Mas de 1| E2[Event: Derivar a llamada]
  E2 --> END1((Fin))

  P1 -->|Una mascota| C2[Command: Solicitar especie, sexo, peso]
  C2 --> E3[Event: Datos clinicos recibidos]
  E3 --> P2{Policy: Especie}

  P2 -->|Gato| C3[Command: Preguntar datos adicionales]
  C3 --> E4[Event: Gato validado]
  E4 --> P3[Policy: Calcular tiempo gato]

  P2 -->|Perro| C4[Command: Validar celo y peso]
  C4 --> P4{Policy: En celo?}
  P4 -->|Si| E5[Event: Rechazo temporal]
  E5 --> END2((Fin))
  P4 -->|No| P5[Policy: Calcular tiempo perro]

  P3 --> C5[Command: Comprobar disponibilidad]
  P5 --> C5

  C5 --> A1[(Aggregate: Agenda diaria)]
  A1 --> P6{Policy: Minutos ocupados + nueva cita <= 240}
  P6 -->|No| E6[Event: Sin disponibilidad]
  E6 --> C6[Command: Proponer siguiente dia]
  C6 --> A1

  P6 -->|Si| P7{Policy: Si es perro, total perros <= 2}
  P7 -->|No| E7[Event: Restriccion por especie]
  E7 --> C6
  P7 -->|Si| E8[Event: Fecha valida]

  E8 --> C7[Command: Mostrar fechas y confirmar]
  C7 --> E9[Event: Cita confirmada]
  E9 --> C8[Command: Enviar instrucciones preoperatorias]
  C8 --> END3((Fin))
```

## Resumen numerado del flujo
1. Se identifica al usuario y se valida si gestiona una o varias mascotas.
2. Si hay multiples mascotas, se deriva a llamada por complejidad operativa.
3. Se solicitan datos clinicos minimos para clasificar el servicio.
4. Se calcula tiempo quirurgico segun especie, sexo y peso.
5. Se valida disponibilidad por capacidad diaria y restriccion por especie.
6. Si no hay hueco valido, se propone siguiente dia.
7. Si hay disponibilidad, se confirma fecha y se envian instrucciones.

# Reglas de negocio explicitas

## Objetivo
Documentar las politicas operativas para la reserva de esterilizacion en clinica veterinaria.

## Politicas operativas
1. **Capacidad diaria maxima:** 240 minutos de cirugia por dia operativo.
2. **Dias operativos por defecto:** lunes a jueves para cirugia.
3. **Modelo de agenda:** inventario de minutos, no franjas publicas de quirofano.
4. **Perros por dia:** maximo 2 procedimientos caninos por dia.
5. **Gatos por dia:** sin limite por cantidad, solo sujeto a capacidad en minutos.
6. **Si hay multiples mascotas en una solicitud:** derivar a llamada para gestion asistida.
7. **Ventana de entrega para gatos:** 08:00-09:00, obligatoria.
8. **Ventana de entrega para perros:** 09:00-10:30, obligatoria.
9. **Validacion de disponibilidad:** una fecha solo se confirma si cumple simultaneamente reglas de tiempo y especie.
10. **Sin disponibilidad:** el flujo debe proponer siguiente dia habil.
11. **Privacidad:** no registrar ni publicar datos personales reales en artefactos de demostracion.
12. **Gobernanza:** no modificar business rules de Cursor.

## Tabla de tiempos de referencia
| Servicio | Tiempo |
| --- | --- |
| Gato macho | 12 min |
| Gata hembra | 15 min |
| Perro macho (cualquier peso) | 30 min |
| Perra 0-10 kg | 45 min |
| Perra 10-20 kg | 50 min |
| Perra 20-40 kg | 60 min |
| Perra >40 kg | 70 min |

## Regla de decision tipo Tetris
Una cita se acepta solo si:
1. `minutos_ocupados + minutos_nueva_cita <= 240`
2. Si especie es perro: `perros_dia + 1 <= 2`

## Resultado esperado del sistema
- Confirmar dia valido y comunicar ventana de entrega por especie.
- Enviar instrucciones preoperatorias tras confirmacion.

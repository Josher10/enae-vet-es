# Glosario, supuestos MVP y limites

## Objetivo
Establecer el contexto operativo del caso de clinica veterinaria, con definiciones comunes para el equipo y limites del MVP.

## Glosario
- **MVP:** version minima funcional para validar valor.
- **Event Storming:** tecnica para modelar eventos, decisiones y acciones del negocio.
- **Regla Tetris:** validacion de disponibilidad por capacidad diaria en minutos y restricciones por especie.
- **Entrega:** franja horaria en la que la mascota se recibe en clinica.
- **Reserva:** seleccion del dia para procedimiento, sin exponer horario quirurgico interno.
- **AC/CAC:** criterios de aceptacion del ticket.

## Supuestos del MVP
1. El chatbot atiende solicitudes para esterilizacion de perros y gatos.
2. La agenda quirurgica opera por capacidad total diaria en minutos, no por turnos fijos para clientes.
3. La clinica controla la secuencia real interna; el usuario final solo elige dia.
4. La ventana de entrega para gatos y perros es obligatoria y no negociable.
5. El flujo prioriza seguridad operativa y coherencia con reglas de negocio documentadas.

## Limites del MVP
1. No se integra calendario real en esta fase.
2. No se procesan pagos ni facturacion.
3. No se incluyen datos personales reales en documentos de ejemplo.
4. No se implementa diagnostico veterinario automatizado.
5. No se cambian business rules de Cursor.

## Criterios de calidad documental
- Las reglas deben ser auditables y trazables a tickets.
- Las decisiones de negocio deben estar en Markdown versionado.
- El README debe enlazar estos documentos.

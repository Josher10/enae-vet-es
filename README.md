# ENAE - Veterinary Clinic Chatbot

Repositorio del equipo para el caso de chatbot de clinica veterinaria en ENAE.

## Deploy en Vercel (VET-3 / ENAE-2)
Este proyecto se despliega en Vercel con integracion directa desde GitHub.

- Plataforma: Vercel
- URL de produccion: `https://enae-vet-es.vercel.app` (asumida, validar en panel)
- Flujo: GitHub push/PR -> Build Vercel -> URL Preview/Production
- Evidencia de deploy: ver `docs/deploy-vercel.md`
- Seguridad: variables de entorno solo en Vercel (no commitear secretos)

## Documentacion de dominio (VET-14 / ENAE-6)
Estos documentos son la base funcional del caso y deben leerse antes de implementar:

1. [Glosario, supuestos y limites](docs/glosario-supuestos-limites.md)
2. [Event Storming (Mermaid)](docs/event-storming.md)
3. [Reglas de negocio explicitas](docs/reglas-de-negocio.md)

## Estado
- Ticket Jira despliegue: `ENAE-2`
- Ticket Jira dominio: `ENAE-6`
- Epic: `ENAE-16` (SET UP)

## Notas
- No incluir secretos en el repositorio.
- No incluir datos personales reales en ejemplos.

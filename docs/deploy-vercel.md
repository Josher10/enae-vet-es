# Deploy Runbook - ENAE-2

## Contexto
Ticket Jira: `ENAE-2` (`VET-3`)  
Objetivo: vincular el repositorio en Vercel, validar deploy y dejar trazabilidad operativa.

## Arquitectura de despliegue
- Source of truth: repositorio GitHub `Josher10/enae-vet-es`.
- Plataforma de despliegue: Vercel.
- Entornos:
  - Preview: generado por rama/PR.
  - Production: rama estable configurada en Vercel.
- Secretos: gestionados unicamente en Vercel Environment Variables.

## Tecnologias usadas
- GitHub (SCM, PR y disparadores de build).
- Vercel (build, hosting, dominios y variables).
- Node.js y npm para build (si aplica al proyecto web).
- Markdown para documentacion operativa.

## Flujo operativo definido
1. Importar el repositorio en Vercel.
2. Configurar ramas de preview y production.
3. Definir variables en Vercel por entorno.
4. Lanzar deploy inicial.
5. Validar que el estado sea `Ready`.
6. Verificar URL de preview o production accesible.
7. Registrar evidencia y fecha en este documento y en `README.md`.

## Variables de entorno (politica)
- Nunca subir `.env` con secretos al repositorio.
- Configurar secretos solo en Vercel para cada entorno necesario.
- Rotar credenciales si se sospecha exposicion en terminales o logs.

## Evidencia de despliegue
- URL de produccion validada: `https://enae-vet-es-enae2.vercel.app`
- URL de deployment: `https://enae-vet-es-enae2-6ec5yy19n-josher10s-projects.vercel.app`
- Deployment ID: `dpl_HKWNZvkn3EgpbVvQzMKDGmcDV3SS`
- Estado real: `READY`
- Fecha de validacion (UTC): `2026-04-22T18:12:00Z`
- Comando de referencia local:

```bash
npm install
npm run build
```

## Riesgos y rollback
- Riesgo: variables faltantes -> build fallido.
- Riesgo: rama de produccion mal configurada -> despliegue incorrecto.
- Rollback: promover el ultimo deployment estable desde Vercel o revertir commit en rama estable.

## Out of scope
- Modificar business rules de Cursor.
- Cambios funcionales de negocio no relacionados con despliegue.

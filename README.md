
Ecosistema GEO 2026 para la lectura y transformación del espacio

1. ¿Qué es este repositorio?

Proyectando a la Tendencia Fuera es el repositorio principal del Ecosistema GEO 2026:  
un marco teórico–metodológico y técnico para leer, diagnosticar y proyectar territorios entendidos como espacio producido socialmente, no como contenedores vacíos.

Aquí el espacio se asume como:

una totalidad dialéctica (físico, social, simbólico),
un sistema de objetos y acciones,
una trama afectiva y relacional,
y una dimensión planetaria (Gaia) atravesada por técnicas y tecnologías.

Este repositorio reúne:

la base teórica: Geografía 2026, Espacio 2026, Manifiesto de la Integración Geo-Espacial;
el motor GEO: algoritmo conceptual para leer territorios;
lineamientos para una implementación tecnológica flexible (SIG, datos, narrativas, etc.).

No es solo código: es un ecosistema.

2. Geografía 2026 y Espacio 2026

El proyecto se sostiene sobre dos pilares conceptuales:

Geografía 2026:  
  una geografía que abandona la división rígida entre “física” y “humana” y se asume como ciencia de la síntesis, integrando:
  procesos biofísicos (relieve, clima, agua, riesgos),
  relaciones sociales, económicas y políticas,
  experiencias vividas, memorias y afectos,
  y tecnologías de representación y cálculo.

Espacio 2026:  
  el espacio es una realidad compleja y multidimensional, un producto social en constante construcción, definido por la convergencia de cuatro dimensiones:
  Espacio como producto social (trialéctica)  
     percibido (práctica material),
     concebido (representaciones técnicas y planificadas),
     vivido (experiencia simbólica y afectiva).
  Sistema de objetos y acciones (Milton Santos).
  Dimensión relacional y afectiva (lugares como puntos de encuentro, topofilia, lugares invisibles).
  Visión planetaria y tecnológica (Gaia + capacidades geocomputacionales para procesar esa complejidad).

Documentos clave (en docs/):

01-definicion-del-espacio.md  
00-geografia-2026.md (opcional, si lo incluyes luego)

3. Manifiesto de la Integración Geo-Espacial 2026

El Manifiesto de la Integración Geo-Espacial 2026 fija el marco político y ético del ecosistema:

Declara el fin de la dicotomía entre ciencias de la tierra y ciencias sociales.
Afirma la trialéctica indivisible del espacio (percibido, concebido, vivido).
Reconoce a Gaia como sistema planetario autorregulado, ya atravesado por técnica.
Recupera lo subjetivo y lo invisible (topofilia, lugares invisibles, espacios diferenciales).
Asume una responsabilidad ética y ambiental:
  riesgos como construcciones socioespaciales,
  responsabilidad a distancia,
  lucha por el espacio diferencial frente al espacio abstracto.

Documento:

docs/02-manifiesto-integracion-geo-2026.md

4. El Ecosistema GEO 2026

Proyectando a la Tendencia Fuera articula varios componentes:

Base ontológica  
   Definición de Espacio 2026.  
   Geografía 2026 como ciencia de la síntesis.

Marco político–metodológico  
   Manifiesto de la Integración Geo-Espacial 2026.  
   Principios: Intersección, Transparencia, Memoria, Ética, Espacio Diferencial, Replicabilidad.

Motor GEO (núcleo algorítmico/conceptual)  
   Representación del territorio como:text
   Entorno:
     fisico   → lo percibido + procesos de Gaia
     humano   → lo concebido + sistemas de objetos/acciones
     simbolico → lo vivido + topofilia + lugares invisibles
   Funciones principales:

   LeerTerritorio()  
     Integra dimensiones física, humana y simbólica para generar una narrativa del territorio.
   Diagnostico()  
     Recupera memoria y tensiones (contestaciones sociales) para producir un diagnóstico crítico.
   ProponerAcciones()  
     Propone recomendaciones situadas a partir del diagnóstico, guiadas por los principios del Manifiesto.

Capas de implementación tecnológica  
   (no fijadas de antemano, sino adaptables al contexto)

   Gestión de datos espaciales (SIG, cartografía digital, datos abiertos).
   Integración de datos humanos (censos, normativas, planes).
   Integración de datos simbólicos (relatos, mapeo participativo, entrevistas).
   Herramientas de geovisualización y, cuando tenga sentido, análisis y simulación.

Comunidad y usos  
   El ecosistema está pensado para ser utilizado, adaptado y criticado por:
   investigadores/as en geografía, urbanismo, ciencias sociales,
   colectivos territoriales, organizaciones comunitarias,
   instituciones que quieran repensar sus prácticas de planificación.

5. El motor GEO (versión conceptual)

En geo/core.py se incluye una implementación conceptual del motor GEO en Python.

Esquema general:python
from dataclasses import dataclass

PRINCIPIOS = [
    "Intersección",
    "Transparencia",
    "Memoria",
    "Ética",
    "EspacioDiferencial",
    "Replicabilidad",
]

@dataclass
class Entorno:
    fisico: object    # datos biofísicos y materiales
    humano: object    # datos sociales, económicos, normativos
    simbolico: object # datos narrativos, afectivos, culturales

def leer_territorio(datos_fisicos, datos_humanos, datos_simbolicos) -> str:
    """Genera una narrativa integrada del territorio."""
    ...

def diagnostico(entorno: Entorno) -> dict:
    """Produce un diagnóstico crítico (memoria + tensiones)."""
    ...

def proponer_acciones(diagnostico: dict) -> dict:
    """Sugiere líneas de acción éticas y situadas."""
    ...

def geo(entorno: Entorno) -> dict:
    """Función principal GEO: Narrativa + Diagnóstico + Recomendaciones."""
    ...
Por ahora, el código funciona como plantilla conceptual: la lógica interna (cómo combinar datos, cómo generar narrativas, etc.) debe ser diseñada según cada caso de estudio y contexto.

6. Estado del proyecto

Estado actual:  
  Marco teórico y político en construcción (Espacio 2026, Geografía 2026, Manifiesto).  
  Pseudocódigo y estructura básica del motor GEO.  
  Diseño del ecosistema GEO 2026 como referencia.

Próximos pasos posibles:
  Definir formatos de datos de entrada para fisico, humano y simbolico.
  Documentar casos de uso (por ejemplo: ciudad intermedia, cuenca, barrio).
  Desarrollar prototipos de lectura territorial con datos reales o simulados.
  Abrir el ecosistema a colaboraciones y críticas.

7. Licencia

Este proyecto se distribuye bajo la Apache License 2.0  
(puedes ajustar este punto si decides otra licencia).

8. Autoría y cocreación

Proyectando a la Tendencia Fuera – Ecosistema GEO 2026  
es una obra en construcción cocreada por:

Juan Antonio Pulido Correa (autor humano, curaduría conceptual, territorial y política).  
Inteligencia Artificial como herramienta de asistencia en redacción, organización y formalización técnica.

Toda interpretación, uso o extensión del ecosistema debe respetar:

la definición de Espacio 2026,
el Manifiesto de Integración Geo-Espacial 2026,
y los principios éticos que los sostienen.

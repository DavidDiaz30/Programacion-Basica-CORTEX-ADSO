# Programacion-Basica-ADSO
## Integrantes
### Santiago López, Ivan Alvarez, David Figueredo
### Semana 1 y 2
<img width="1999" height="1545" alt="image" src="https://github.com/user-attachments/assets/57b86c2d-c6df-4d00-b45c-47f58f8d6970" />
### Semana 3
<img width="1574" height="1566" alt="image" src="https://github.com/user-attachments/assets/f8b64b12-f5d1-41c8-bc78-2e6cfdf81ddf" />

Procesamiento Lingüístico (10/10): Dominio absoluto del lenguaje natural y sintáctico. Puede interpretar prompts complejos, traducir código entre múltiples lenguajes de programación y redactar explicaciones pedagógicas claras y estructuradas.

Aprendizaje y Memoria (9/10): Acceso instantáneo a bases de conocimiento masivas, documentación técnica y patrones de diseño. Su única limitación es el techo de la ventana de contexto durante sesiones muy extensas.

Percepción y Atención (8/10): Excelente capacidad para rastrear variables, detectar errores sintácticos y procesar contexto mediante mecanismos de atención, aunque puede obviar detalles del entorno de ejecución o interfaz gráfica.

Pensamiento y Razonamiento (8/10): Alta competencia en resolución de problemas algebráicos, diseño de algoritmos y optimización paso a paso, restringida en escenarios de abstracción profunda sin ejecución en tiempo real.

Motivación, Cognición y Emoción (3/10): Carece de emociones, conciencia o motivación intrínseca. Su acompañamiento empático y actitud alentadora son simulaciones programadas, no estados emocionales reales.

### Semana 4 y 5
<img width="1061" height="779" alt="image" src="https://github.com/user-attachments/assets/c090c52e-4aa1-4e40-8324-e7dfd650062f" />
<img width="679" height="867" alt="image" src="https://github.com/user-attachments/assets/46a95c91-38c9-45ff-8c4b-851454b66b45" />

### Semana 6
## 2. Arquitectura de Atención

Esta sección documenta el diseño del **"Gatekeeper"**: el mecanismo que decide qué parte de cada mensaje del estudiante recibe atención real del asistente, y qué se descarta como ruido. Corresponde a la Semana 6 (Atención Selectiva y Carga Cognitiva) del plan de desarrollo.

### 2.1 Principio general: Señal vs. Ruido

El asistente parte de la base de que **no toda la información de un mensaje es igual de relevante**. Antes de generar una respuesta, el Gatekeeper clasifica el contenido entrante en dos categorías:

- **Señal**: preguntas, código, mensajes de error, palabras clave técnicas (lenguajes, funciones, errores) y marcadores de intención (`?`, `!`, bloques de código entre backticks).
- **Ruido**: relleno conversacional, repeticiones, contexto irrelevante para el problema técnico planteado.

### 2.2 Regla de Atención (Gatekeeper Rule)

> **Regla principal:** Si el mensaje tiene más de 500 palabras, el mecanismo de atención solo priorizará los **sustantivos clave** y la **última frase** del mensaje.

Esta regla evita la sobrecarga cognitiva del modelo ante mensajes largos, asumiendo que:
1. Los sustantivos clave concentran la carga semántica del problema (ej. nombres de lenguajes, funciones, estructuras de datos).
2. La última frase suele contener la pregunta concreta o la petición final del estudiante, incluso si el resto del mensaje es narrativo.

### 2.3 Inventario de Inputs procesados

| Input | Ejemplo | Qué detecta el filtro |
|---|---|---|
| Texto crudo del mensaje | "pq mi for no funciona" | La pregunta o código que escribe el estudiante (contenido literal, sin interpretar) |
| Signos de puntuación | `¿`, `!`, código entre backticks o bloques ``` | Percepción básica del formato: si es pregunta o si es código |
| Metadata de hora | Timestamp 11:36 p.m. | Patrones de estudio (ej. preguntas frecuentes de noche) |
| Tono / emojis (si el canal lo permite) | Emoji triste o de enojo | Frustración o confusión del estudiante, para ajustar el tono de respuesta |
| Palabras clave técnicas | "for", "error", "python" | Lenguaje o tema tratado, para guiar la respuesta técnica |

### 2.4 Lógica de procesamiento (flujo del Gatekeeper)

1. **Mensaje recibido del estudiante** → se registra el momento del mensaje (timestamp) para detectar patrones de estudio.
2. **Análisis de símbolos** → se buscan signos como `¿`, `!`, backticks o bloques de código para distinguir entre pregunta y código (percepción básica del formato).
3. **Escaneo de emojis** (si el canal lo permite) → se detecta frustración o confusión, lo que ajusta el tono de la respuesta.
4. **Búsqueda de términos técnicos** → se identifican palabras como nombres de lenguajes, funciones o errores para guiar la respuesta técnica.
5. Con estos cuatro puntos combinados, el Gatekeeper decide **qué información pasa al motor de respuesta** y cuál se descarta como ruido.

### 2.5 Parámetros del asistente (contexto de diseño)

- **Nombre:** Asistente de aprendizaje básico de programación.
- **Público objetivo:** a partir de los 15 años.
- **Propósito:** explicar código y resolver el desconocimiento de las bases de programación.
- **Tono de respuesta:** educativo, enfocado en explicar tecnicismos con claridad.

### 2.6 Perfil cognitivo de referencia

El radar cognitivo del asistente (ver `radar_cognitivo.png`) muestra el balance de capacidades sobre el que se apoya este filtro de atención:

| Dimensión | Puntaje (0–10) |
|---|---|
| Procesamiento Lingüístico | 10 |
| Aprendizaje y Memoria | 9 |
| Percepción y Atención | 8 |
| Pensamiento y Razonamiento | 8 |
| Motivación, Cognición y Emoción | 3 |

El punto más débil es **Motivación, Cognición y Emoción (3/10)**, lo que refuerza por qué la Regla de Atención incorpora explícitamente la detección de tono/emojis: es el mecanismo compensatorio para no perder de vista el estado emocional del estudiante pese a que esa dimensión es, por diseño, la menos desarrollada del asistente.
## 3. Arquitectura de Memoria

Esta sección documenta el diseño de la memoria del asistente y corresponde a la Semana 7 (Memoria y Conocimiento Permanente) del plan de desarrollo. Las tablas simulan el esquema de una base de datos: cada fila representa una categoría de datos almacenados y el tipo de memoria al que pertenece.

### 3.1 Principio general: Memoria a largo plazo (LTM)

El asistente distingue dos tipos de memoria de largo plazo:

- **Memoria semántica:** conocimiento general y estable, independiente del estudiante (su "enciclopedia interna").
- **Memoria episódica:** información específica de cada estudiante y de sus interacciones previas con el asistente.

### 3.2 Memoria semántica (enciclopedia interna)

| Tipo de Memoria | Categoría de Datos | Descripción | Ejemplo de Entrada |
|---|---|---|---|
| Semántica (LTM) | Fundamentos de programación | Conceptos base: variables, tipos de datos y operadores | "Variable: espacio de memoria con nombre que almacena un valor" |
| Semántica (LTM) | Estructuras de control | Condicionales y ciclos con su sintaxis y uso | "for: ciclo que repite un bloque un número definido de veces" |
| Semántica (LTM) | Funciones y modularidad | Definición, parámetros y valores de retorno | "def suma(a, b): return a + b" |
| Semántica (LTM) | Errores comunes | Mensajes de error frecuentes, su causa y su solución | "IndentationError: bloque con sangría incorrecta" |
| Semántica (LTM) | Sintaxis por lenguaje | Reglas de escritura propias de cada lenguaje (Python, entre otros) | "Python: los bloques se delimitan por sangría, no por llaves" |
| Semántica (LTM) | Glosario de tecnicismos | Definiciones claras de términos técnicos para principiantes | "Algoritmo: secuencia finita de pasos para resolver un problema" |
| Semántica (LTM) | Buenas prácticas | Convenciones básicas de estilo y legibilidad del código | "Usar nombres descriptivos para las variables" |

### 3.3 Memoria episódica (datos del estudiante)

| Tipo de Memoria | Categoría de Datos | Descripción | Ejemplo de Entrada |
|---|---|---|---|
| Episódica (LTM) | Perfil del estudiante | Nivel y lenguaje con el que trabaja | "Nivel: principiante, Lenguaje: Python" |
| Episódica (LTM) | Historial de errores | Errores recurrentes del estudiante, para reforzar los temas débiles | "Error frecuente: confundir `=` con `==`" |
| Episódica (LTM) | Patrones de estudio | Horarios de consulta obtenidos del timestamp del Gatekeeper | "Consultas frecuentes después de las 11:00 p.m." |
| Episódica (LTM) | Estado emocional | Frustración o confusión detectada por tono y emojis | "Última sesión: frustración alta ante ciclos `for`" |

### 3.4 Relación con el Gatekeeper

La memoria se articula con la Arquitectura de Atención (Sección 2): el Gatekeeper filtra el mensaje del estudiante y las palabras clave técnicas detectadas (por ejemplo, `for`, `error`, `python`) funcionan como consulta hacia la memoria semántica. A su vez, el timestamp y la detección de tono alimentan la memoria episódica, lo que permite ajustar las explicaciones al historial del estudiante.

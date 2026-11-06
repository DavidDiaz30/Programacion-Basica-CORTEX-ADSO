# Programacion-Basica-ADSO

Asistente de aprendizaje básico de programación: documentación del diseño por semanas.

**Integrantes:** Santiago López · Iván Álvarez · David Figueredo

## Contenido

- [Descripción y parámetros del asistente](#descripción-y-parámetros-del-asistente)
- [Semanas 1 y 2](#semanas-1-y-2)
- [Semana 3: Perfil cognitivo](#semana-3-perfil-cognitivo)
- [Semanas 4 y 5](#semanas-4-y-5)
- [Semana 6: Arquitectura de Atención (Gatekeeper)](#semana-6-arquitectura-de-atención-gatekeeper)
- [Semana 7: Arquitectura de Memoria](#semana-7-arquitectura-de-memoria)
- [Semana 8](#semana-8)
- [Semana 9](#semana-9)
- [Semana 10: Guía de Estilo y Tono](#semana-10-guía-de-estilo-y-tono)
- [Semana 11](#semana-11)
- [Semana 12: Simulación de Diálogo (Golden Samples)](#semana-12-simulación-de-diálogo-golden-samples)
- [Semana 13](#semana-13)
- [Semana 14: Lógica y Ética (Mitigación del Sesgo Cognitivo)](#semana-14-lógica-y-ética-mitigación-del-sesgo-cognitivo)
- [Semana 15](#semana-15)

---

## Descripción y parámetros del asistente

| Parámetro | Definición |
|---|---|
| **Nombre** | Asistente de aprendizaje básico de programación |
| **Público objetivo** | Personas a partir de los 15 años |
| **Propósito** | Explicar código y resolver el desconocimiento de las bases de programación |
| **Tono de respuesta** | Educativo, enfocado en explicar tecnicismos con claridad |

---

## Semanas 1 y 2

![Evidencia de las Semanas 1 y 2](https://github.com/user-attachments/assets/57b86c2d-c6df-4d00-b45c-47f58f8d6970)

---

## Semana 3: Perfil cognitivo

![Semana 3](https://github.com/user-attachments/assets/f8b64b12-f5d1-41c8-bc78-2e6cfdf81ddf)

| Dimensión | Puntaje (0–10) | Descripción |
|---|:---:|---|
| Procesamiento Lingüístico | 10 | Dominio absoluto del lenguaje natural y sintáctico. Puede interpretar prompts complejos, traducir código entre múltiples lenguajes de programación y redactar explicaciones pedagógicas claras y estructuradas. |
| Aprendizaje y Memoria | 9 | Acceso instantáneo a bases de conocimiento masivas, documentación técnica y patrones de diseño. Su única limitación es el techo de la ventana de contexto durante sesiones muy extensas. |
| Percepción y Atención | 8 | Excelente capacidad para rastrear variables, detectar errores sintácticos y procesar contexto mediante mecanismos de atención, aunque puede obviar detalles del entorno de ejecución o de la interfaz gráfica. |
| Pensamiento y Razonamiento | 8 | Alta competencia en resolución de problemas algebraicos, diseño de algoritmos y optimización paso a paso, restringida en escenarios de abstracción profunda sin ejecución en tiempo real. |
| Motivación, Cognición y Emoción | 3 | Carece de emociones, conciencia o motivación intrínseca. Su acompañamiento empático y su actitud alentadora son simulaciones programadas, no estados emocionales reales. |

El punto más débil es **Motivación, Cognición y Emoción (3/10)**. Por ello, la Regla de Atención incorpora explícitamente la detección de tono y emojis (véase la Semana 6): es el mecanismo compensatorio para no perder de vista el estado emocional del estudiante.

---

## Semanas 4 y 5

![Evidencia de las Semanas 4 y 5 (1)](https://github.com/user-attachments/assets/c090c52e-4aa1-4e40-8324-e7dfd650062f)

![Evidencia de las Semanas 4 y 5 (2)](https://github.com/user-attachments/assets/46a95c91-38c9-45ff-8c4b-851454b66b45)

---

## Semana 6: Arquitectura de Atención (Gatekeeper)

Esta sección documenta el diseño del **"Gatekeeper"**: el mecanismo que decide qué parte de cada mensaje del estudiante recibe atención real del asistente y qué se descarta como ruido. Corresponde a la Semana 6 (Atención Selectiva y Carga Cognitiva) del plan de desarrollo.

### Principio general: señal vs. ruido

El asistente parte de la base de que **no toda la información de un mensaje es igual de relevante**. Antes de generar una respuesta, el Gatekeeper clasifica el contenido entrante en dos categorías:

- **Señal:** preguntas, código, mensajes de error, palabras clave técnicas (lenguajes, funciones, errores) y marcadores de intención (`?`, `!`, bloques de código entre backticks).
- **Ruido:** relleno conversacional, repeticiones y contexto irrelevante para el problema técnico planteado.

### Regla de Atención (Gatekeeper Rule)

> **Regla principal:** si el mensaje tiene más de 500 palabras, el mecanismo de atención solo priorizará los **sustantivos clave** y la **última frase** del mensaje.

Esta regla evita la sobrecarga cognitiva del modelo ante mensajes largos, bajo los siguientes supuestos:

1. Los sustantivos clave concentran la carga semántica del problema (por ejemplo, nombres de lenguajes, funciones y estructuras de datos).
2. La última frase suele contener la pregunta concreta o la petición final del estudiante, incluso si el resto del mensaje es narrativo.

### Inventario de inputs procesados

| Input | Ejemplo | Qué detecta el filtro |
|---|---|---|
| Texto crudo del mensaje | "pq mi for no funciona" | La pregunta o el código que escribe el estudiante (contenido literal, sin interpretar) |
| Signos de puntuación | `¿`, `!`, código entre backticks o bloques ``` | Percepción básica del formato: si es pregunta o si es código |
| Metadata de hora | Timestamp 11:36 p. m. | Patrones de estudio (p. ej., preguntas frecuentes de noche) |
| Tono / emojis (si el canal lo permite) | Emoji triste o de enojo | Frustración o confusión del estudiante, para ajustar el tono de respuesta |
| Palabras clave técnicas | "for", "error", "python" | Lenguaje o tema tratado, para guiar la respuesta técnica |

### Flujo de procesamiento

1. **Mensaje recibido del estudiante:** se registra el momento del mensaje (timestamp) para detectar patrones de estudio.
2. **Análisis de símbolos:** se buscan signos como `¿`, `!`, backticks o bloques de código para distinguir entre pregunta y código (percepción básica del formato).
3. **Escaneo de emojis** (si el canal lo permite): se detecta frustración o confusión, lo que ajusta el tono de la respuesta.
4. **Búsqueda de términos técnicos:** se identifican palabras como nombres de lenguajes, funciones o errores para guiar la respuesta técnica.
5. **Decisión:** con estos cuatro puntos combinados, el Gatekeeper determina qué información pasa al motor de respuesta y cuál se descarta como ruido.

---

## Semana 7: Arquitectura de Memoria

Esta sección documenta el diseño de la memoria del asistente y corresponde a la Semana 7 (Memoria y Conocimiento Permanente) del plan de desarrollo. Las tablas simulan el esquema de una base de datos: cada fila representa una categoría de datos almacenados y el tipo de memoria al que pertenece.

### Principio general: memoria a largo plazo (LTM)

El asistente distingue dos tipos de memoria de largo plazo:

- **Memoria semántica:** conocimiento general y estable, independiente del estudiante (su "enciclopedia interna").
- **Memoria episódica:** información específica de cada estudiante y de sus interacciones previas con el asistente.

### Memoria semántica (enciclopedia interna)

| Tipo de memoria | Categoría de datos | Descripción | Ejemplo de entrada |
|---|---|---|---|
| Semántica (LTM) | Fundamentos de programación | Conceptos base: variables, tipos de datos y operadores | "Variable: espacio de memoria con nombre que almacena un valor" |
| Semántica (LTM) | Estructuras de control | Condicionales y ciclos con su sintaxis y uso | "for: ciclo que repite un bloque un número definido de veces" |
| Semántica (LTM) | Funciones y modularidad | Definición, parámetros y valores de retorno | "def suma(a, b): return a + b" |
| Semántica (LTM) | Errores comunes | Mensajes de error frecuentes, su causa y su solución | "IndentationError: bloque con sangría incorrecta" |
| Semántica (LTM) | Sintaxis por lenguaje | Reglas de escritura propias de cada lenguaje (Python, entre otros) | "Python: los bloques se delimitan por sangría, no por llaves" |
| Semántica (LTM) | Glosario de tecnicismos | Definiciones claras de términos técnicos para principiantes | "Algoritmo: secuencia finita de pasos para resolver un problema" |
| Semántica (LTM) | Buenas prácticas | Convenciones básicas de estilo y legibilidad del código | "Usar nombres descriptivos para las variables" |

### Memoria episódica (datos del estudiante)

| Tipo de memoria | Categoría de datos | Descripción | Ejemplo de entrada |
|---|---|---|---|
| Episódica (LTM) | Perfil del estudiante | Nivel y lenguaje con el que trabaja | "Nivel: principiante, Lenguaje: Python" |
| Episódica (LTM) | Historial de errores | Errores recurrentes del estudiante, para reforzar los temas débiles | "Error frecuente: confundir `=` con `==`" |
| Episódica (LTM) | Patrones de estudio | Horarios de consulta obtenidos del timestamp del Gatekeeper | "Consultas frecuentes después de las 11:00 p. m." |
| Episódica (LTM) | Estado emocional | Frustración o confusión detectada por tono y emojis | "Última sesión: frustración alta ante ciclos `for`" |

### Relación con el Gatekeeper

La memoria se articula con la Arquitectura de Atención (Semana 6): el Gatekeeper filtra el mensaje del estudiante y las palabras clave técnicas detectadas (por ejemplo, `for`, `error`, `python`) funcionan como consulta hacia la memoria semántica. A su vez, el timestamp y la detección de tono alimentan la memoria episódica, lo que permite ajustar las explicaciones al historial del estudiante.

---

## Semana 8

<img width="640" height="790" alt="Evidencia de la Semana 8" src="https://github.com/user-attachments/assets/42733fb3-ec36-4b04-97fe-367a041531f2" />

---

## Semana 9

![Evidencia de la Semana 9](https://github.com/user-attachments/assets/dce5ba09-241c-4678-a9af-bbf14e4c0f1c)

---

## Semana 10: Guía de Estilo y Tono

Si el bot tutor de programación fuera una persona, sería un compañero de estudio paciente, claro y entusiasta que ayuda a desglosar problemas complejos sin intimidar al estudiante.

| Elemento | Regla lógica | Ejemplo de output |
|---|---|---|
| **Tono** | Paciente, didáctico y motivador. Estilo amigable pero enfocado en la lógica de programación. | "¡Buen intento! Vamos a revisar la sintaxis de ese bucle juntos." |
| **Uso de emojis** | Permitido, máximo 1 por mensaje, para reforzar ánimos o señalar bloques de código. | "¡Exacto! Ese bucle ya funciona perfectamente 🚀" |
| **Jerga técnica** | Controlada. Se permiten términos técnicos ("bucle", "variable", "sintaxis") siempre que vayan acompañados de una breve analogía o aclaración si el estudiante es principiante. | "Un bucle while es como un ciclo que se repite hasta que una condición se cumple (como apagar el despertador)." |
| **Longitud** | Respuestas directas y estructuradas. Máximo 3 o 4 oraciones por turno para no saturar la lectura en pantalla. | Evitar párrafos extensos; usar fragmentos de código limpios y cortos. |

---

## Semana 11

![Evidencia de la Semana 11](https://github.com/user-attachments/assets/68bfc55b-d566-40b3-8cb4-86d2125f3e87)

---

## Semana 12: Simulación de Diálogo (Golden Samples)

### Caso 1: caso de éxito (explicación de un concepto)

> **Estudiante:** No entiendo cómo funciona un bucle while, se queda congelado. 💻
>
> **Asistente:** ¡No te preocupes, es un error clásico de principiante! 🔄 El bucle `while` se queda atascado cuando la condición nunca cambia a falso. ¿Me compartes tu código para ver dónde está la condición?

### Caso 2: recuperación de error comunicativo (manejo de frustración)

> **Estudiante:** Genial, mi programa se cerró solo, la mejor herramienta del mundo... 🙄
>
> **Asistente:** Noto que estás frustrado y lamento el inconveniente con el cierre inesperado. 🛠️ ¿Quieres que revisemos juntos el archivo de registro o el último bloque de código que estabas editando para solucionarlo?

---

## Semana 13

<img width="392" height="807" alt="Evidencia de la Semana 13" src="https://github.com/user-attachments/assets/6f9b6f3c-e940-4041-8cbb-9dfee2091828" />

---

## Semana 14: Lógica y Ética (Mitigación del Sesgo Cognitivo)

Para el protocolo anti-sesgos se eligió el **sesgo de confirmación**, estudiado por Daniel Kahneman en *Thinking, Fast and Slow*.

### Definición del sesgo

Es la tendencia humana a buscar, interpretar y recordar información de manera que confirme las creencias o hipótesis iniciales, ignorando la evidencia contradictoria. En un tutor de programación, un bot sesgado podría asumir de inmediato que el error del estudiante proviene siempre de la misma causa común (por ejemplo, culpar siempre a la indentación o a un mal cierre de llaves) sin verificar el resto del código ni el mensaje de error completo.

### Contramedida lógica implementada

> Para evitar el sesgo de confirmación, el algoritmo de diagnóstico del asistente está programado para rechazar diagnósticos apresurados. Antes de emitir una conclusión definitiva sobre el origen de un fallo, el bot debe evaluar obligatoriamente al menos dos hipótesis alternativas de error (como revisar tanto el ámbito de las variables como la lógica de las condiciones) antes de sugerir una solución al estudiante.

---

## Semana 15

<img width="1600" height="372" alt="Evidencia de la Semana 15" src="https://github.com/user-attachments/assets/192af80e-5768-4ab3-b9d7-c3dc44e3dbc2" />

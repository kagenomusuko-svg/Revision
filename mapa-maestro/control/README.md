# Control de fuentes, lectura y continuación

Fecha: 1 de noviembre de 2026. Commit de partida: `7f5b3c3ca8cb3496c6920237f1dcc1745ddc7eac`.

## Alcance realizado

- Identificación de los siete adjuntos y cotejo SHA-256 con los siete originales canónicos del repositorio. Los siete coinciden.
- Extracción de texto página por página de los siete archivos y elaboración de un inventario de 1,613 páginas.
- Consulta temática de pasajes para fundamentar fichas y relaciones. El apéndice II de Areópago, pp. 240–254 [PDF 253–267], se consultó completo; esto no acredita la lectura del resto de Areópago.
- Inspección visual de cuatro páginas decisivas: CAO p. 263 [PDF 270], ARE p. 241 [PDF 254], CAE p. 192 [PDF 208] y DAM p. 16 [PDF 40]. Se confirmó que las precisiones y formulaciones discutidas aparecen en la página, no solo en una extracción defectuosa.
- Fichas iniciales de los siete libros, mapa transversal, registro técnico y ruta de operacionalización.

**No está concluida la lectura exhaustiva solicitada.** Todos los libros siguen abiertos. No se certifica una revisión de cada página, de cada nota, de cada demostración ni del aparato bibliográfico completo. Tampoco se han auditado externamente las afirmaciones jurídicas, históricas, clínicas o cuánticas citadas por los libros.

## Archivos de control

| Archivo | Qué acredita | Qué no acredita |
|---|---|---|
| [fuentes.json](fuentes.json) | Correspondencia de archivos, SHA-256, extensión y método de conteo | Lectura intelectual de los textos. |
| [inventario-paginas.csv](inventario-paginas.csv) | Posición PDF, etiquetas arábigas reconocidas, extensión extraída y coincidencias léxicas | Comprensión o validación de los pasajes con coincidencias. |
| Fichas por libro | Argumentos y conexiones apoyados en pasajes consultados | Dictamen exhaustivo del volumen. |
| Registro técnico | Cuestiones con localización y propuesta de resolución | Correcciones ya aceptadas o incorporadas al canon. |

El campo `consulta_tematica=sí` indica consulta de al menos un pasaje de esa página, en ocasiones parcial. Incluye índices, encabezamientos y páginas auxiliares cuando se consultaron. No significa lectura continua de la página ni de todo el capítulo. El campo `lectura_integral_acreditada` permanece en `no`: esta entrega no acredita ese nivel de revisión para las páginas del inventario.

Las coincidencias léxicas son automáticas. La ausencia de coincidencia no demuestra ausencia de un concepto: puede estar formulado con otro vocabulario, aparecer en notación no extraída o desarrollarse indirectamente. El conteo de palabras también es aproximado y no tiene valor filológico.

## Actualización: relectura focalizada

Se amplió la consulta de Areópago en los capítulos 1, 3, 4, 5, 9 y 10 y su apéndice II, y de Caelus en los desarrollos colectivos, el capítulo 13 y su apéndice. Se revisaron las objeciones sobre dolo/φ₂ y normalización: A-02, A-03 y A-06 se retiran como deudas conceptuales; A-04 incorpora una precisión ya existente. Los argumentos están en [la relectura](../04-relectura-dolo-normalizacion.md). Esto no certifica una lectura integral nueva de ambos volúmenes ni ratifica las restantes observaciones provisionales.

## Qué falta para cerrar el encargo

1. Leer cada libro de principio a fin en continuidad y registrar contenido, conexiones y dudas también en las páginas sin términos destacados.
2. Completar las fichas con la función de cada capítulo y apéndice, sin tratar sus títulos como sustituto de contenido.
3. Cotejar los pasajes que parecen tensionarse con todas sus precisiones, notas y glosarios. Actualizar el registro para retirar deudas resueltas y delimitar las que persistan.
4. Verificar visualmente las fórmulas y tablas restantes antes de transcribirlas como base de una operación.
5. Revisar las remisiones a obras fuera de los siete PDF antes de atribuirles demostraciones o soluciones no examinadas.
6. Reescribir la síntesis transversal desde la lectura completa y solo entonces declarar concluida la revisión literaria exhaustiva.

Los próximos recorridos continuos deben mantener el orden CAO, PAS, AGA, DAM, ARE, CAE y NIK. La consulta transversal ya hecha sirve de orientación, no de exención de leer las partes intermedias.

## Dependencias fuera del corpus principal

`El Contrato Fiscal - Eris`, `El Contrato Fiscal - Kratos`, `El cálculo de la responsabilidad`, `El telar de las Moiras`, `El juego de las máscaras` y los demás manuscritos del repositorio no quedan cubiertos por esta revisión de los siete adjuntos.

En la entrega inicial se consultaron puntualmente las páginas PDF 5, 16 y 59 del Cálculo que está en `libros a revisar`. Al comenzar la relectura hubo una consulta auxiliar adicional de ese manuscrito siguiendo remisiones; tras la precisión del usuario, se limitó el trabajo a Areópago y Caelus. Las conclusiones de la relectura focalizada se fundamentan exclusivamente en estos dos libros. No se presenta una lectura ni auditoría del Cálculo.

Los números de teoremas y referencias a otros títulos que aparecen en CAE se registran como remisiones del propio libro. Afirmar que un libro remite a una prueba no equivale a afirmar que esta revisión ya comprobó esa prueba.

## Condición de cierre

El trabajo podrá llamarse exhaustivo cuando cada libro cuente con lectura continua documentada, revisión de sus partes y cotejo transversal, y cuando las deudas técnicas se distingan de precisiones que ya existían en el texto. Contar páginas extraídas o coincidencias de palabras no satisface esa condición.

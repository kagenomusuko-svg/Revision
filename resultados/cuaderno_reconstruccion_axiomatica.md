# Cuaderno de reconstrucción axiomática y normalizaciones epistemológicas

**Estado:** cuaderno de trabajo; no es el manuscrito de *Axiomatización*.  
**Inicio:** 31 de octubre de 2026.  
**Ámbito:** reconstrucción de la epistemología derivada de la ontología canónica.  
**Fuentes de partida:** `libros canónicos/`, `libros a revisar/Axiomatización del sistema de la doble mediación.pdf`, `libros a revisar/El cálculo de la responsabilidad una ontología matemática para sistemas causales complejos.pdf`, `libros a revisar/El método Prometeo imputación causal para juristas y abogados.pdf`.  
**Relación con trabajos previos:** [inventario técnico acumulativo](derivacion_ontologica_y_normalizacion_formulas.md), [lectura crítica](lectura_critica_libros_a_revisar.md) y [puente aritmético-espectral](puente_aritmetico_espectral_prometeo.md). Estos documentos se conservan: el presente cuaderno registra las decisiones, preguntas resueltas y normalizaciones que resulten de la conversación de reconstrucción.

> **Regla central.** La ontología publicada es el marco canónico; la epistemología, incluida la *Axiomatización*, es objeto de revisión y reconstrucción. No se modifica la ontología para ajustar sus proposiciones a una teoría matemática elegida previamente. Tampoco se da por demostrado un teorema por el solo hecho de que una expresión aparezca en un libro epistemológico.

## 1. Para qué existe este cuaderno

Se mantendrán **dos niveles documentales separados**:

- **Libro axiomático futuro:** definiciones formales mínimas, dominios, relaciones, axiomas, proposiciones, teoremas, demostraciones, condiciones de aplicación y corolarios. Trabajará sobre **propiedades** y no necesitará narrar expedientes completos ni cargar cada relación con valores empíricos.
- **Cuaderno de investigación (este documento):** explicaciones de qué hace cada operación; genealogía **lógica** desde el canon (no historia de borradores); ejemplos que permitan comprobar la interpretación; cotejos con pasajes de los libros; alternativas, incompatibilidades, normalizaciones y decisiones editoriales. Se documenta aquí lo que el equipo necesita entender, aunque **no deba aparecer en el texto final de axiomas**.

Un caso ilustrativo es un **test de funcionamiento**, no un axioma. Un valor numérico obtenido de un expediente tampoco es una propiedad matemática universal.

### Estados de una anotación

- **C — Canónico:** proposición sustentada directamente por los libros ontológicos; consignar libro y pasaje.
- **D — Derivado:** consecuencia argumentada o demostrada de proposiciones anteriores; incluir justificación.
- **P — Propuesta:** formalización o normalización candidata, todavía no incorporada al sistema.
- **V — Verificación pendiente:** requiere una prueba, contramodelo, precisión tipada o cotejo textual.
- **R — Resuelto:** acuerdo o normalización consolidada en la investigación; no implica por sí mismo que ya se haya editado un libro.

No se ascenderá una propuesta a «demostrada» sin exhibir sus hipótesis y su derivación.

## 2. Dirección del proyecto y alcance del método

**[R: acuerdo metodológico]** Dirección de trabajo:

```text
Ontología canónica
    → propiedades estructurales que deben preservarse
    → definiciones y axiomas mínimos
    → consecuencias demostradas y operadores
    → instrumentos epistemológicos
    → aplicaciones y, sólo después, implementación
```

El **motor programado de Prometeo queda fuera de la discusión inmediata**. Puede ser cotejado más adelante contra las fórmulas normalizadas, pero no dictará la definición de los objetos matemáticos.

**[C: alcance reconstruido de Areópago, cotejar cada pasaje antes de publicarlo]** La imputación causal estudia un **evento determinado** mediante la reconstrucción de posiciones, actos, relaciones y consecuencias. No pretende calcular «la causalidad qua causalidad» ni la causalidad universal. El analista debe explicitar su discriminación del evento y las condiciones bajo las que reconstruye la cadena.

La contabilización causal puede servir para **comprender** un fenómeno, aunque no exista reparación posible, titular actual al que exigirla o sujeto jurídico imputable. Determinación causal, atribución de consecuencias y exigibilidad jurídica no son operaciones sinónimas.

## 3. Contrato funcional de las operaciones que investigamos

Este apartado es un **mapa de lo que cada operación hace**; no define aún fórmulas axiomáticas definitivas.

| Elemento | Función en el método | Estado y problema que debemos tratar |
|---|---|---|
| Evento discriminado `D` | Referente específico de la investigación causal; delimita el colapso estudiado. | [P] Formalizar cómo cambia un cálculo al cambiar `D`. |
| Nodos `N` | Posiciones, sujetos, estructuras o condiciones pertinentes al evento. | [P] Distinguir candidato investigable de contribución acreditada. |
| Relaciones `E` | Actos, habilitaciones, decisiones, omisiones y transmisiones que conectan nodos. | [P] Tipos, orientación, temporalidad y mecanismos. |
| Matriz `W` | Representación ponderada de relaciones reconstruidas hacia el evento. | [V] Separar existencia y dirección de arista, respaldo probatorio e intensidad causal; fijar convención de filas/columnas. |
| Convergencia `R*` | Participación relativa del nodo **respecto de `D`** bajo el modelo y la evidencia declarados. | [V] Precisar estimando, escala y operador; no identificar sin prueba un autovector con porcentaje de daño. |
| Sustituibilidad `S` | Contrafáctico de reemplazo del ocupante de una posición y continuidad del resultado. | [V] Formalizar intervenciones admisibles y qué parte corresponde a diseño frente a ocupante. |
| Contribución atribuible | Contribución asociada al nodo tras la operación de sustituibilidad. | [P] Distinguir descuento individual de eventual atribución estructural; prohibir doble contabilización. |
| Asunción interna `δ_int` | Operación de reconocimiento constitutivo e integración egoica; segunda mediación. | [C] No identificar automáticamente con las consecuencias materiales soportadas. |
| Imputación exterior `δ_ext` | Atribución desde la alteridad; no requiere reconocimiento interno del imputado. | [C] La atribución puede constituir, además, un acto con consecuencias propias. |
| Asunción/repercusión efectiva `α` | En el cálculo aplicado, consecuencia/carga que efectivamente recae sobre un sujeto, aun sin aceptación subjetiva. | [P] Definir operacionalmente y distinguir de aceptación interior, sanción, reparación y beneficio. |
| Asimetría repercusiva `Δ` | Comparar contribución causal con repercusión soportada, después de declarar una base comparable. | [V] Resolver convención, escala y si la comparación procede con `R*` bruto o con contribución neta. |
| Daño total / delta del daño | Cuantificar consecuencias sufridas y divergencia de trayectorias para el evento específico. | [V] Determinar magnitudes y unidades, horizonte, contrafactual y componentes aditivos que no se solapen. |
| Beneficio / delta de aprovechamiento | Registrar qué obtuvo cada nodo y cuánto revirtió del aprovechamiento. | [V] Mantener separado del cálculo del daño; establecer unidades comparables. |
| Ajuste *debitor* | Expresar el resultado posible de restauración proporcional cuando proceda. | [V] Diferenciar medida causal, restauración estructural, deducción fiscal complementaria y exigibilidad. |

La nomenclatura `δ_int` / `δ_ext` pertenece al desarrollo de *Areópago*; **no convertir automáticamente una diferencia por ciclo en `dEgo/dt`**. *Caelus* distingue explícitamente esos objetos.

## 4. Primera ficha de trabajo: qué tipo de texto será la Axiomatización

**[R: acuerdo sobre la forma]** La *Axiomatización* no será un manual del método ni el repertorio de los expedientes. Su núcleo será una exposición de objetos abstractos y sus propiedades, prescindiendo de datos particulares cuando éstos no sean necesarios.

Ejemplo de distinción (todavía no son axiomas adoptados):

- **Explicación operativa que pertenece a este cuaderno:** «Se identifica el evento de una falla ferroviaria, se reconstruyen las posiciones según documentos, permisos, protocolos y evidencia, y se examinan las relaciones pertinentes hacia ese resultado».
- **Proposición candidata para la axiomatización:** «El operador de atribución es relativo a un evento discriminado: su dominio incorpora el evento `D` o una referencia formal que lo determine».
- **Prueba que se exigiría:** explicar por qué la formulación escogida hace depender el resultado de `D` y qué se mantiene invariante cuando se cambia únicamente el nombre del evento o de los nodos.

Evitar publicar fórmulas como axiomas si son **definiciones**, identidades algebraicas derivadas, ejemplos de cálculo o hipótesis empíricas de calibración.

## 5. Normalizaciones concretas identificadas en la fase inicial

### N-01 — Atribución como acto y no como simple descripción

**[C; criterio de terminología para el trabajo]** En *Areópago*, cap. 11, la decisión de imputar tiene su propia cadena causal. Que el contenido de una atribución sea incorrecto o no quede acreditado **no anula la ocurrencia del acto de imputar**, ni deshace sus consecuencias. Para esta reconstrucción, evitar usar la etiqueta «imputación falsa» como cierre ontológico del análisis. Cuando sea necesario evaluar el contenido, hablar de **atribución no acreditada, incorrecta o desproporcionada**, indicando exactamente la propiedad evaluada.

Esto **no autoriza** a concluir automáticamente que toda imputación causa daño o que toda consecuencia da lugar a obligación jurídica de reparación. La imputación es un acontecimiento investigable.

### N-02 — Integridad entre asunción interna y asunción repercusiva

**[C/P]** La asunción de la segunda mediación es una operación constitutiva del ego. En cambio, la variable empírica de repercusión debe poder registrar **consecuencias efectivamente soportadas**, aunque el sujeto rechace la responsabilidad atribuida. *El cálculo de la responsabilidad* ya admite una «asunción forzada» al tratar condenas o sanciones. Estas magnitudes no deben ser confundidas. Decisión de nomenclatura y regla de medición: **pendientes**, no insertarlas como cambios silenciosos al canon.

### N-03 — Sustituibilidad y partición formal del puntaje

**[D: identidad algebraica; P: interpretación causal]** La expresión epistemológica publicada es:

$$
R_{i,\mathrm{neta}}^*=R_i^*(1-S_i).
$$

De ella se obtiene:

$$
R_i^*=R_i^*(1-S_i)+R_i^*S_i.
$$

La segunda igualdad es **álgebra demostrada**, pero aún no demuestra que el segundo sumando pueda **transferirse** a un diseñador específico. El eventual operador de reasignación debe justificar el destino de la participación estructural, preservar las propiedades de reparto que efectivamente se adopten y evitar contabilidad doble. **No adoptar como axioma una reasignación no demostrada.**

### N-04 — Propiedades del índice J

**[D: contraejemplo aritmético; V: decisión editorial]** En *El cálculo de la responsabilidad*, cap. 4, se escribe:

$$
J=1-\sum_i |R_i^*-\alpha_i|
$$

y se afirma que `J<0` es imposible sólo porque `R_i^*, α_i ∈ [0,1]`. El libro incluye después un resultado `J = −0.632`. En efecto, con `R*=(0.9,0.1)` y `α=(0,1)`, se obtiene `J=−0.8`. **El enunciado de imposibilidad es falso con esas hipótesis**; no es razón para eliminar el índice. Revisar sus propiedades y límites verdaderos según la clase de vectores permitidos.

### N-05 — Isomorfismo de operaciones vs. identidad de implementaciones

**[P; derivación por explicitar]** El isomorfismo atribuido a operaciones interna y exterior, así como las correspondencias entre dominios, debe formalizarse precisando **objetos, relaciones y correspondencias conservadas**. No exige que todos los resultados numéricos coincidan, ni supone de antemano que un mismo autovector sea la definición del isomorfismo. Se estudiará la conservación de la **función atributiva** y su estructura, sin afirmar «teorema» hasta demostrar las condiciones requeridas.

### N-06 — Elección de herramienta matemática bajo condiciones

**[R: criterio metodológico]** Perron–Frobenius, Banach, Itô y Shapley son herramientas **candidatas**, nunca el fundamento ontológico mismo. Una propiedad —por ejemplo, proporcionalidad, invariancia, sensibilidad a la sustitución o aditividad— no pertenece en exclusiva al teorema usado para obtenerla. Cada herramienta requerirá: (i) propiedad deseada; (ii) hipótesis explícitas; (iii) prueba de que la herramienta la realiza; (iv) comparación con otras soluciones; (v) límites.

### N-07 — Convergencia dirigida hacia el evento

**[P/V]** La estructura causal discriminada debe conservar la referencia al sumidero o evento `D`. En particular, la centralidad de una red sin condición sobre `D` no queda convertida por simple normalización en una contribución causal atribuible a `D`. Véase el cotejo previo en [puente aritmético-espectral](puente_aritmetico_espectral_prometeo.md). El operador definitivo todavía no está seleccionado.

## 6. Inventario inicial de candidatos para la axiomatización

**No aprobados todavía como axiomas.** El primer trabajo formal será determinar si son definiciones, axiomas independientes, consecuencias o requisitos del instrumento.

| ID provisional | Propiedad/cuestión | Fuente o situación |
|---|---|---|
| A-C01 | Relatividad de la atribución a un evento discriminado. | *Areópago*: especificidad causal. |
| A-C02 | Separabilidad entre causalidad del acto y reconocimiento subjetivo de autoría. | *Sobre la pasión* y *Areópago*: doble mediación y atribución exterior. |
| A-C03 | Reconstruibilidad y trazabilidad de relaciones respecto de evidencia declarada. | *Areópago* y apéndice B de *El cálculo*. |
| A-C04 | Evaluabilidad contrafáctica de la sustituibilidad, sin confundir sustitución de ocupante con eliminación del diseño. | *Areópago*: jerarquía diseño/ejecución. |
| A-C05 | Comparabilidad tipada de contribución y consecuencias soportadas antes de restarlas. | *El cálculo*: `R*`, `S`, `α`, `Δ`. |
| A-C06 | Imputabilidad causal del acto de imputar y de sus consecuencias, sin descolapso retrospectivo. | *Areópago*: cap. 11; ontología del colapso. |
| A-C07 | Invariancia de las relaciones esenciales bajo cambios admisibles de representación o nombres entre dominios. | *Areópago* y capítulo del isomorfismo en *El cálculo*. |
| A-C08 | Propiedad de ordenación por posición causal antes o sin cardinalizarla. | *Areópago*: proporcionalidad y jerarquía causal. |

## 7. Ficha que se utilizará para cada operación

Cada nueva propuesta o normalización se agregará con los siguientes campos:

1. **Enunciado y estado** (C/D/P/V/R), con fuente exacta y pasaje.
2. **Qué pretende hacer**, explicado sin introducir anticipadamente una técnica matemática.
3. **Objeto y tipos de entrada/salida** (evento, nodo, evidencia, tiempo, unidad, dominio).
4. **Propiedades exigidas** y propiedades que **no** debemos suponer.
5. **Fórmulas textuales** de los libros, distinguidas de abreviaturas propias.
6. **Derivación o prueba**, con hipótesis; o un contraejemplo de una propiedad incorrecta.
7. **Ejemplo de control**, exclusivamente como test y no como contenido axiomático.
8. **Herramientas candidatas** y condiciones bajo las cuales sirven.
9. **Decisión de normalización** y texto potencial para el libro axiomático, sólo una vez resuelto.
10. **Impacto aguas abajo** sobre metrología, taxonomía, cálculo aplicado y software, sin editar esos instrumentos prematuramente.

## 8. Próximo punto lógico del estudio

La primera operación a formalizar será **la discriminación de un acontecimiento y la dependencia respecto de él de la atribución**. A partir de ese objeto, se podrán estudiar la estructura de nodos y aristas y las propiedades que debe satisfacer el cálculo de convergencia. Los ejemplos de expedientes servirán para verificar que las expresiones hacen lo que se pretende, no para imponer valores al libro de axiomas.

**Regla de continuidad:** ningún descubrimiento se trasladará automáticamente al manuscrito publicable. Primero quedará explicado y cotejado en este cuaderno; luego se determinará si corresponde a una definición, axioma, proposición, teorema, corolario, nota editorial o herramienta complementaria.

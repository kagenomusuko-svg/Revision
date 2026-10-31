# Cuaderno de reconstrucción axiomática y normalizaciones epistemológicas

> **Diagnóstico técnico vigente (31-10-2026):** [Revisión del estado axiomático tras los acuerdos](revision_del_estado_axiomatico_tras_acuerdos_2026-10-31.md). Sus criterios de convergencia, alcance lógico y prioridades sustituyen las interpretaciones incompatibles de las secciones históricas de este cuaderno. No se modifica el canon.

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
| Convergencia `R*` | Grado de convergencia del nodo hacia la **atribución del evento `D`** bajo criterios y evidencia declarados; no cuota de una responsabilidad total. | [V] Precisar escala y operador, sin asumir suma 1 entre nodos ni identificar un autovector normalizado con fracción de daño. |
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


---

## 9. Diagnóstico inicial de deudas para la axiomatización (31-10-2026)

**Estatus general:** inventario razonado de problemas a resolver, no axiomas aprobados. El objetivo no es desautorizar postulados ontológicos sino precisar el tipo matemático, las hipótesis y la deducción de cada instrumento. Esta sección establece la **secuencia de dependencias** para la reconstrucción.

### 9.1. Deudas fundacionales / orden obligatorio

**DA-01 — Cotejar estructuras ya presentes antes de agregar notación nueva. [Rectificado 31-10-2026]**  
La propuesta original de introducir una firma o tupla general de investigación **no quedó justificada por una necesidad operativa ni por un pasaje canónico específico**. Se retira como requisito previo. Partir de las operaciones que ya aparecen en los libros: $G=(N,E,W)$, las distintas definiciones de $R^*$, $S$, $\alpha$, $\Delta$, y las mediaciones; examinar qué hace cada una, cuál es su propósito canónico, qué propiedades necesita y qué se puede demostrar con la notación ya existente. **Sólo** introducir tipos, estructuras o símbolos nuevos si resuelven un problema matemático concreto que no pueda expresarse adecuadamente con los actuales.

**DA-02 — Formular el puente entre doble mediación y atribución exterior. [Crítica, P/V]**  
*Sobre la pasión* y *Areópago* distinguen $\varphi_1$, $\varphi_2$, $\delta_{\rm int}$ y $\delta_{\rm ext}$. Se necesita una construcción que identifique **qué relación conserva** la atribución interior/exterior, sin exigir que la experiencia egoica, la atribución probatoria y el resultado escalar sean idénticos. La fórmula ontológica
$$
\delta_{\rm int}(t)=\varphi_2(\varphi_1(v_t,c_t),I(t))-I(t)
$$
y
$$
\delta_{\rm ext}(t)=\operatorname{atribución}(\varphi_1(v_t,c_t),\mathrm{Sujeto})
$$
no tienen necesariamente el mismo tipo matemático de salida. Para comparar con $>$, $<$ o $=$, formular el morfismo, medida o criterio de comparación **sin identificar** $\delta_{\rm int}$ con $dEgo/dt$ ni imponer que la segunda mediación sea un número.

**DA-03 — Elegir el tipo de integral que realiza el canon. [Crítica, P/V]**  
La *Axiomatización* existente, Parte II, usa integral de Bochner $\int c(t)w(t)\,dt$ en Hilbert, actualización $\varphi_2$ binaria y, para eventos puntuales, una delta de Dirac tratada como función de peso. *Caelus* utiliza una medida ontológica autorreferente y una representación Lebesgue–Stieltjes con saltos. Es preciso distinguir qué representación preserva las trayectorias asumidas y qué hipótesis concretas requiere cada una. **No se descarta la integral.** Se estudia el espacio de integración, la medida, la dependencia de la historia, la incorporación de saltos y la relación entre incremento por ciclo y derivada temporal. Una delta de Dirac no es una función ordinaria acotada: la formulación discreta requiere tratamiento de medidas/masas puntuales o una representación por sumas.

**DA-04 — Examinar exclusivamente el teorema vectorial añadido, sin alterar la irreversibilidad ontológica. [V; corrección de encuadre]**  
El teorema 2.1 de la *Axiomatización* epistemológica deduce $\|\int_{t_1}^{t_2}c(t)w(t)\,dt\|>0$ a partir de que $c$ es no nula en un conjunto de medida positiva y $w>0$. En espacios vectoriales esa conclusión no se sigue por posibles cancelaciones algebraicas: éste es un **problema del teorema matemático declarado**. No se sigue de allí que un acontecimiento se revierta, desaparezca, deje de haber ocurrido, ni que el canon deba exigir crecimiento estricto, inyectividad temporal o inexistencia de cancelación entre valores. **La irreversibilidad del colapso no está en revisión.** Corresponde corregir, retirar o condicionar el teorema epistemológico en los términos exactos que se pretenda probar; no añadir obligaciones ontológicas nuevas. La representación integral del ego se examinará por las funciones que el canon le asigna, no por una propiedad ajena introducida desde el instrumento.

### 9.2. Deudas relativas a convergencia y sustituibilidad

**DA-05 — Axiomatizar convergencia sin presupuesto de reparto total. [Crítica, P/V; rectificada 31-10-2026]**  
El autor precisa que **el método no mide causalidad qua causalidad ni responsabilidad qua responsabilidad; mide convergencias de nodos hacia la atribución de un evento discriminado**. Es incorrecto tomar $R_D(i)$, por definición, como cuota de un total de responsabilidad igual a 100 %. Se exige referencia al evento, criterio de convergencia explícito, relación con el expediente, sentido de escala y sensibilidad a condiciones de investigación; **no se impone $\sum_i R_D(i)=1$**. Si eventualmente se expresa el índice individual en $[0,1]$, el 1 representa su extremo convencional de convergencia y no «el 100 % del evento causado por este nodo». Dos nodos podrían alcanzar alta convergencia respecto del mismo acontecimiento sin reparto forzoso. Definir cuándo una operación produce un **índice individual**, cuándo un **ranking comparativo** y cuándo una **distribución de cuotas**; son tres resultados matemáticos distintos. Las cuotas restaurativas, si se requieren, son operaciones posteriores y no redefinen $R_D$. Perron–Frobenius o la suma de caminos podrán ser herramientas candidatas, no fundamentos de una conservación que el método no postula.

**DA-06 — Distinguir hecho ocurrido, relación causal y estado probatorio del expediente. [P/V; precisión de encuadre]**  
Un daño, un suicidio o una lesión **no aparecen ni desaparecen según el expediente los conozca o los demuestre**. Una atribución o ausencia de prueba tampoco altera retroactivamente un colapso. *El cálculo*, apéndice B, propone pesos sobre relaciones investigadas; la deuda consiste en declarar **qué permite afirmar o cuantificar la evidencia**, no en decidir si los acontecimientos existen. Distinguir: (1) acontecimiento ocurrido; (2) relación causal que puede o no haberlo producido; (3) lo que el investigador ha logrado reconstruir acerca de esa relación. Una arista no acreditada no es por ello ontológicamente inexistente; una relación con peso numérico provisional cero no demuestra ausencia causal. A su vez, la mera ocurrencia acreditada del daño no prueba automáticamente la conexión causal específica con cualquier nodo investigado. La calibración debe expresar los límites de la **inferencia y el resultado del método**, nunca borrar los hechos. Evaluar por separado la fuerza probatoria de un documento y la fuerza causal del acto que documenta.

**DA-07 — Contrafáctico de sustituibilidad. [Crítica, P/V]**  
El objeto de la sustitución es el **ocupante de una posición conservando el marco pertinente**, no una eliminación arbitraria de la fila de una matriz. Deben declararse: conjunto de reemplazantes admisibles, invariantes del campo, horizonte, variable de resultado y criterio de «mismo resultado» o «mismo tipo de resultado». La *Axiomatización*, Parte III, ofrece $S_{\rm op}$ mediante razón de normas y $S_{\rm est}=1-D_{\rm KL}(R^*\|R^{*(i)})/\log m$. Estas no miden por definición la misma pregunta contrafáctica; su puente monótono requiere demostración independiente.

**Contraejemplo formal para revisar $S_{\rm est}$ [D]:** no vale en general $D_{\rm KL}(P\|Q)\le\log m$ para distribuciones con $m$ estados. Para $P=(0.9,0.1)$, $Q=(0.01,0.99)$ y $m=2$, $D_{\rm KL}(P\|Q)\approx3.82>\log 2$. Por tanto $1-D_{\rm KL}/\log m$ puede ser negativo. Si $Q_i=0$ donde $P_i>0$, la divergencia es infinita. Se requiere revisar intervalo, normalización y justificación de la divergencia para esta tarea.

**DA-08 — Descuento de sustituibilidad y atribución estructural condicional. [D/P; precisión de alcance]**  
La fórmula epistemológica $R_{i,\mathrm{neta}}=R_i(1-S_i)$ implica la identidad $R_i=R_i(1-S_i)+R_iS_i$. Es una **descomposición algebraica del puntaje**, no una descarga de responsabilidad de un sujeto en otro. La responsabilidad causal de un acto se determina por sus propias relaciones, no por cuánto soportan otros sujetos. Si un caso requiere atribuir una contribución de diseño y otra de ejecución, el procedimiento deberá acreditarlas sin doble conteo; **no se impone transferencia automática ni conservación interpersonal de cargas como fundamento universal**. Toda regla adicional de reasignación deberá justificarse en el evento particular y no inferirse de la sola sobreasunción.

### 9.3. Repercusiones, daños, beneficios y restauración

**DA-09 — Diferenciar $\varphi_2$, $\alpha$ y consecuencias efectivamente soportadas. [Crítica, P/V]**  
La asunción egoica es reconocimiento constitutivo; las consecuencias materiales pueden recaer sobre un sujeto que no reconoce la imputación. El libro aplicado contempla «asunción forzada». Definir la base cuantitativa de repercusión y separarla de aceptación interior y de reparación voluntaria. Para comparar contribución $C_i(D)$ y carga soportada $A_i(D)$, fijar **el mismo referente, horizonte y escala**; $C_i-A_i$ sólo es interpretable si existe correspondencia comprobable entre magnitudes. No reemplazar silenciosamente la fórmula editorial $\Delta=R^*-\alpha$ por otra: considerar expresiones bruta y neta, determinar el alcance de cada una y tomar una decisión documentada.

**DA-10 — La sobreasunción es asimetría repercusiva y no condición fundante de causalidad. [D/V; corrección de encuadre]**  
La comparación $\Delta_i=C_i-A_i$ (con escalas declaradas) señala sobreasunción si $A_i>C_i$. **No exige** que exista otro sujeto con déficit ni que alguien haya «descargado» su responsabilidad sobre el primero. El hecho causal original y su pertenencia están establecidos independientemente de la carga que cada sujeto soporte. El signo de $\Delta_i$ no crea ni traslada la responsabilidad original. La *Axiomatización* epistemológica, Proposición 5.2, contiene una **afirmación suplementaria**: si $\Delta_i<0$ con grafo completo, existiría $j\ne i$ con $\Delta_j>0$. Esa afirmación no se deduce de las hipótesis allí declaradas: $R^*=(0.5,0.5)$, $\alpha=(0.8,0.5)$ producen $\Delta=(-0.3,0)$ sin déficit ajeno. La corrección editorial debe **desvincular la definición de sobreasunción de cualquier transferencia forzosa**; el mecanismo de descarga o externalización institucional será objeto de una investigación adicional únicamente cuando haya evidencia de que sucedió. No debe elevarse esa inferencia suplementaria a axioma general del método.

**DA-11 — Propiedades efectivas de $J$ y dependencia de la normalización. [Alta, D/V]**  
En *El cálculo*, cap. 4, la fórmula $J=1-\sum_i|R_i^*-\alpha_i|$ convive con la afirmación «$J<0$ imposible» y ejemplos posteriores con $J<0$. Contraejemplo documentado en N-04. **Además**, si la convergencia no es una cuota normalizada de una totalidad causal, deben reexaminarse la interpretación y las cotas de cualquier indicador global que dependa de $\sum_i R_i^*=1$. No eliminar el índice anticipadamente: reconstruir qué quiere medir y cuáles condiciones permiten agregarlo, sin inferir un 100 % de responsabilidad general.

**DA-12 — Delta del daño y su dimensionalidad. [Alta, V]**  
El libro propone $D_{\rm total}=T_{\rm invertido}+T_{\rm impedido}+\Delta T_{\rm trayectoria}$ y una representación contrafáctica por diferencias de trayectorias. Para una suma legítima, cada sumando ha de expresarse en **la misma unidad** o convertirse explícitamente. Si un salto $X(t_0^-)-X(t_0^+)$ mide unidades de $X$ y una integral $\int (X^{(0)}-X^{(1)})\,dt$ mide unidades de $X\cdot\mathrm{tiempo}$, **no se pueden sumar sin definir qué significa $X$ o cómo se convierten**. Separar pérdida inmediata, flujo impedido y futuro no superpuesto; fijar horizonte y descuento con hipótesis declaradas.

**DA-13 — Beneficio, apropiación y *debitor*. [Alta, P/V]**  
Distinguir el beneficio recibido, el beneficio producido, su procedencia causal y lo efectivamente revertido. Una «delta del aprovechamiento» requiere base de comparación explícita. El ajuste *debitor* necesita regla de correspondencia entre contribución, daño, aprovechamiento y restauración; **no confundir** cálculo de daño con decisión de exigibilidad. La restauración puede ser estructural, y la deducción fiscal un medio complementario, no la definición del ajuste.

### 9.4. Propiedades transversales y de demostración

**DA-14 — Isomorfismos: definir estructura y preservaciones. [Alta, P/V]**  
Distinguir tres afirmaciones: (i) correspondencia interior/exterior de la atribución; (ii) isomorfismo de los métodos entre dominios; (iii) identidad de algoritmos numéricos. No equivalen. Formalizar funciones de traducción, qué diagramas conmutan, qué propiedades se preservan y bajo qué transformaciones. La recurrencia de un eigenvector en tres ejemplos es evidencia de **mismo procedimiento**, no demostración de isomorfismo de objetos.

**DA-15 — Demostraciones y dominio de herramientas. [Alta, V]**  
Perron–Frobenius, Banach, Shapley, Itô, Pinsker, Davis–Kahan, softmax y modelos de Markov sólo tendrán lugar donde satisfagan el contrato de la operación. La *Axiomatización*, Parte VI, combina nodo sumidero con fila nula, hipótesis de irreducibilidad y afirmación de estocasticidad global; estas condiciones no coexisten de la forma invocada. No convertir la regularización que agrega aristas ficticias en «evidencia» del expediente. Reexaminar cada hipótesis antes de mantener los enunciados de existencia, unicidad y convergencia.

**DA-16 — Consistencia de tipos y definiciones. [Alta, V]**  
Evitar $RSC(t)\setminus I(t)$ cuando $RSC(t)$ es un conjunto e $I(t)$ un vector integral, y $A_D\cap I(t)$ con esos mismos tipos. Definir el **conjunto de eventos efectivamente asumidos** por separado de su agregado integral. Para comparar derivadas, valores en espacios funcionales y proporciones, declarar la aplicación de medida que los convierte a una escala comparable. Distinguir identificación de nodos con voluntad de nodos instrumentales sin voluntad.

**DA-17 — Alcance del conocimiento y niveles de resultados, sin negación de hechos no observados. [P; precisión de encuadre]**  
Una reconstrucción causal es relativa a su evento, expediente y condiciones de investigación; eso no implica que la realidad causal dependa de la investigación. Se distinguirán conclusiones sobre relaciones acreditadas, orden parcial de intervenciones, intervalos y cuotas justificadas. La ausencia de prueba de una relación específica sólo limita lo que **podemos imputar sustentablemente en ese expediente**; no elimina el acontecimiento ni permite concluir que la causalidad desconocida sea nula. La completitud de un grafo es una propiedad relativa al modelo y al alcance de la investigación, no una declaración de conocimiento exhaustivo de todos los hechos del mundo.

## 10. Primera secuencia de reconstrucción recomendada

La estructura de precedencias es:

1. **Bloque A — Lenguaje y objetos:** $D$, tipos de nodos, actos, relaciones, prueba, atribución; relación con $\varphi_1$ y $\delta_{\rm ext}$. Resolver DA-01, DA-02, DA-16.
2. **Bloque B — Trayectoria y actos:** $\varphi_2$, integral del ego, incrementos por ciclo, la distinción de medidas y la corrección de los teoremas integrales añadidos. Resolver DA-03, DA-04 sin exigir nuevas propiedades a la irreversibilidad canónica.
3. **Bloque C — Convergencia y contrafactuales:** propiedades mínimas de $W$, $R_D$, definición contrafáctica de sustitución, tratamiento de instrumentos y, sólo cuando la investigación lo justifique, atribución entre diseño y ejecución. Resolver DA-05 a DA-08.
4. **Bloque D — Repercusión:** identificación matemática de las consecuencias soportadas, asimetría, déficit, exceso, comparabilidad y señales de inversión. Resolver DA-09 a DA-11.
5. **Bloque E — Daño, beneficio y restauración:** $\Delta D$, $\Delta B$, $AD$, conservación donde proceda, irreversibilidad de daños y exigibilidad separada. Resolver DA-12, DA-13.
6. **Bloque F — Metateoremas:** isomorfismos, criterios de existencia/consistencia, estabilidad, incertidumbre, selección de herramientas y ejemplos de control. Resolver DA-14, DA-15, DA-17.

**Criterio de salida para una operación:** firma de dominio/codominio; definición ligada al canon; axiomas mínimos; al menos una demostración o construcción correcta; caso que cumple y contraejemplo que detecta una afirmación excesiva; condiciones de uso y límites. Si una operación no posee todavía una realización numérica, puede quedar axiomáticamente caracterizada mediante sus propiedades sin fingir que ya existe una medición cardinal validada.

**Decisión de enfoque:** el primer capítulo de investigación será **evento discriminado, acto, nodo, relación y atribución exterior**, no «Teorema de Perron–Frobenius». El libro final podrá omitir los ejemplos explicativos desarrollados en este cuaderno.


## 11. Rectificación de imputaciones indebidas al canon (31-10-2026)

Esta nota corrige el **encuadre del diagnóstico anterior**, no los textos ontológicos:

1. **Irreversibilidad:** una integral que vuelve a un valor anterior no descolapsa acontecimientos. La fórmula ontológica no debe ser obligada a satisfacer una inyectividad o monotonicidad no postulada. Sólo se audita la afirmación específica del teorema 2.1 de la *Axiomatización*.
2. **Sobreasunción:** que un nodo soporte consecuencias por encima de su contribución atribuible constituye una asimetría de repercusión. **No supone**, por definición, que otra persona haya descargado su responsabilidad, ni funda causalidad donde no existía. La inversión institucional y el déficit de terceros requieren sus propias reconstrucciones.
3. **Prueba y existencia:** una herida, una muerte y todo acto ya ocurrido mantienen su realidad independientemente de su acreditación. Lo que cambia es la **atribución que el expediente puede justificar**. El método no debe etiquetar «inexistente» un evento porque no logró acreditarlo; tampoco puede afirmar una relación causal concreta sin el soporte exigido para la conclusión.
4. **Regla de trabajo:** antes de señalar una «deuda ontológica», localizar el postulado canónico exacto que la exige. Si la exigencia aparece sólo en el libro epistemológico, anotarla como deuda de ese **instrumento o demostración**, no de la ontología. Evitar introducir condiciones adicionales para satisfacer teoremas conocidos.

Estas correcciones sustituyen la lectura anterior de DA-04, DA-06, DA-08, DA-10 y DA-17 y tienen prioridad sobre los enunciados previos del cuaderno cuando entren en conflicto.


## 12. Caso de control: gerente bancario y sobreasunción favorable (31-10-2026)

**[R: precisión conceptual incorporada por el autor; P: notación operativa]**

**Supuesto:** una sucursal cumple y supera la meta de ventas de seguros. El superior felicita al gerente por «todos los seguros que vendiste»; el gerente acepta con satisfacción una atribución referida al resultado de la sucursal aunque no haya ejecutado personalmente todas las ventas.

**Qué establece el ejemplo:**

1. El evento discriminado —ventas realizadas por la sucursal— es real y está separado de los actos de atribuir y aceptar el reconocimiento.
2. El gerente puede **sobreasumir favorablemente** (reconocimiento por producción colectiva); la sobreasunción no requiere daño, sanción, aceptación de culpa, coacción o sufrimiento.
3. El reconocimiento recibido o aceptado **no determina** por sí mismo la cantidad ni la clase de contribución causal del gerente. Su papel de diseño, capacitación, dirección, metas o infraestructura debe investigarse separadamente de **quién ejecutó cada venta**.
4. La sobreasunción **no demuestra** que otro nodo esté en déficit ni identifica a quién corresponden las contribuciones restantes. Tampoco traslada causalidad por aceptación voluntaria de méritos.
5. Las asunciones de mérito pueden solaparse: el gerente y los vendedores pueden atribuirse simultáneamente el éxito colectivo. **No existe un axioma general de conservación de asunción** ni una suma obligatoria de asunciones igual a uno.
6. Una contribución de dirección y una de ejecución pueden coexistir sin que sean idénticas. El **tipo de resultado investigado** (ventas ejecutadas individualmente / resultado comercial colectivo / diseño de condiciones que favorecieron el resultado) determina qué propiedad se está contrastando.
7. La repercusión o asunción efectiva puede ser favorable, desfavorable o neutra; la medición de méritos aceptados, consecuencias impuestas, daños soportados y beneficios recibidos no puede confundirse por compartir la palabra «asunción».

**Ejemplo de control, no axioma:** si hubo 100 ventas, el gerente ejecutó 5 y acepta como propias las 100, la diferencia en el **ámbito de ejecución directa** es $5-100=-95$. El número **no calcula** su contribución a la estrategia comercial de la sucursal y **no identifica** a quienes efectuaron las 95 ventas restantes; eso requiere expediente. Sólo es legítimo realizar la comparación si ambos números se refieren al **mismo atributo** (ventas personalmente realizadas / ventas personalmente asumidas), no a magnitudes heterogéneas.

**Consecuencia para DA-09 y DA-10:** la definición general de sobreasunción es una **comparación relativa al evento y al atributo examinado**, no un mecanismo distributivo. La sobreasunción puede darse por atribución favorable voluntaria o por consecuencias adversas impuestas. Será necesario precisar si la misma letra $\alpha$ puede codificar estas manifestaciones sin perder información, o si el aparato de medición debe distinguirlas como coordenadas/modalidades de un objeto repercusivo más amplio. **No se aprueba todavía una nueva fórmula ni se altera la ontología.**

**Regla de auditoría:** ante cualquier exceso de asunción, no preguntar automáticamente «¿a quién se descargó la responsabilidad?», sino primero «¿qué resultado fue asumido, qué tipo de participación se atribuye y qué participación muestra el expediente?». La eventual distribución de otros nodos pertenece al análisis causal independiente.


## 13. Rectificación principal: el índice R mide convergencias, NO cuotas de responsabilidad total (31-10-2026)

**[R: aclaración expresa del autor sobre el objeto del método; P/V: formalización matemática aún por construir]**

### 13.1. Afirmación de alcance que debe prevalecer sobre el uso anterior de R*

**El método NO calcula causalidad qua causalidad. NO calcula responsabilidad qua responsabilidad. Estudia la convergencia de los nodos hacia la atribución causal de un EVENTO discriminado mediante las relaciones y evidencia investigadas.** La causalidad y responsabilidad totales no se postulan como masas conocidas, cerradas y disponibles para reparto exhaustivo.

No está justificada, como axioma ontológico ni epistemológico general, la igualdad
$$
\sum_{i\in N_D}R_D(i)=1.
$$

Si se usa una escala individual $R_D(i)\in[0,1]$, el extremo de esa escala **no** debe confundirse con propiedad o fracción del 100 % de la causalidad del evento. Por ello, varias convergencias pueden ser simultáneamente elevadas: la convergencia relativa a un acontecimiento no está por definición regida por una suma conservativa entre nodos. Tampoco se adopta el axioma opuesto «la suma nunca puede ser uno»: puede coincidir con uno accidentalmente o por convención de un análisis particular, sin que sea ley general.

**Cuidado:** el índice de convergencia tampoco se identifica de antemano con una probabilidad estadística $P(i\text{ causó }D)$; su definición, sus extremos, orden y escala deben justificarse por la operación propuesta.

### 13.2. Caso de control documental: expediente Madoff de la biblioteca

*Expediente EP-1777319755497*, «Fraude piramidal institucional — esquema Bernard Madoff» (27-04-2026), presenta los siguientes **valores producidos por su procedimiento anterior**:
- SEC: «índice de convergencia» 38.10 %;
- Bernard Madoff: 22.63 %;
- Empresas del grupo: 15.48 %;
- Bancos custodios y entidades relacionadas: 13.16 %;
- Feeder funds: 6.86 %; modelos y reportes: 3.77 %; inversionistas institucionales: 0.00 %.

El mismo expediente explica su operación: $\mathrm{influencia}(i)$ suma productos ponderados de caminos al nodo final y luego
$$
R_i^*=\frac{\mathrm{influencia}(i)}{\sum_{j\in N_{\rm activos}}\mathrm{influencia}(j)}.
$$
Por ello, los porcentajes **suman 100 % por definición de la normalización**, no por una demostración de que la causalidad de la pérdida global se distribuye como masa de responsabilidad cerrada. **Este hecho revela una deuda del instrumento, no una propiedad del canon.** Los valores se citan únicamente para cotejar el problema semántico/operacional; **no se toman aquí como medidas verificadas de la participación causal histórica de los sujetos**.

La frase del glosario de ese expediente «fracción del resultado total que se explica por la posición del nodo» deberá reconsiderarse: una cuota del puntaje agregado no demuestra una fracción del daño real.

### 13.3. Tres objetos que NO debemos fusionar

1. **Convergencia hacia el acontecimiento:** $R_D(i)$ — correspondencia atribuible del nodo $i$ con $D$ bajo un contrato de investigación explícito. Índice por nodo, no necesariamente aditivo.
2. **Comparación o ranking de convergencias:** orden relativo entre $R_D(i)$ y $R_D(j)$ bajo la misma especificación. No exige cuotas globales ni demuestra que el máximo sea «culpable» o que haya producido cierta fracción material del daño.
3. **Distribución restaurativa de una magnitud definida:** si un daño cuantificado y una regla de reparto aplicable justifican cuotas que sumen una cantidad determinada, será una **operación posterior y distinta**. Que ese reparto sume un daño medido no convierte $R_D$ en una partición de la causalidad.

Por tanto, las interpretaciones de $R^*$, $S$, $\alpha$, $\Delta$, $J$, $\mathrm{AD}$ y las notas anteriores que presupongan «una masa global de responsabilidad» deben cotejarse contra este criterio antes de entrar en la axiomatización.

### 13.4. Deudas matemáticas concretas, correctamente encuadradas

**DC-01 — Definir el estimando de convergencia.** Precisar qué significa «se acerca a la atribución del evento» para cada nodo, cómo se ordena o cuantifica y bajo qué condiciones un valor extremo es admisible. No convertir un índice de cercanía en probabilidad ni en fracción de daño sin demostración independiente.

**DC-02 — Separar escala individual de normalización colectiva.** Llevar cada índice al intervalo $[0,1]$, si corresponde, no requiere dividirlo entre la suma de índices. La normalización $R_i=r_i/\sum_jr_j$ altera la interpretación: produce una **cuota relativa del puntaje** y obliga a suma uno aunque nada demuestre un reparto exhaustivo de causalidad.

**DC-03 — Evitar perturbaciones de significado por agregar actores.** Una cuota colectiva disminuye si se agrega otro nodo de puntaje positivo aunque no se modifique la relación del nodo original con el evento. Determinar qué tipo de dependencia contextual entre nodos sí exige la convergencia causal y cuál es mero efecto del denominador de normalización.

**DC-04 — Comparación repercusiva sin hipótesis de suma cero.** Si la asunción de méritos y de consecuencias no requiere conservación global, $\Delta_i=R_D(i)-\alpha_i$ se interpretará sólo con ambos términos en escalas comparables y respecto del mismo atributo/evento, **sin inferir déficits de terceros ni un reparto universal de cargas**.

**DC-05 — Condiciones de uso de técnicas de centralidad.** La centralidad normalizada, el autovector de Perron, Shapley y la suma de caminos no definen por su nombre la convergencia que busca el método. Se examinarán sólo después de formular las propiedades de $R_D$.

### 13.5. Prioridad de reconstrucción corregida

**La primera definición matemática pendiente es «índice de convergencia de un nodo respecto de un evento discriminado» sin presupuesto de normalización a una masa total.** A partir de esta definición se podrá especificar $W$ y el contrafáctico de sustituibilidad y después revisar las operaciones repercusivas y restaurativas.

**Advertencia editorial:** esta rectificación prevalece sobre pasajes previos del cuaderno que llamen a $R^*$ «distribución de responsabilidad», «fracción del resultado», «porcentaje material del daño» o postulen conservación/reasignación como reglas generales. Se conservan las expresiones publicadas como objetos a cotejar, no como afirmaciones automáticamente aprobadas.


## 14. Límite epistémico de la convergencia y prohibición de inferencia normativa automática (31-10-2026)

**[R: delimitación del autor; P: fórmulas y condiciones futuras]**

**Premisa rectora declarada por el autor:** la investigación no accede a «la causalidad *qua* causalidad» ni, por consiguiente, calcula «responsabilidad *qua* responsabilidad». El método examina **convergencias atribuibles hacia un acontecimiento discriminado** a partir de la reconstrucción de relaciones y la evidencia disponible. La elección de un grafo no acredita que éste contenga el conjunto de todas las condiciones causales del acontecimiento. El acontecimiento no depende de ser conocido por el investigador; las imputaciones fundamentadas sí dependen de lo que puede reconstruirse.

### 14.1. Distinciones obligatorias

1. **Evento ocurrido:** $D$ no se produce ni desaparece según el analista lo represente.
2. **Relaciones causales reales:** no se presupone que sean completamente cognoscibles o enumerables en el expediente. No se afirma tampoco, sin prueba, que no exista causalidad objetiva.
3. **Reconstrucción causal:** $G_D$ es una representación investigativa con criterios, alcance, fuentes y convenciones declaradas. La completitud relativa al expediente no implica completitud causal absoluta.
4. **Convergencia:** $R_D(i;G_D,\mathcal E_D,\mathcal K_D)$ se refiere a la atribución de un evento **en las condiciones del procedimiento**. No es por definición la probabilidad de que $i$ haya causado $D$, una fracción ontológica del acontecimiento ni una cuota de responsabilidad total.
5. **Obligación/restitución:** cualquier conclusión normativa o de exigibilidad requiere premisas adicionales; no se deriva automáticamente del índice numérico.

### 14.2. Dos inferencias prohibidas por falta de premisa

**Error epistémico / ontológico:**
$$
G_D \not\Rightarrow \text{«totalidad de la causalidad de }D\text{»}.
$$

**Error normativo («ser» → «deber ser»):**
$$
R_D(i)=r \not\Rightarrow \text{«el nodo }i\text{ debe soportar o pagar la cuota }r\text{»}.
$$

La **guillotina de Hume en sentido estricto** corresponde al segundo paso (*Treatise of Human Nature*, III.1.1: no derivar un «debe» de proposiciones puramente descriptivas sin una premisa normativa). La **cuestión humeana del conocimiento de conexiones necesarias y de la inducción** corresponde a la cautela del primer paso (*Enquiry concerning Human Understanding*, IV y VII). Hay una conexión metodológica entre ambos límites, pero no deben confundirse en el libro. Lecturas de referencia para cotejo filosófico externo: Stanford Encyclopedia of Philosophy, «Hume's Moral Philosophy», §5; «David Hume», sección sobre causalidad.

### 14.3. Consecuencias directas para la axiomatización

- **No universalizar el 100 %:** el evento discriminado puede codificarse como ocurrido ($\chi_D=1$), pero esa convención **no demuestra** que $\sum_i R_D(i)=1$. Son objetos distintos: indicador de ocurrencia y colección de índices.
- **No agotar la causalidad por definición:** «grafo completo» sólo puede significar **completo bajo un criterio explícito del expediente**, nunca prueba de conocimiento exhaustivo de la causalidad universal.
- **No inferir deberes por aritmética:** aunque un operador produjese un número preciso, no determina por sí solo culpabilidad, sanción o cuota restaurativa. El ajuste *debitor* pertenece a una fase ulterior que debe declarar las condiciones de restauración aplicables.
- **No reificar la calibración:** aunque el índice tenga escala porcentual, sus valores son dependientes de la definición del operador y su calibración. Se necesita justificar qué significa «convergencia = 1» o «convergencia = 0» sin interpretar que el nodo «posee» la totalidad del hecho.
- **La precisión de medida no supera el límite de objeto:** un cálculo reproducible y numéricamente estable puede ser útil sin constituir una medida de la totalidad causal.
- **No escéptico radical por defecto:** el límite de inferencia no obliga a concluir que toda relación causal es mera ilusión ni que no puedan formularse atribuciones justificadas. El método conserva finalidad investigativa y criterios explícitos de reconstrucción.

### 14.4. Próxima cuestión formal

Definir el índice de convergencia **como una función relativa a un acontecimiento y a una reconstrucción declarada**, determinar cuáles son sus propiedades necesarias (orden, sensibilidad, invariancia, valores extremos) y separar **ocurrencia de $D$**, **índice de convergencia** y **reparación exigible**. No escoger primero el algoritmo ni usar la normalización como sustituto de esa definición.

**Advertencia sobre material previo:** donde la documentación anterior haya confundido un vector normalizado con la «responsabilidad causal real total» o el valor 1 con exhaustividad ontológica, esta nota corrige aquella inferencia y tiene prioridad en la reconstrucción. No se modifica el canon.


## 15. Criterio de ingeniería para la reconstrucción: función primero, herramienta después (31-10-2026)

**[R — Directriz metodológica expresa del autor; no es axioma ontológico ni teorema matemático]**

La investigación de la axiomatización debe proceder **desde el problema y la función del instrumento hacia sus propiedades**, y sólo después hacia los teoremas, técnicas y algoritmos posibles. No se seleccionará una matemática para imponer luego su estructura al método. La dirección de trabajo es:

$$
\text{problema delimitado}
\;\longrightarrow\;
\text{operación requerida}
\;\longrightarrow\;
\text{propiedades indispensables}
\;\longrightarrow\;
\text{consecuencias demostrables}
\;\longrightarrow\;
\text{herramienta admisible (si la hay)}.
$$

La exigencia de rigor subsiste íntegra, pero se aplica a **la definición de la propiedad, las hipótesis y las inferencias que realmente pueden probarse**, no al prestigio de un teorema o a la conveniencia de un modelo existente.

### 15.1. Prueba de utilidad de cada herramienta

Para cada objeto u operación (incluidos $W$, $R^*$, $S$, $\alpha$, $\Delta$, daño, beneficio y *debitor*), registrar:

1. **Qué pregunta concreta responde** en relación con un evento discriminado.
2. **Qué aspecto del canon realiza**, indicando texto/pasaje y sin añadir presupuestos no expresados.
3. **Qué propiedades matemáticas necesita** para cumplir esa función, cuáles son opcionales y cuáles contradicen su alcance.
4. **Qué resulta lógicamente demostrable**, bajo qué premisas, y qué no puede concluirse.
5. **Qué instrumento propuesto las satisface**, con una construcción y prueba o contraejemplo verificable.
6. **Qué gana y qué pierde** al aplicarlo (sensibilidad al expediente, evidencia, coste de complejidad, interpretabilidad, posible información omitida).
7. **Decisión:** conservar, conservar bajo condiciones, sustituir, crear un operador, o descartar. No rescatar una herramienta por familiaridad o elegancia formal.

**Regla de descarte:** si la operación matemática exige aceptar una propiedad ajena o contraria al canon para funcionar, se **descarta como definición de esa operación**, aunque siga siendo matemáticamente válida en otros dominios. La incompatibilidad no reabre la ontología.

### 15.2. Ejemplo inmediato: convergencia $R_D(i)$

**Necesidad:** investigar hasta qué punto un nodo se aproxima a la atribución del evento $D$ conforme a una reconstrucción contextual y evidencial.

**No se exige:** una masa total de causalidad conocida; sumar 1 entre nodos; equiparar convergencia con causalidad o responsabilidad *qua* tales; que el índice numérico determine culpabilidad o una obligación *debitor*.

**Por examinar:** cómo depende de $D$ y de las relaciones reconstruidas; qué información expresa; qué cambios resultan pertinentes al cambiar evidencia, nodo o campo; qué significa una escala, si existe; qué conclusiones de orden o magnitud pueden sostenerse.

**Consecuencia:** Perron–Frobenius, una suma de caminos, una función de similitud, una medida contrafáctica u otro operador no se adoptarán por su notoriedad: se probará si realizan exactamente esas funciones. La normalización al simplex puede servir para una **comparación de cuotas del puntaje**, pero no es constitutiva ni obligatoria para **convergencia por nodo**.

### 15.3. Distinciones editoriales vinculantes

- **Propiedad necesaria** no equivale a **teorema escogido**: distintas construcciones pueden realizar una misma propiedad.
- **Identidad algebraica** no equivale a **principio ontológico**: una igualdad comprobada entre símbolos no autoriza interpretaciones causales adicionales.
- **Existencia de un valor calculado** no equivale a **validez del índice**: una fórmula puede producir números y no medir el objeto pretendido.
- **Consistencia formal** no equivale a **exhaustividad causal**: los expedientes no agotan el acontecimiento.
- **Resultado descriptivo** no equivale a **obligación normativa**: la reparación, sanción y exigibilidad requieren sus propias premisas.
- **Explicación de ingeniería** no equivale a **contenido de la axiomatización publicable**: los ejemplos, comparativas y decisiones se documentan en este cuaderno; el libro final contendrá solamente las relaciones y pruebas necesarias.

**Primer entregable operativo siguiente:** la ficha de requisitos de la convergencia $R_D$ —pregunta, objetos, relación con el canon, propiedades requeridas/prohibidas, escenarios de verificación— **antes** de escoger un algoritmo y **sin imponer $\\sum_i R_D(i)=1$**.


## 16. Reutilización, composición y creación de herramientas (31-10-2026)

**[R — criterio metodológico acordado; no constituye axioma ontológico ni teorema]**

El propósito de la reconstrucción **no es inventar una matemática** ni obtener originalidad por sí misma. Se utilizarán resultados existentes cuando sirvan a las propiedades requeridas por los postulados, sin comprometer el alcance epistemológico del método. Cuando una herramienta aislada sea insuficiente, se podrá combinar propiedades o procedimientos procedentes de distintas áreas, siempre que sus dominios, hipótesis y resultados sean compatibles. Si tampoco existe una construcción adecuada, se formulará un operador nuevo **únicamente porque resuelve el problema** y se lo someterá a pruebas.

Reglas de admisión:

1. **Reutilizar:** una herramienta conocida que satisface las propiedades requeridas puede incorporarse sin modificación.
2. **Adaptar:** conservar lo útil, modificar los supuestos instrumentales admisibles y demostrar las nuevas propiedades.
3. **Componer:** conectar operaciones de diferentes áreas especificando claramente dominio, codominio, orden de aplicación y condiciones de compatibilidad.
4. **Construir:** definir una operación nueva cuando las anteriores no representen el objeto o no produzcan las conclusiones requeridas; explicitar sus propiedades y demostrar los resultados enunciados.
5. **Descartar:** una construcción matemáticamente impecable pero ajena al objeto investigado no se conserva por elegancia, prestigio o tradición.

Distinguir cuidadosamente **nuevo operador**, **nueva formalización**, **nueva proposición demostrada** y **nueva teoría matemática**: no son equivalentes, y la novedad no se proclamará sin prueba. En cualquier caso, el criterio de éxito es la adecuación operacional al canon y a la pregunta investigativa, con validez lógica explícita.

**Regla editorial:** la explicación de cómo se ensamblaron las herramientas se documenta en el cuaderno; el libro de *Axiomatización* expondrá solamente las definiciones, axiomas, hipótesis y demostraciones indispensables. No añadir al canon propiedades por conveniencia de las herramientas.


## 17. Principio rector: subordinación instrumental de la matemática a la ontología (31-10-2026)

**[R — decisión metodológica explícita del autor; sin modificar el canon publicado]**

> La ontología establece qué es y qué relaciones constituyen el sistema. La matemática no decide el objeto ontológico ni corrige la ontología para ajustar sus estructuras a técnicas disponibles: **operacionaliza el modelo ontológico y formaliza las relaciones que se siguen de él**.

**Jerarquía de trabajo:**
1. **Ontología canónica:** determina los objetos, relaciones, actos, mediaciones y límites conceptuales del sistema. Su contenido publicado no se modifica para acomodar el cálculo.
2. **Axiomatización epistemológica:** especifica los objetos matemáticos y sus tipos; separa definiciones, hipótesis instrumentales, axiomas formalizadores, identidades derivadas y resultados demostrables. Explicita cuál relación del canon pretende representar cada expresión.
3. **Herramientas matemáticas:** se seleccionan, ajustan, componen, crean o descartan por su capacidad para realizar esas operaciones bajo hipótesis verificadas; ninguna propiedad de una herramienta se convierte automáticamente en principio ontológico.
4. **Instrumentación y aplicación:** calibración, investigación de expedientes, grados de convergencia, repercusiones y restauraciones cuando corresponda. La precisión instrumental nunca equivale a conocimiento exhaustivo de la causalidad.

**Criterio para un aparente conflicto:** si una representación matemática no cumple el canon, revisar primero su tipado, las hipótesis, el dominio, el operador y la demostración. Dejar constancia de una limitación no resuelta si aún no existe formalización adecuada. **No trasladar la deuda del instrumento al canon.** Esto no dispensa de rigor: una fórmula sigue siendo inválida si su demostración falla y no se la debe publicar como teorema hasta corregirla.

**Ejemplo de aplicación:** que un vector propio se normalice a suma 1 no hace que el acontecimiento posea una «responsabilidad total» divisible en porcentajes ni que los índices de convergencia tengan que sumar 1. Una identidad formal de normalización no modifica la definición ontológica del objeto investigado.

**Distinción necesaria:** «la ontología establece el objeto» no implica «cualquier fórmula propuesta sobre el objeto está matemáticamente demostrada». La verdad o consistencia matemática de una formalización se somete a su propia prueba; lo que está subordinado es la **selección e interpretación del aparato matemático**, no la exigencia de validez lógica.

**Regla de continuidad editorial:** esta sección prevalece sobre cualquier formulación de la reconstrucción que trate como axioma una convención técnica sólo porque simplifica la aplicación de una teoría conocida. El cuaderno documentará la traducción entre las relaciones canónicas y los instrumentos; el libro de axiomatización presentará las relaciones formales estrictamente necesarias.


## 18. Alcance lógico de la axiomatización y separación de validación empírica (31-10-2026)

**[R — aclaración metodológica expresa del autor; no es axioma nuevo]**

**Objetivo central:** traducir a símbolos y relaciones matemáticas las construcciones lógicas establecidas por la ontología canónica y determinar con rigor **si la formalización es correcta en sus propios términos**. El propósito inmediato **no es demostrar empíricamente la verdad de la ontología ni validar todos los valores que después producirán los instrumentos**; ese trabajo pertenece a etapas ulteriores.

**Niveles que se mantendrán separados:**

1. **Contenido ontológico de partida (canon):** establece el objeto y las relaciones que requieren representación. No se modifica para salvar un modelo.
2. **Formalización y demostración:** construcción de dominios, símbolos, definiciones, hipótesis, axiomas, operadores, identidades, pruebas y contraejemplos; verificación de que las conclusiones se siguen realmente de las premisas. Debe examinar también la **fidelidad de la traducción**: coherencia interna de la matemática no basta si se formalizó un objeto diferente.
3. **Adecuación empírica futura:** evaluación de calibraciones, calidad probatoria, capacidad explicativa, repetibilidad, sensibilidad y correspondencia de resultados con expedientes y fenómenos observados. No confundir una demostración condicional con una validación empírica.

**Criterios de rigor de la fase axiomática:** enunciados sin ambigüedad; dominio y codominio tipados; ausencia de usos incompatibles de un mismo símbolo; hipótesis declaradas; deducciones válidas; consistencia examinada; ejemplos matemáticos de existencia cuando se requieran; separación entre axiomas, teoremas y modelos; identificación de límites y supuestos instrumentales. Una afirmación sobre un caso concreto no se vuelve teorema por usar notación matemática.

**Precisión sobre «si puede pensarse, puede operacionalizarse»:** se adopta como orientación constructiva la búsqueda de una **representación formal** para las relaciones pensadas; no se supone de antemano que toda representación implique computabilidad efectiva, medición cardinal única o identificación empírica. Esa diferencia no bloquea la axiomatización: si un operador todavía no tiene procedimiento numérico, se pueden investigar formalmente sus propiedades y condiciones de existencia, sin inventar resultados.

**Regla de ingeniería:** seleccionar o construir el instrumental mínimo que modele fielmente las relaciones canónicas y que permita derivaciones matemáticamente correctas. La prueba formal verifica una consecuencia **dadas las premisas**; la investigación empírica futura verificará el alcance y utilidad de la representación en fenómenos concretos.

**Ejemplo rector:** si se propone $R_D(i)$ como índice de convergencia hacia la atribución del evento, la axiomatización debe definir su estructura y deducir las propiedades que verdaderamente se siguen. No debe imponer $\\sum_iR_D(i)=1$ por facilidad técnica ni declarar probado, por obtener un número, que se agotó la causalidad de $D$.

**Decisión editorial:** las pruebas formales necesarias van en la *Axiomatización*. Los debates sobre su origen ontológico, pruebas de ingeniería, calibraciones, expedientes y verificación empírica futura se documentan aquí o en los instrumentos epistemológicos correspondientes.


## 19. Retirada de formalización preliminar innecesaria (31-10-2026)

**[R — corrección a instancia del autor]** En la revisión del estado se había propuesto la tupla $\mathcal I_D=(D,N_D,\Gamma_D,\mathcal R_D)$ y una relación nueva $N_i\preceq_{D,\Gamma_D}N_j$ como etapa inicial. **No se derivaron de un postulado ni resolvían una deuda funcional identificada.** Se retiran como punto de partida. La mención canónica de ordenación de posiciones causales no exige crear una relación de orden independiente: si es necesaria, la propiedad debe surgir de las operaciones investigadas o justificarse por función específica.

Esta corrección se aplica también a la firma $\mathcal C_D$ propuesta provisionalmente en la versión anterior de DA-01: **no es requisito del método**. Ninguna de estas notaciones será trasladada al libro de axiomatización salvo demostración posterior de su necesidad.

**Procedimiento sustituido:** leer la fórmula que ya se propone, localizar su finalidad canónica, comprobar cada operación, sus tipos, hipótesis y consecuencias, y conservar/modificar/descartar según utilidad y rigor. **No inventar andamiajes generales de presentación antes de diagnosticar la función matemática que falta.**

Véase el informe vigente: [revisión del estado axiomático](revision_del_estado_axiomatico_tras_acuerdos_2026-10-31.md), sección 6.

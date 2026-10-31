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

**DA-01 — Especificar qué estructura será axiomatizada. [Prioridad crítica, P]**  
La entidad primaria del método epistemológico es una **investigación relativa a un evento determinado**. Propuesta de firma provisional (sin adoptar todavía un estimador):
$$
\mathcal C_D=(D,N,E,\mathcal E,\mathcal K),
$$
donde $D$ es el acontecimiento seleccionado, $N$ contiene posiciones candidatas a intervención, $E$ relaciones de causalidad propuestas, $\mathcal E$ información probatoria y $\mathcal K$ reglas de discriminación, contexto y contrafácticos admisibles. La firma completa será objeto de revisión. Una imputación no calcula la causalidad universal, sino una **atribución condicionada por $D$, por el modelo y por la evidencia disponible**.

Preguntas de tipado: ¿el resultado $D$ es nodo sumidero o un objeto distinguido? ¿Los nodos representan sujetos, roles, condiciones, actos o todos, con clases tipadas? ¿Qué ocurre si dos actos de un mismo sujeto son nodos diferentes? ¿Cuándo un nodo candidato pasa a «acreditado»? ¿Qué representa una omisión? ¿Cómo se registra una atribución como acto ulterior?

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

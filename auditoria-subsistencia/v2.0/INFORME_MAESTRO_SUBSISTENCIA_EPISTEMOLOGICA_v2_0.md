# INFORME MAESTRO DE SUBSISTENCIA EPISTEMOLÓGICA — VERSIÓN 2.0

**Auditoría sustantiva, corte documental: 30 de octubre de 2026**  
**Estado:** segunda etapa sustantiva parcial; conclusiones proporcionales al material efectivamente examinado.

## Síntesis ejecutiva

Esta etapa realizó comprobaciones matemáticas concretas y cotejó fórmulas contra el código de Prometeo y pasajes completos de los manuscritos. No es una certificación exhaustiva de las 5.643 páginas. Los hallazgos de mayor consecuencia son:

1. **La Proposición 5.2 de M10 es falsa bajo sus hipótesis escritas.** El ejemplo (R^*=(.5,.5),\alpha=(.8,.8)) satisface coeficientes independientes en [0,1] y produce dos déficits negativos en un grafo completo. La prueba introduce una transferencia de asunción que no está entre las premisas. Solo una condición adicional de conservación como \(\sum_i\alpha_i=\sum_iR_i^*=1\) permitiría inferir suma de déficits cero; esa condición no es la declarada.
2. **La arquitectura de matriz de M10 no coincide de manera demostrada con su propio nodo sumidero D.** Si se interpreta literalmente la matriz aumentada con fila final cero, no es estocástica por filas en todas sus filas y el grafo completo no es irreducible. La prueba del Teorema 6 usa \(W\mathbf1=\mathbf1\), lo cual no vale para esa matriz. El teorema requiere especificar si se refiere a submatriz de actores, matriz aumentada u otro operador.
3. **La orientación es material.** En un grafo asimétrico, el eigenvector derecho de \(W\) no coincide con el de \(W^T\). M10 usa \(W^TR^*=\lambda R^*\); M01/M02 y Prometeo describen/ejecutan \(WR^*=\lambda R^*\). No se resuelve por imitación del código: se requiere fijar índices, orientación de aristas y magnitud pretendida.
4. **El Lema 8.1 de M10 falla como está enunciado.** Una matriz estrictamente positiva de filas idénticas permite sustituir una fila sin cambiar el eigenvector, por lo que \(S_{est}=1\) mientras \(R^*(E)>0\), contradiciendo la cota declarada \(R^*(E)\le(1-S)/(m-1)\). El Apéndice D.3 habla de una magnitud neta \(R^*_{net}=R^*(i)-R^{*(i)}_i\); esto puede ser una distinción aclaratoria, pero no vuelve verdadera la cota del lema para el total ni las aplicaciones que usan el total.
5. **La justificación de convergencia en M01 también requiere revisión.** El texto afirma que \(T(v)=Wv/\|Wv\|_1\) es una contracción L1 en el símplex cuando W es primitiva y da \(c=1-\delta(W)<1\). La primitividad no implica contracción estricta en una iteración de ese operador; además, el coeficiente de Dobrushin depende de convención estocástica/orientación. Un contraejemplo primitivo de 3×3 mantiene distancia de variación total 1 entre dos vértices tras una iteración normalizada. Perron–Frobenius sí ofrece existencia/positividad y unicidad del eigenvector positivo para una matriz primitiva; eso no valida esa demostración de Banach ni la semántica causal de R*.
6. **Prometeo no es una transcripción literal de M10.** En el commit `84e8ad0191856bcfd658b472c89266fbe12983a2`, el motor implementa W derecha, conserva pesos empíricos sin normalizar, excluye D del cálculo y trata la acreditación del cierre como compuerta previa. Los tests/CI verifican contratos y regresiones del software, no verdad matemática ni validez causal/empírica.
7. **La base empírica de M10 no valida todavía los teoremas.** Tres casos piloto calibran parámetros con muestra mínima y sin protocolo inferencial reproducible completo en el texto examinado. Los 18 casos de nueve dominios aparecen como revisión de casos con aproximaciones, marcas y narrativas, sin publicación del conjunto íntegro de matrices, codificación y datos que permita reproducir las cotas; son evidencia ilustrativa/estructural, no validación independiente de medición o predicción.
8. **El corpus instrumental sugiere separación de funciones, no una escuela metodológica única.** ECO produce información elicitada; SDO ofrece un vocabulario/lectura de posiciones; HISTOS describe acompañamiento longitudinal; Taxonomía U·1 enruta fuentes documentales o entrevista. Ninguno es requisito matemático para computar una imputación con información suficiente. Sus funciones autónomas merecen evaluación, pero la eficacia clínica no queda acreditada por las autodescripciones.

### Recomendación provisional por resultado

- **REFORMULAR / INVESTIGAR:** R* como índice espectral hasta fijar contrato matemático (orientación, pesos, universo, cierre y validación externa).
- **DESCARTAR en su forma actual:** Proposición 5.2 como teorema general; cota total del Lema 8.1; afirmación de que M01 demuestra contracción de Banach por primitividad sola.
- **INVESTIGAR, no descartar:** Teorema 6, Teorema de Inversión Causal y teoremas 8.1–8.4, porque requieren reparación de hipótesis/pruebas y separar magnitudes; algunos resultados particulares podrían sostenerse bajo condiciones explicitadas.
- **INTEGRAR como documentación modular candidata:** glosario de M04 y protocolos/catálogos taxonómicos; no se justifica todavía conservar cada libro como obra independiente.
- **INVESTIGAR por función independiente:** ECO, SDO e HISTOS. No son necesarios para el cálculo causal común; no se recomienda afirmar eficacia diagnóstica o terapéutica sin validación.

## 1. Objeto, límites y autoridad

Se evalúa subsistencia de aportaciones, no se corrigen libros ni código. La ontología publicada en `publicaciones` se mantiene fija; M10 se trata como fuente epistemológica bajo examen, nunca como canon ontológico. *Arquitectura ontológica de sistemas artificiales* queda fuera. “Imputación causal”, “contabilidad ontológica” y “compliance causal” se tratan como nombres contextuales del mismo método.

PDF originales adjuntos: fuentes prioritarias; se consultaron sus extracciones de texto para localización y lectura. La extracción facilita búsqueda, pero no reemplaza la inspección visual de tablas o notación. Las páginas citadas son paginación impresa cuando el manuscrito la muestra. Prometeo fue inspeccionado por GitHub autorizado a la revisión `84e8ad0191856bcfd658b472c89266fbe12983a2` (rama main, 2026-10-08). `publicaciones`: commit `3e3e93a127c72ca0bc521e88014308d52a12a5a5` (2026-10-29). No se modificó ningún repositorio.

La versión v1.1 contenía afirmaciones residuales de inaccesibilidad de Prometeo y numeración de versión discordante. Esta v2.0 corrige esa descripción: el repositorio privado sí se consultó por el conector GitHub; las observaciones aquí refieren al código y commit indicados.

## 2. Corpus y cobertura efectiva

| ID | Obra | Extensión PDF | Cobertura sustantiva de esta etapa |
|---|---|---:|---|
| M01 | El cálculo de la responsabilidad | 834 pp. | Sección de R* y Apéndice A.1 de Banach examinados; otras fórmulas/casos pendientes de cotejo línea por línea. |
| M02 | La transformación formal | 301 pp. | Pasajes de definición/orientación de R* localizados; derivación integral y correspondencia total pendientes. |
| M03 | Metrología causal I | 498 pp. | Introducción y afirmaciones metrológicas preliminares; inventario de instrumentos no exhaustivo. |
| M04 | Metrología causal II | 183 pp. | Introducción/glosario operativo: función de traducción terminológica; cotejo término-operador pendiente. |
| M05 | Taxonomía General de Aplicaciones | 1.506 pp. | Índice, U·1 y rutas de legibilidad examinadas; trece partes y 78 capítulos no cotejados completos. |
| M06 | SDO | 1.130 pp. | Índice, cinco ejes, seis códigos del eje I y secciones de función/límites examinadas por muestreo. |
| M07 | ECO | 436 pp. | Inicio, propósito, salidas, relación con SDO/Taxonomía/HISTOS; protocolo y fiabilidad pendientes. |
| M08 | HISTOS | 515 pp. | Inicio, finalidad y flujo de entrada/salida; etapas completas, riesgos y resultados no auditados. |
| M09 | Método Prometeo | 113 pp. | Flujo general y límites declarados parcialmente; procedimientos jurídicos concretos pendientes. |
| M10 | Axiomatización doble mediación | 127 pp. | Partes V–VI y VIII, Apéndices A–B: P5.2, Teorema 6, Lemas 8.1/8.2, Teoremas 8.1–8.4 y calibración examinados; sistema entero no verificado línea por línea. |

Cobertura matemática efectiva: ejemplos calculados independientemente y derivaciones locales en el Registro de comprobaciones. No se declara exhaustiva la verificación de todas las pruebas de M10. El registro de cobertura adjunto detalla lo leído, cotejado, comprobado y pendiente.

## 3. Marco ontológico y dependencias

El proyecto establece como doctrina publicada el marco de doble mediación, integral del ego y colapso descrito por los libros ontológicos publicados. En esta auditoría se verifica compatibilidad documental, no se reinterpreta ni certifica su verdad filosófica. Una analogía entre un operador formal y un concepto ontológico no prueba identidad: hace falta un puente semántico operacional.

Dependencia metodológica identificada: el cálculo necesita una representación del expediente (nodos, aristas, pesos, evento final), una regla de cierre/acreditación, una función numérica R*, una medición de asunción α y una regla de comunicación. M10 añade condiciones de grafo y resultados espectrales; Prometeo añade contratos de entrada, rangos, linter, resolución de intervalos y generación de expediente. ECO/Taxonomía/SDO pueden suministrar o estructurar información, pero su necesidad debe establecerse para una aplicación concreta, no por derivación automática.

No se ha demostrado que todos estos elementos se deduzcan de la ontología. Son instrumentos auxiliares legítimos en principio si se explicitan y validan. La compatibilidad conceptual no equivale a derivación matemática.

## 4. Auditoría formal cruzada

### 4.1 P5.2: déficit negativo y existencia de compensador

M10, págs. impresas 34–35: \(\Delta_i=R_i^*-\alpha_i\); los coeficientes de asunción pueden ser independientes por nodo en [0,1] y su suma no está restringida a 1. La proposición infiere que si \(\Delta_i<0\), existe j con \(\Delta_j>0\) cuando el grafo es completo. La demostración supone que la sobreasunción de i debe haber sido “absorbida” desde j, sin premisa de conservación que imponga dicha transferencia.

Contraejemplo reproducible: W con todas las entradas 0.5, \(R^*=(.5,.5)\), \(\alpha=(.8,.8)\), luego \(\Delta=(-.3,-.3)\). W es completa, no negativa y estocástica por filas; no hay compensador. El mismo texto ofrece un caso de reparación voluntaria extendida en que un nodo puede asumir más que su causalidad, lo que es consistente con déficits simultáneamente negativos.

**Resultado:** proposición falsa con las premisas declaradas. Si se agregara una ley de conservación de suma uno para α (además de \(\sum R^*=1\)), entonces \(\sum\Delta=0\) y el resultado se sigue. Esa ley es adicional y no debe insertarse retrospectivamente. P5.2 no aparece como premisa formal en las demostraciones exhibidas de Thm 8.1–8.2; opera como puente explicativo hacia el diseñador, no como dependencia lógica directa de esas pruebas.

### 4.2 Teorema 6, matriz y nodo D

M10, págs. 38–41: se describe una matriz aumentada de tamaño n+1 con filas actoras estocásticas y fila final de D igual a cero; después exige irreducibilidad/aperiodicidad y usa \(W\mathbf1=\mathbf1\) para obtener λ=1. En la matriz completa esto es imposible: la última suma de fila es cero y D es sumidero, de modo que el grafo completo no es fuertemente conexo. Ejemplo de 3×3 en anexo produce sumas [1,1,0] y no satisface el paso citado.

Esto no demuestra que jamás exista un eigenvector ni que el resultado sea falso para una submatriz distinta. Sí demuestra que el objeto y las hipótesis de la demostración no coinciden literalmente. Si el teorema se refiere al subgrafo de actores, deben especificarse matriz, normalización, tratamiento de aristas a D y relación con el evento acreditado. La regularización impresa con divisor n debe revisarse además porque el tamaño anunciado es n+1 y puede destruir la estocasticidad y el carácter sumidero.

### 4.3 Orientación y normalización de W

Para (W_{ij}=w(i\to j)), el cálculo (Wr) y (W^Tr) agregan magnitudes en direcciones diferentes. Ejemplo (W=[[.9,.1],[.4,.6]]): eigenvector derecho de W normalizado = (.5,.5); eigenvector derecho de Wᵀ = (.8,.2). Si se pretende acumular influencias entrantes, la transpuesta puede ser apropiada; si se interpreta el producto como puntuación de consecuencias salientes, puede tener otro sentido. La decisión depende de la definición de responsabilidad, no de coincidir con un programa.

En M10 se pide estocasticidad por filas; el motor Prometeo utiliza pesos empíricos sin normalización. No son magnitudes intercambiables. Con W bruto [[9,1],[20,80]], eigenvector derecho ≈(.0138,.9862); normalizando filas a [[.9,.1],[.2,.8]], resulta (.5,.5). La normalización cambia el resultado, no solo la escala del eigenvalor.

### 4.4 Lema 8.1, Lema 8.2 y TIC

M10, pp. 58–62 y Apéndice A, pp. 79–82, define una sustituibilidad de fila mediante KL y afirma la cota \(R^*(E)\le(1-S_{est})/(m-1)\). Matriz positiva con cinco filas idénticas p=(.30,.25,.15,.15,.15): reemplazar la segunda fila por la media de las restantes deja W igual; KL=0, \(S_{est}=1\), pero \(R^*_E=.25\), no ≤0. El supuesto de matriz primitiva se satisface. Por tanto el lema no vale para la masa total indicada.

El propio Apéndice D.3 emplea después \(R^*_{net}=R^*(i)-R^{*(i)}_i\), una diferencia respecto de baseline. Esta es una magnitud distinta y puede ser objeto de una proposición nueva; no repara el enunciado total que se aplica previamente en Thm 8.2, ejemplos y cuadro resumen.

Lema 8.2: la prueba usa que D domina todos los m componentes para concluir (R_D>1/m), pero la condición declarada de TIC en el pasaje relevante solo compara D con un E seleccionado. Vector positivo p=(.19,.18,.30,.20,.13), W de filas idénticas p: D=.19>E=.18, aunque D<.2. Bajo esa lectura, la cota falla. Si el término “dominante” impone máximo global por definición, la premisa debe enunciarlo explícitamente y mantener esa definición en el teorema.

Thm 8.1 hereda la dependencia de Lema 8.2 y usa límites numéricos adicionales (α_vol, h, m=5) no comprendidos todos en sus tres condiciones resumidas. Thm 8.2 depende directamente de Lema 8.1. Thm 8.3 deriva monotonía mediante derivadas de una cota que no queda establecida y no modela de manera explícita cómo S cambia cuando cambia W. Thm 8.4 añade restricciones/calibraciones y límites a términos de α que no forman parte de las tres condiciones de inevitabilidad anunciadas. Se deben tratar como resultados condicionales pendientes, no como teoremas generales probados.

En Apéndice A, la desigualdad auxiliar (t\ln t\ge(t-1)+(t-1)^2/2) es falsa para t=2. La desigualdad de Pinsker puede ser verdadera por un resultado estándar independiente, pero esta ruta demostrativa es insuficiente. El uso de Davis–Kahan clásico requiere condiciones de operador autoadjunto/Hermitiano; M10 no establece simetría/hermiticidad de la matriz causal genérica. La cadena final tampoco controla cuantitativamente el término de error que luego afirma menor que .01.

### 4.5 M01: Banach, PF y convergencia

M01, Apéndice A.1, pp. 798–799: para (T(v)=Wv/\|Wv\|_1), afirma contracción en variación total por ser W primitiva y da (c=1-\delta(W)). Contraejemplo reproducible: W=[[0,1,0],[.5,0,.5],[.4,0,.6]]. El grafo es fuertemente conexo y aperiodico (nodo 3 tiene lazo y desde allí se alcanza el resto), por tanto W es primitiva; para v=e1 y w=e2, T(v) y T(w) tienen soportes disjuntos, de modo que su distancia de variación total permanece 1. No hay contracción estricta en una iteración.

Perron–Frobenius brinda para matriz primitiva un autovalor dominante simple y eigenvectores positivos; la convergencia de iteración de potencia estándar requiere condiciones pertinentes (gap espectral, orientación compatible, matriz bien definida), pero el argumento de Banach mostrado no prueba su constante ni el contrato para una matriz arbitraria. Para matrices reducibles o periódicas, puede haber selección dependiente del inicio o no convergencia; el motor indica condiciones suficientes y registra residuo, lo cual es útil, aunque no define por sí solo una magnitud única.

Más fundamental: un eigenvector es una propiedad algebraica de W; que mida “responsabilidad causal” necesita argumento semántico y validación frente a casos identificables/contrafactuales. No se deriva de existencia o convergencia.

## 5. Prometeo: correspondencia examinada

Revisión Git: `84e8ad0191856bcfd658b472c89266fbe12983a2`; archivos inspeccionados incluyen `dist-motor/grafo.js`, `r_estrella.js`, `modelo.js`, `series.js`, `alpha.js`, `delta.js`, `sustituibilidad.js`, `iic.js`, `b_estrella.js`, `fraude_annona.js`, `ampliacion.js`, `hipercubo.js`, `linter.js`, `expediente.js`, API routes, catálogo `operadores-taxonomicos.json` y suites de test. Catálogo enumera 23 operadores.

| Operación | Hecho observado en el código | Límite epistemológico |
|---|---|---|
| R* | Iteración de potencia sobre matriz dispersa; multiplica W·r; normaliza L1; residuo y diagnóstico de condiciones suficientes; regularización opcional. | No normaliza filas automáticamente; D no entra en W; unicidad/interpretación no derivan de tests. |
| Cierre | E0 queda no acreditado; E1–E8 pueden abrir cálculo según regla. | Acreditación es compuerta documental; no equivale a causalidad ni ingresa como peso espectral. |
| S | Diferencia entre R y R con fila sustituida; puede promediar/ponderar; el motor ofrece también variantes del operador. | Requiere definición estable de baseline; M10 cota total falla en caso exacto. |
| α, Δ | α externa explícita o derivación operativa, p.ej. proporción económica con límite 1; Δ=R−α por nodo. | Comparabilidad de escalas/constructos no la garantiza código. |
| IIC, B* | Conteo de coincidencias y reparto proporcional de beneficio. | Son indicadores definidos operacionalmente, no validación causal automática. |
| Sensibilidad | Extremos min/central/max, OAT o hipercubo sujeto a presupuesto. | Sensibilidad condicionada a rangos declarados, no distribución probabilística ni validez del rango. |
| Fraude annona | Fórmula de riesgo orientadora, con descargo de no calificar automáticamente jurídicamente. | Requiere validación y límites legales por jurisdicción. |
| expediente/API | Linter, validación de entrada, API y generación de expediente. | Robustez de interfaz/contratos es separable de verdad del modelo. |

Tests de la revisión cubren casos de regresión, gates, validación de interfaz, casos de matriz y diferencias de presentación. El workflow CI del commit consultado terminó exitosamente; no se ejecutó localmente en esta etapa. “44/44” aparece en registro versionado, pero no reemplaza revisión de suficiencia de cobertura ni contraste independiente.

## 6. Subsistencia instrumental

### ECO
Función efectiva observada: elicitación en presencia del sujeto; produce seis ponderaciones P(Hijos), códigos sobre cinco ejes SDO y principios de intervención/orientación. El propio texto limita su alcance: no es psicoterapia, psiquiatría ni diagnóstico DSM/CIE. U·1 de Taxonomía ofrece ruta documental y deriva a ECO cuando el material no determina ciertos pesos/posiciones. ECO puede aportar datos no documentales, pero no es condición necesaria del cálculo causal si otras fuentes satisfacen el contrato de datos. Validez, estabilidad entre entrevistadores, calidad de probabilidad y sesgo de respuesta siguen sin evidencia independiente examinada. Decisión por función: INVESTIGAR; integrar protocolo de recogida solo si produce información fiable y necesaria. No inferir eficacia clínica.

### SDO
Se describe como instrumento dinámico de lectura de posiciones de voluntad, con cinco ejes modulares y seis posiciones del eje de Hijos, rechazando expresamente que sea esencia o clasificación fija. Tiene valor potencial como vocabulario de anotación del proyecto. No se verificó fiabilidad, acuerdo interevaluador, validez de constructo ni consecuencias de decisiones basadas en códigos. Decisión: INVESTIGAR su valor como esquema de codificación; separar terminología ontológica propia de cualquier diagnóstico clínico; no conservar el volumen como sistema aplicado hasta validar reglas y utilidad.

### HISTOS
Protocolo de acompañamiento longitudinal que recibe resultados ECO/SDO y busca re-localización/sostén a través de sesiones. No es necesario para imputar causalidad de un evento; es una intervención/acompañamiento autónomo. No se revisaron de forma exhaustiva ética, salvaguardas, medidas de resultados, riesgos o evaluación de eficacia. Decisión: INVESTIGAR independiente; no sostener eficacia clínica/terapéutica con evidencia disponible.

### Taxonomía General
U·1 distingue evidencia documental confirmable, hipótesis con incertidumbre y necesidad de fuente con presencia del sujeto; la obra se extiende a 78 capítulos/13 partes. Es una arquitectura de enrutamiento y reglas por dominio, potencialmente más adecuada a catálogo versionado o base de protocolos que a tratado lineal, pero esta es hipótesis, no recomendación final. La auditoría no ha comparado capítulo por capítulo lo efectivamente cargado en Prometeo ni identificado qué reglas son fundamentales, particulares o narrativas. Decisión: INTEGRAR/INVESTIGAR por módulo; no conservar ni descartar íntegramente todavía.

### Metrología I y II
M03 declara mensurandos, incertidumbre, comparabilidad y tipos de verdad; la afirmación de que los instrumentos ya están calibrados queda como afirmación del manuscrito hasta verificar magnitudes/protocolos. M04 se presenta como glosario operativo para traducción entre nueve conceptos y cinco tipos de pregunta, no como teoría exhaustiva. M04 parece candidato a documentación de apoyo integrada; M03 requiere cotejar cada escala, error, calibración y trazabilidad con metrología estándar. No se certifica una teoría nueva de medición.

### Método Prometeo
M09 y el motor describen un proceso común de imputación y expediente jurídico. Las denominaciones de presentación no se multiplican como métodos. Hay infraestructura real de reproducibilidad (entradas estructuradas, validaciones, sensibilidad, expediente), candidata a conservar como herramienta de auditoría. La atribución jurídica final exige evidencia del caso, reglas probatorias y jurisdicción; el cálculo no reemplaza tales decisiones.

## 7. Alternativas y comparación prudente

La literatura causal contiene marcos establecidos con objetivos distintos: resultados potenciales de Rubin definen efectos de tratamiento mediante resultados contrafactuales y distinguen diseños aleatorizados/no aleatorizados; diagramas causales/SCM de Pearl representan supuestos causales y reglas de identificación. No son equivalentes automáticamente a imputación ontológica de responsabilidad: sí son comparadores necesarios para definir qué pregunta responde R*, qué contrafactual se usa y qué datos identifican el efecto. Para contribución de agentes en juegos/cooperación, Shapley es opción matemática diferente con axiomas de reparto; no se ha demostrado que iguale R* ni que mida la misma magnitud.

Entrevistas estructuradas y codificación doble ciega son alternativas para mejorar reproducibilidad de información de ECO, no sustitutos automáticos de su ontología. Para riesgo organizacional, análisis de riesgo convencional puede producir priorización de peligros, pero no siempre atribución individual. Cada sustitución debe comparar función, entradas, supuestos y pérdida informativa.

Bibliografía primaria consultada: Davis & Kahan (1970), DOI 10.1137/0707001; Rubin (1974), “Estimating Causal Effects of Treatments in Randomized and Nonrandomized Studies”; Pearl (1995), “Causal Diagrams for Empirical Research”, Biometrika 82(4), 669–688; Pearl (2010), “Causal Inference”, Proceedings of the 3rd Annual ACM/IEEE Symposium on Logic in Computer Science, 2010. Estas referencias delimitan alternativas/técnicas, no prueban o refutan el marco ontológico del proyecto.

## 8. Hipótesis de reorganización (no índice editorial)

1. Considerar un núcleo metodológico reducido: contrato de expediente, regla de inclusión de nodos, especificación de W, operador R*, α, incertidumbre/sensibilidad, salida auditable y límites de interpretación.
2. Mantener las herramientas auxiliares como módulos separados: adquisición documental, entrevista, codificación ontológica, acompañamiento y protocolos por dominio.
3. Tras resolver la definición de R*, separar resultados demostrados de convenciones y calibraciones empíricas. Retener solo teoremas con hipótesis explícitas y pruebas válidas.
4. Evaluar el glosario y taxonomía como datos/documentación navegable/versionada en vez de asumir libros independientes.

No se fija una nueva colección de libros ni se decide supervivencia editorial final.

## 9. Decisiones que corresponden al autor

- Qué significa exactamente W_ij: arista de i a j, probabilidad de transición, fracción de causalidad o peso de contribución.
- Si los pesos deben sumar 1 por fila, por columna, globalmente o conservar dimensión empírica absoluta.
- Si D es vértice de cálculo, criterio de cierre separado o variable de resultado fuera del grafo de actores.
- Si R* pretende distribuir masa de un evento, puntuación estructural de red o contribución causal identificable.
- Si α puede exceder en suma el total de R*, y si existe alguna ley de conservación.
- Si S significa sustitución estructural, cambio contrafactual o exceso neto frente a baseline.
- Qué uso está permitido de ECO/SDO/HISTOS fuera de acompañamiento y bajo qué salvaguardas.

## 10. Programa de continuación priorizado

1. Formalizar un contrato único de grafo y unidades; construir suite de matrices dirigidas/asimétricas y validar (W) vs (W^T), filas/columnas y D.
2. Reconstruir M10 en un grafo de dependencias teorema→lema→axioma→apéndice; revisar prueba completa de cada resultado que pretenda conservarse, comenzando por TIC.
3. Auditar formalmente la integral del ego/espacios/operadores de M10 y su correspondencia con M02/M01; verificar dominios, continuidad, medidas e hipótesis funcionales.
4. Reproducir calibración de 3 pilotos y extraer datos de los 18 casos; preespecificar qué evidencia y métricas aceptarían validación independiente.
5. Cotejar 23 operadores Prometeo uno por uno con fuente, contrato, tests y casos; añadir solo como trabajo de auditoría, no modificar código.
6. Terminar la subsistencia instrumental capítulo por capítulo, empezando por Taxonomía (U·1–U·4 y operadores efectivamente cargados), luego SDO/ECO/HISTOS; diseñar evaluación interevaluador/utilidad si se pretende validar.
7. Comparar R* con SCM/contrafactual, resultados potenciales, Shapley y métricas de red en una misma batería de casos, indicando dónde las preguntas no son equivalentes.

## 11. Trazabilidad y artefactos

La matriz maestra acompaña el informe como XLSX/CSV; conserva los IDs semilla A01–A25 y agrega registros nuevos. El registro independiente enumera cálculos, hipótesis y resultados. El registro de cobertura muestra secciones leídas parcialmente. Estas conclusiones son provisionales en cuanto a subsistencia global; los contraejemplos exactos sí refutan los enunciados bajo las hipótesis especificadas.

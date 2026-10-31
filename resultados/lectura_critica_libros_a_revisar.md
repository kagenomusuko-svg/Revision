# Lectura crítica de «libros a revisar»
## Informe de cierre y base de trabajo para la metrología causal

**Fecha:** 31 de octubre de 2026  
**Corpus revisado:** 10 libros en `Revision/libros a revisar`  
**Propósito:** identificar aportes aprovechables, deudas internas y condiciones necesarias para operacionalizar la imputación causal y la herramienta Prometeo, manteniendo la ontología publicada como marco canónico de referencia.

## Estado de lectura

Se completó la lectura del corpus de diez títulos de principio a fin, incluidos cierres y apéndices. ECO se revisó hasta su página física 519/519; Metrología Causal I se cotejó hasta 498/498; *El cálculo de la responsabilidad* se contrastó contra sus 834 páginas físicas. La revisión se concentra en la coherencia interna y la posibilidad de operacionalización de lo que los propios manuscritos presentan. No equivale a una verificación externa de todas las fuentes históricas, jurídicas, clínicas o empíricas que los libros citan.

## Síntesis general

El corpus ofrece una arquitectura de trabajo ambiciosa: representar actores y relaciones causales, explicitar evidencia y supuestos, localizar posiciones ontológicas, separar descripción, comprensión, prevención e imputación formal, y reconocer incertidumbre. Su valor más inmediato es como **marco de organización de preguntas, hipótesis y evidencia**. El paso desde ese mapa hacia magnitudes que puedan interpretarse como proporciones causales, medidas de responsabilidad o decisiones jurídicas todavía requiere definiciones operativas, justificación matemática y validación que los manuscritos no aportan de manera consistente.

La contabilidad causal u ontológica puede servir para comprender un fenómeno incluso cuando no existe una persona actual a quien exigir reparación, una medida ejecutable o una intervención que lo revierta. Esa función de comprensión debe permanecer distinguible de la exigibilidad jurídica, el cobro, la prevención y el acompañamiento. La lectura no debe reducir el método a encontrar culpables ni suponer que todo análisis tiene que producir una reparación.

### Contratos que deben estabilizarse antes de calcular

- **R*** aparece como eigenvector/centralidad de red y también como fracción causal o porcentaje de resultado imputable. La primera interpretación no implica automáticamente la segunda.
- **S** se describe como sustituibilidad contrafáctica del actor, pero a veces se aproxima mediante perfiles de Hijos, correlaciones, centralidad o juicio cualitativo. Esas operaciones no son equivalentes sin una regla de medición demostrada.
- **α** cambia entre integración/asunción ontológica, rúbrica conductual, mitigación, reparación y proporción monetaria. No debe tratarse como una misma magnitud hasta fijar su constructo, unidad y procedimiento.
- **Δ** no mantiene una convención estable: aparecen tanto `R* − α` como `R*(1−α)`. Esta segunda forma solo es dimensionalmente coherente si α es una proporción compatible; las obras alternan entre esas definiciones.
- La orientación de la matriz **W** y el uso de `W` frente a `Wᵀ` no se mantienen uniformes. Como cambia qué nodos resultan dominantes, debe definirse explícitamente si las filas representan origen o destino y qué interpretación tiene el vector.
- **P(Hijos)** se presenta como distribución probabilística y también como ponderación heurística o código clínico. Los umbrales y señales no cuentan con calibración ni fiabilidad interevaluador suficiente para tratar los valores como probabilidades validadas.

Para cada salida cuantitativa faltan, según el caso, el estimando, población/unidad de análisis, resultado, horizonte temporal, contrafactual, regla de inclusión de actores, método de agregación, incertidumbre, sensibilidad y evidencia de calibración. Definir una fórmula no demuestra por sí solo que mida el concepto nombrado.

## Hallazgos por libro

### 1. *La transformación formal: la ontología del ego como fundamento del cálculo causal*

Aporta el armazón ontológico que relaciona voluntad, campo, primera y segunda mediación e integral del ego. Es indispensable como especificación del sentido que el sistema atribuye a sus variables. El propio libro distingue derivación formal y calibración empírica, distinción útil para no confundir consistencia conceptual con medición observada.

Los parámetros, rangos por Hijo y coeficientes como β, γ e IIC no quedan calibrados empíricamente por la derivación ontológica. En la integral vectorial, la afirmación de irreversibilidad requiere precisar las condiciones: un integrando no nulo puede acumularse con cancelaciones vectoriales. También es necesario mantener tipadas las diferencias entre conjuntos de colapsos, vectores y magnitudes escalares.

### 2. *Axiomatización del sistema de la doble mediación*

Expone resultados matemáticos y supuestos que podrían formar parte de una teoría formal. La revisión encontró saltos en las condiciones de Perron–Frobenius: una matriz asociada a un grafo causal con sumideros puede ser reducible, de modo que positividad, unicidad y convergencia no se siguen sin condiciones adicionales.

La demostración de Cramér–Rao contiene pasos numéricos inconsistentes entre varianza y cota; el límite de Davis–Kahan atribuido al vector de responsabilidad no queda derivado en el apéndice; y el supuesto de Markov introduce independencias que no se establecen. Los resultados deben presentarse como pendientes hasta que se corrijan pruebas y se especifiquen los supuestos.

### 3. *Metrología Causal: La ciencia de la medición causal*

Su aporte organizador principal es tratar las Series I, II y III como configuraciones de consulta de un mismo operador: describir/comprender, evaluar una brecha normativa e imputar formalmente. Esto permite que la contabilidad causal no se confunda con una búsqueda exclusiva de sanción o reparación.

El libro formula R* como eigenvector y lo interpreta como necesidad o fracción de responsabilidad sin demostrar esa equivalencia. Los rangos de S por Hijo se declaran no empíricos; α e IIC dependen de criterios aún no operacionalizados; la sensibilidad finita no acredita estabilidad en todo el espacio de parámetros. El glosario final confirma cambios semánticos de R*, S, α y Δ entre dominios. El glosario es un mapa conceptual, no evidencia independiente de validez.

### 4. *Metrología Causal Vol. II*

Es un manual útil para organizar el flujo de datos: entradas, hoja de calibración, rangos, análisis de sensibilidad, declaración de robustez y reporte. La distinción entre incertidumbre epistémica y estructural puede conservarse como requisito de documentación.

Las rutas propuestas para estimar S y α no muestran que midan el mismo constructo ni que produzcan valores reproducibles entre evaluadores. Las ponderaciones, rangos y umbrales se proponen con precisión numérica mayor que la evidencia que los sustenta. Una prueba de sensibilidad solo informa sobre la incertidumbre modelada; no corrige una estructura causal incompleta ni valida la interpretación de R*.

### 5. *SDO: Sistema de diagnóstico ontológico*

Proporciona el vocabulario y la estructura de cinco ejes para localizar configuraciones del ego. Puede servir como esquema de codificación cualitativa o como generador de hipótesis sobre qué evidencia buscar.

Los códigos no equivalen por sí mismos a escalas numéricas. Las reglas para inferir estados internos desde actos, documentos y relatos necesitan especificar codificación, evidencia negativa, evaluadores independientes, desacuerdos, estabilidad temporal y falsos positivos/negativos. La conexión entre los ejes y valores de S, α o R* no se valida mediante la mera correspondencia conceptual.

### 6. *Taxonomía General de Aplicaciones*

Reúne 78 ámbitos y muestra cómo adaptar preguntas y fuentes a dominios diferentes. Su amplitud ayuda a identificar diversidad de unidades causales, resultados y contextos, y a evitar que una sola plantilla narrativa se imponga sin ajustes.

Los capítulos no constituyen 78 validaciones del método. En múltiples aplicaciones, las distribuciones, coeficientes, contrafácticos y efectos monetarios se asignan sin datos, calibración o análisis reproducible suficientes. Debe tratarse cada dominio como un programa de investigación separado en sus definiciones de resultado y evidencia, sin presentar valores ilustrativos como medidas obtenidas.

### 7. *HISTOS: Protocolo de Acompañamiento Ontológico*

Aporta una distinción relevante entre localización y acompañamiento, incorpora seguimiento longitudinal y reconoce que la mediación puede alterar el fenómeno observado. También advierte sobre reactivación, contexto, reversión y la necesidad de derivar cuando el caso excede el marco.

Sus señales y escalas de S, α y Δ son predominantemente cualitativas, ordinales o dependientes del juicio del mediador. Los umbrales de sesiones y las asociaciones clínicas descritas no vienen acompañados de validación reproducible. HISTOS puede aportar contexto y trazabilidad longitudinal, pero no debe convertirse sin puente validado en una medición numérica de imputación.

### 8. *El método Prometeo: imputación causal para juristas y abogados*

Ofrece un lenguaje para ordenar actores, aristas, evidencia, rangos, incertidumbre y escenarios adversariales. La separación declarada entre mapa causal y decisión jurídica es útil y debe preservarse: el método no sustituye el estándar probatorio ni decide culpabilidad.

Los rangos E0–E8 y pesos de arista no se derivan automáticamente del tipo de documento: una fuente puede sustentar que ocurrió un acto sin medir la intensidad causal atribuible. R* como eigenvector no se identifica con porcentaje causal; S y α requieren definiciones distintas y estables; dolo, culpa, imputación jurídica y causalidad no son intercambiables. Los casos contienen cifras y conclusiones que exceden lo que los datos y reglas descritos permiten establecer.

### 9. *El cálculo de la responsabilidad: una ontología matemática para sistemas causales complejos*

Es el tratamiento más amplio de dominios, casos, apéndices, calibración y código. Entre sus elementos útiles están la explicitación de incertidumbre, la diferenciación entre responsabilidad distribuida y exigibilidad, y el reconocimiento de que la prueba contrafáctica y la selección de actores condicionan el análisis.

La revisión detectó problemas reiterados: centralidad espectral interpretada como fracción causal; grafos reducibles tratados como si cumplieran las condiciones de Perron–Frobenius; S calculada mediante correlación o sustitución arbitraria; escalas de α heterogéneas; predictores y coeficientes sin datos reproducibles; errores aritméticos y de código en apéndices; y valores históricos/jurídicos presentados con una precisión que no está sustentada por el procedimiento expuesto. Los ejemplos sirven para revelar decisiones que el método tendría que formalizar, no como resultados empíricos ya establecidos.

### 10. *ECO: Entrevista Clínica Ontológica*

ECO reconoce límites, permite declarar incertidumbre, diferencia localización incompleta/no concluyente/no evaluable e incorpora criterios de derivación. Esos elementos pueden orientar un registro transparente de evidencia y límites. El libro insiste en que la localización no debe confundirse con el acompañamiento y que Histos requiere consentimiento, orientación del sujeto y condiciones relacionales.

Las categorías cualitativas dependen fuertemente del mediador; no se presentan estudios de acuerdo interevaluador, sensibilidad, especificidad ni validez externa. Varias preguntas y dinámicas pueden inducir la señal que luego se interpreta como diagnóstica. El principio de no etiquetado mantiene una tensión con autonomía y consentimiento cuando se recomienda ocultar el mapa técnico incluso ante preguntas de la persona. Los apéndices contienen discrepancias de códigos, escalas EP, sondeos y reglas de cierre que requieren control de versión antes de uso.

## Orden de trabajo recomendado para operacionalizar

1. **Fijar el contrato de variables** desde la ontología canónica: significado, tipo, unidad, dominio, instante y relación formal entre v, c, φ₁, φ₂, I, R*, S, α, Δ e IIC.
2. **Separar tres capas** en cada expediente: evidencia observada; interpretación/hipótesis ontológica; conclusión o magnitud imputativa. Añadir trazabilidad de quién codificó, con qué regla y qué alternativas quedan abiertas.
3. **Definir qué se quiere medir** por Serie y por dominio, aunque el resultado sea solo comprensión: objeto, actores, efecto, horizonte temporal y contexto. No exigir posibilidad de reparación para admitir un análisis.
4. **Resolver las propiedades matemáticas** del grafo y del algoritmo: orientación W/Wᵀ, condiciones de existencia/estabilidad, nodos aislados/sumideros y significado del vector calculado.
5. **Separar estimación causal de centralidad**. Si R* quiere significar fracción atribuible, especificar el estimando y el método contrafáctico; si se conserva como centralidad, nombrar e interpretar esa medida sin equipararla a porcentaje causal.
6. **Construir rúbricas de codificación** con ejemplos positivos, negativos y ambiguos; medir acuerdo entre evaluadores y revisar sesgos del instrumento, del mediador y de la fuente.
7. **Validar por etapas**: primero casos simulados y revisión aritmética; después estudios retrospectivos con criterios externos; finalmente evaluación prospectiva. Reportar incertidumbre y fallos, no solo rankings estables.
8. **Auditar Prometeo contra el contrato estabilizado** antes de cerrar la herramienta. La fidelidad del software depende de que las fórmulas, escalas, entradas y salidas de los libros se hayan resuelto primero.

## Criterio de lectura aplicado

La ontología publicada se toma como marco de referencia del proyecto, no como un texto que se reabre para acomodarlo a los resultados. Las observaciones de este informe señalan si los libros de metrología, aplicación y herramienta representan ese marco de forma consistente y si justifican sus mediciones. Una deuda de demostración o validación no elimina el valor de un concepto como pregunta o hipótesis; sí impide presentarlo como magnitud demostrada.


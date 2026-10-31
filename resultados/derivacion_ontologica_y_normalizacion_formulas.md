# Derivación ontológica y normalización de las fórmulas
## Documento de trabajo acumulativo

**Versión:** 0.5  
**Fecha de inicio:** 31 de octubre de 2026  
**Repositorio de trabajo:** `Revision`  
**Marco normativo:** libros canónicos de ontología de Afrodita Areia y textos ontológicos asociados.

## 1. Propósito y regla de derivación

Este documento reúne, en un mismo recorrido:

1. las fórmulas y relaciones que se derivan de la ontología canónica;
2. las formalizaciones que *El cálculo de la responsabilidad*, *Axiomatización del sistema de la doble mediación* y otros libros epistemológicos hacen de esas relaciones;
3. las operaciones que esos libros ejecutan con las fórmulas; y
4. las normalizaciones necesarias para que la formulación epistemológica y Prometeo sean consecuentes con el marco canónico.

La dirección es ontología → derivación → formalización → operación. Una fórmula de un libro epistemológico no se toma como canónica por aparecer allí. Cada conclusión se coteja con la definición ontológica que pretende expresar.

Este archivo es un registro técnico de trabajo. Las marcas de cotejo sirven para resolver las fórmulas antes de redactar la versión publicable; no son reservas que deban trasladarse automáticamente a los libros finales ni una solicitud de abrir investigaciones nuevas.

## 2. Convenciones de este documento

- **Derivada:** consecuencia formal o estructural que se sigue de una definición canónica.
- **Formalización compatible:** expresión matemática posible para una relación ontológica, siempre que sus términos representen exactamente esa relación.
- **Operación añadida:** procedimiento que un libro epistemológico introduce y que no se sigue únicamente de la fórmula ontológica.
- **Normalización:** ajuste de notación, dominio, unidad, orientación o significado requerido para que la operación exprese la relación canónica.
- **No equivalente:** dos expresiones pueden compartir símbolos o lenguaje sin medir la misma cosa.

El término *contabilidad causal/ontológica*, así como sus usos en imputación o compliance, se conserva como una misma operación presentada desde distintas preguntas y objetos. La exigibilidad de consecuencias es una cuestión distinta de la contabilización y comprensión causal.

## 3. Núcleo canónico ya cotejado

### 3.1. Doble mediación

La fórmula canónica de la mediación bis es:

[
Ego(t)=arphi_2!left(arphi_1(v_t,c_t),I(t)ight).
]

Definimos, como abreviatura de lectura y no como concepto nuevo,

[
a_t:=arphi_1(v_t,c_t).
]

Entonces:

[
Ego(t)=arphi_2(a_t,I(t)).
]

- (arphi_1) orienta la voluntad en el campo y produce el acto/colapso (a_t).
- (arphi_2) retorna ese acto al sujeto que lo asume y opera respecto de la trayectoria acumulada (I(t)).
- (I(t)) nombra la trayectoria que entra como condición histórica del ciclo; (Ego(t)) nombra el resultado egoico de la operación. No son intercambiables.

**Fuentes canónicas:** *Afrodita Areia I: Sobre la pasión*, fórmula de mediación bis y glosario “Integral del ego” (pp. 190–191); *Ágape*, formulación de la fórmula Ego(t); *Areópago*, cap. V, pp. 36–37.

### 3.2. Integral del ego y actualización de la trayectoria

El marco canónico caracteriza (I(t)) como la acumulación de los colapsos que el sujeto ha asumido como propios. En el apéndice formal de *Sobre la pasión* aparece la expresión esquemática:

[
Ego(t)=int f(v),dv,
qquad
rac{d}{dt}Ego(t)=f(v_t).
]

El glosario precisa que (f) representa la contribución de cada ciclo de doble mediación: el acto orientado por (arphi_1) y retornado como propio mediante (arphi_2), en sus circunstancias y desde la trayectoria previa. Por tanto, la integral no acumula sin distinción todo lo que ocurrió: representa la trayectoria constituida por la operación egoica de asunción.

Como representación recursiva, la relación puede anotarse así:

[
I_{t+1}=operatorname{Actualizar}!left(I_t,arphi_2(a_t,I_t)ight),
qquad a_t=arphi_1(v_t,c_t).
]

Esta escritura conserva la estructura canónica. **No impone todavía** una suma lineal, un umbral binario ni una regla numérica para (operatorname{Actualizar}); esas operaciones deben cotejarse con las definiciones canónicas y distinguirse de los supuestos que agreguen los libros posteriores.

**Fuentes canónicas:** *Sobre la pasión*, apéndice sobre la derivada del ego (p. 165), y glosario “Integral del ego” (pp. 190–191).

### 3.3. Pertenencia causal externa y asunción interna

*Areópago* separa dos operaciones:

- La pertenencia causal del acto se establece por la primera mediación: el acto ocurrió a través del ego y la cadena causal pasa por él.
- La asunción ante sí mismo corresponde a la segunda mediación (arphi_2).

La imputación desde la alteridad puede identificar la posición causal sin requerir que el sujeto haya asumido internamente el acto. En consecuencia, la evasión o bloqueo de (arphi_2) no borra la producción causal ya atribuida mediante (arphi_1).

Esta distinción impide usar un indicador de asunción como sustituto de la atribución causal. Puede modular una operación posterior que el sistema defina, pero no cambia retrospectivamente quién produjo el acto.

**Fuente canónica:** *Areópago*, cap. V, pp. 36–37; formulación corporativa de la mediación en pp. 26–27.

### 3.4. Nodo necesario del daño específico

*Areópago* formula el criterio mínimo:

[
N	ext{ es nodo necesario del daño }D
quadLongleftrightarrowquad

eg N 	o 
eg D.
]

La flecha expresa un contrafáctico: sin (N), este daño específico no habría ocurrido de esa forma específica. No expresa necesidad metafísica. El análisis se refiere a un resultado y unas condiciones concretas, y reconoce la incertidumbre de reconstruir la alternativa.

El canon también afirma que la responsabilidad se distribuye según la posición causal de los nodos cuando concurren varios actores. De ello se deriva la necesidad de analizar posiciones y cadenas causales; **no se identifica todavía una fórmula única de reparto porcentual ni se deduce automáticamente una centralidad espectral**.

**Fuente canónica:** *Areópago*, cap. 4, “El nodo necesario como criterio”, pp. 49–51; desarrollo de especificidad y distribución de nodos a lo largo del volumen.

## 4. Cotejo de las fórmulas epistemológicas

| Fórmula/operación en los libros de trabajo | Relación canónica que pretende expresar | Cotejo y normalización |
|---|---|---|
| (I(t)=int_0^t c(	au)w(	au),d	au) | Trayectoria acumulada por los colapsos asumidos | Es una formalización compatible si el integrando representa la contribución que (arphi_2) efectivamente integra. Si (c) contiene todo colapso producido, la fórmula debe distinguir los colapsos asumidos de los rechazados. No declarar esa equivalencia sin fijar el dominio de (c) y la función de (w). |
| (arphi_2(a,I)=I+delta(a)mathbf{1}_{{operatorname{eval}(a,I)>	heta}}) | Actualización de la trayectoria por segunda mediación | *Axiomatización* introduce una regla binaria de evaluación, umbral e incremento aditivo. Es una operación formal añadida; debe cotejarse con la posibilidad canónica de grados/procesos de asunción. No se obtiene de la fórmula de doble mediación por sustitución algebraica. |
| (RSC(t)={c(	au):0leq	auleq t}) | Registro de todo lo producido | Compatible como inventario de colapsos, separado de la trayectoria que resulta de asumirlos. |
| (RSC(t)setminus I(t)) | Supuesta brecha entre colapsos y trayectoria integrada | No está bien tipada: (RSC(t)) es un conjunto de colapsos e (I(t)) es un vector/estado acumulado. La brecha debe expresarse entre el conjunto de colapsos producidos y el subconjunto/proceso de los integrados; luego, si se requiere una magnitud, definir una operación de agregación sobre esa diferencia. |
| (R^*=) eigenvector dominante de (W^T), normalizado en el simplex | Distribución cuantitativa de influencia/responsabilidad sobre nodos | *Axiomatización* usa (W^T); otros pasajes de *El cálculo* emplean (W) o describen el vector de forma distinta. El canon sustenta pertenencia causal por (arphi_1), contrafáctico específico y proporcionalidad a la posición causal. El puente entre esa proporcionalidad y eigenvector requiere derivación explícita desde la definición canónica; la elección de (W) o (W^T) es parte de esa operación. |
| (S_{mathrm{op}}(t)=rac{|c|}{|c|+|a_t|}) | Sustituibilidad del nodo por el campo | Es una razón construida a partir de dos normas. Comparar normas en espacios distintos exige una escala común; la fórmula no equivale por sí misma al contrafáctico canónico de sustitución. Registrar como índice operacional separado hasta demostrar la correspondencia semántica. |
| (S_{mathrm{est}}(i)=1-rac{D_{KL}(R^*|R^{*(i)})}{log m}) | Efecto de sustituir estructuralmente al nodo | Operación de sensibilidad sobre el grafo: reemplaza una fila y compara distribuciones espectrales. Debe distinguirse de la sustituibilidad contrafáctica del actor y justificar la intervención “promedio de las otras filas”. |
| (R^*_{mathrm{neta},i}=R^*_i(1-S_i)) | Parte no sustituible/idiosincrática de la posición causal | Es una descomposición propuesta por los libros de trabajo. Para derivarla, deben fijarse las escalas y establecer qué significa “parte idiosincrática” a partir de la posición causal canónica; no confundirla con el criterio de nodo necesario. |
| (alpha(t)=rac{int_0^t mathbf{1}_{mathrm{int}}(	au)w(	au)p(	au),d	au}{int_0^t w(	au),d	au}) | Asunción/integración de los actos | La ontología funda (arphi_2) como asunción e integración en la trayectoria. La fórmula incorpora indicador, pesos y grado (p); hay que normalizar si (alpha) mide grado de asunción o fracción de responsabilidad (R^*). No usar ambos sentidos con la misma unidad sin transformación definida. |
| (Delta_i=R^*_i-alpha_i) | Brecha entre posición causal y asunción | Requiere que (alpha_i) se exprese en la misma escala que (R^*_i). |
| (Delta_i=R^*_i(1-alpha_i)) | Responsabilidad causal no integrada | Es dimensionalmente coherente si (alpha_iin[0,1]) es una proporción de (R^*_i). No equivale a (R^*_i-alpha_i) cuando (alpha_i) es una magnitud absoluta. La forma canónica se determinará conforme a qué significa (arphi_2) y a cómo *Areópago* distingue imputación externa de asunción interna. |

## 5. Primeras normalizaciones que se desprenden del cotejo

1. Mantener separados el acto producido por (arphi_1), el acto asumido por (arphi_2), el registro de colapsos y la trayectoria (I(t)).
2. No restar conjuntos de eventos y vectores acumulados. Definir primero los objetos y sus tipos.
3. Tratar la regla de umbral binario de (arphi_2) como formalización añadida, no como consecuencia automática de la fórmula ontológica.
4. Derivar la asignación cuantitativa (R^*) desde el criterio canónico de causalidad y distribución proporcional antes de fijar centralidad espectral como cálculo.
5. Fijar la orientación de (W) y justificar el uso de (W) o (W^T) en relación con esa derivación.
6. Separar (S) como medida contrafáctica de sustituibilidad de las aproximaciones normativas o estructurales que se usen para calcularlo.
7. Fijar si (alpha) es grado de asunción de (arphi_2), proporción de (R^*) ya asumida, o una variable de otro dominio; no mezclarlo.
8. Elegir una única definición de (Delta) compatible con la definición de (alpha) resultante y propagar esa convención a los demás libros y al código.

Estas son operaciones de normalización del material existente. No obligan a conservar cada fórmula ni cada libro: cuando una formalización no se desprenda del canon o no resulte necesaria para el método, se podrá sustituir, retirar o dejar para otra línea de trabajo.

## 6. Siguiente tramo de derivación

El siguiente análisis desarrollará, en este orden:

1. la fórmula de (R^*) de *El cálculo de la responsabilidad* y la definición 6.1 de *Axiomatización* frente al criterio del nodo necesario y la distribución proporcional de *Areópago*;
2. la derivación de (S), separando contrafáctico de sustitución y sustitución del grafo;
3. las versiones de (alpha) como registro de (arphi_2) y su correspondencia con la escala de (R^*);
4. la normalización de (Delta), (R^*_{mathrm{neta}}) y las magnitudes derivadas;
5. los teoremas de existencia, unicidad, estabilidad, Cramér–Rao y Davis–Kahan de *Axiomatización*, comprobando cada hipótesis y cada paso algebraico desde las definiciones ya normalizadas.



## 7. Derivación de la distribución causal R*

### 7.1. Qué establece la ontología

Para un daño específico D y un nodo Nᵢ, *Areópago* establece el criterio contrafáctico mínimo:

`N_i es necesario para D ⇔ ¬N_i → ¬D`.

Ese criterio identifica una relación nodo–resultado bajo una reconstrucción de la cadena. Para varios nodos que concurren, el libro no propone equivalencia automática entre ellos: la distribución debe seguir la **posición causal**, entendida como la capacidad de determinar las condiciones dentro de las cuales operan los demás nodos. El nodo que fija el marco tiene una posición más pesada que quienes actúan dentro de él (*Areópago*, cap. 4, pp. 49–54).

La forma más fuerte que se obtiene directamente del canon es, por tanto, una relación ordinal contextual:

`Pos_i(D) > Pos_j(D)  ⇒  Responsabilidad_i(D) > Responsabilidad_j(D)`,

cuando ambos son relevantes para la misma cadena/daño y la reconstrucción sostiene esa diferencia de posición. No se obtiene por esa relación una escala cardinal única, ni que todas las posiciones deban sumar 1. *Areópago* dice expresamente que la proporcionalidad exige ordenar las posiciones y que no requiere cuantificarlas con precisión matemática (p. 54). La ontología sí exige una atribución proporcional; no fija por sí sola el algoritmo de cuantificación.

### 7.2. Operación de los libros epistemológicos

**El cálculo de la responsabilidad**, §6.2, define `R*` como eigenvector principal de `W`:

`W R* = ρ(W) R*,   R*_i > 0,   Σ_i R*_i = 1`.

**Axiomatización**, Def. 6.1, elige `Wᵀ`:

`Wᵀ R* = λ R*,   R*_i > 0,   Σ_i R*_i = 1`.

Axiomatización declara que `Wᵀ` recoge la influencia que los predecesores ejercen sobre cada nodo; el texto anterior usa `W` en la ecuación y el Método de potencias. Con la convención `W_{ij}=w(i→j)` (fila = origen, columna = destino), ambas operaciones miden centralidades distintas. El canon permite ordenar posición causal, pero no resuelve esta orientación matricial por sí solo.

### 7.3. Compatibilidad con el criterio canónico

El eigenvector normalizado produce una distribución numérica de centralidad estructural para la matriz que se le entrega. Esa salida puede servir como formalización de posición causal **si** las aristas y pesos representan la capacidad de cada nodo para determinar las condiciones de los demás, y si la operación conserva el orden causal exigido por *Areópago*. La ecuación eigenvectorial, sin ese puente semántico, no demuestra que `R*_i` sea una fracción del daño o del resultado que transitó causalmente por i. Menos aún demuestra por sí sola el contrafáctico `¬N_i → ¬D`.

La normalización `Σ_i R*_i=1` convierte el vector en una distribución de centralidad relativa. No se deriva del criterio del nodo necesario: es una convención matemática añadida para comparar componentes. Por ello, las lecturas “52% de la responsabilidad causal” o “esta fracción del daño” no se siguen solo de normalizar el eigenvector. La forma directamente defendible por el cálculo, antes de establecer la equivalencia, es “participación relativa en la centralidad estructural calculada bajo G y W”.

### 7.4. Incompatibilidad entre las condiciones de G y el teorema invocado

Axiomatización define el nodo final n+1 como sumidero sin aristas salientes, y define la última fila de W como cero (Def. 6, pp. 38–39). El mismo teorema de R* requiere irreducibilidad/irreducibilidad del grafo para garantizar eigenvector estrictamente positivo y único. Un grafo con sumidero sin salida no es fuertemente conexo con los demás nodos; por tanto, la condición de irreducibilidad falla en el G definido.

Si el grafo causal es un DAG sin lazos, su matriz de adyacencia ponderada es nilpotente tras ordenar los nodos topológicamente y tiene radio espectral cero; la conclusión de un eigenvector dominante positivo no aplica. Añadir perturbaciones `W(ε)=(1−ε)W+εJ/n` puede crear conectividad matemática, pero añade transiciones que no estaban en la cadena causal reconstruida. Esa perturbación no deriva una conexión ontológica; cambia el objeto modelado.

Además, normalizar cada fila de actores para que sume 1 transforma los pesos en cuotas de salida condicionadas a cada nodo. Si una fila contiene una sola arista, su peso será 1 incluso si la evidencia de esa arista es débil. Por eso las cuotas de salida no pueden llamarse automáticamente intensidad causal absoluta.

### 7.5. Normalización provisional de R*

Para conservar separadas las operaciones que el texto mezcla, el registro usa dos objetos:

- `Nec_i(D)`: resultado del criterio contrafáctico de nodo necesario, cuando la cadena y la evidencia permiten determinarlo.
- `R*_i(G,W)`: componente del índice numérico calculado sobre el grafo y la matriz especificados.

No se identifica `R*_i` con `Nec_i(D)`, ni con una fracción del daño, hasta que el método establezca una derivación entre ellos. Esto no elimina el uso de R*: obliga a nombrar con exactitud qué calcula y a hacer que la normalización elegida sea consistente con la posición causal canónica.

**Resultado de este tramo:** la jerarquía/proporcionalidad de posiciones causales se deriva del canon; el eigenvector y la suma uno son operaciones añadidas. La definición actual del grafo de Axiomatización impide invocar simultáneamente irreducibilidad y sumidero sin salida. La normalización posterior debe fijar el objeto de grafo y la interpretación de W antes de propagar R* a S, α, Δ o montos.

## 8. Registro de normalización pendiente

| Familia | Análisis siguiente | Pregunta formal que debe cerrarse |
|---|---|---|
| Grafo y pesos W | Convención de arista, dominio de actores y resultado, significado de w | ¿w codifica cuota de transición, intensidad causal, evidencia o capacidad de determinar condiciones? |
| Sustituibilidad S | S operacional, S estructural y sustitución contrafáctica | ¿Qué reemplazo se modela y qué resultado se compara? |
| Asunción α | Fórmulas continua y discreta de Axiomatización | ¿Qué operación de φ₂ se registra y cómo se expresa en escala comparable con R*? |
| Déficit Δ | `R*−α` y `R*(1−α)` | ¿α es cantidad absoluta o proporción de la posición causal? |
| Consecuencias de R* | `R*_neta`, AD, D_total, beneficios, Shapley, índices y predictores | ¿Qué interpretación se conserva después de fijar la escala de R*? |
| Teoremas de Axiomatización | Perron–Frobenius, irreversibilidad, Cramér–Rao, Davis–Kahan, Markov | ¿Las hipótesis se cumplen en el modelo y cada conclusión se sigue de ellas? |


## 9. Derivación y normalización de S, α y Δ

### 9.1. Sustituibilidad S

#### Base canónica

*Areópago* incorpora las alternativas disponibles al contrafáctico: al quitar un nodo de la cadena, hay que reconstruir si otro actor/factor habría ocupado esa posición y si el mismo daño específico habría ocurrido. La sustituibilidad es, por tanto, relativa a una posición, una cadena, un resultado y unas condiciones concretas; no es una propiedad fija del actor. La pregunta canónica es contrafáctica: qué habría pasado en ausencia de i y qué alternativa real existía (*Areópago*, cap. 4, pp. 50–51).

#### Operaciones de los libros de trabajo

1. **El cálculo de la responsabilidad** usa `S_i=(A+B+C)/3), con indicadores de formalización del procedimiento, consecuencias de desobedecer y proporción de pares que actuarían igual. Esa media solo tiene interpretación si A, B y C son mediciones comparables y están codificadas en la misma escala; el libro no define una regla homogénea para ello. Además, la respuesta de compañeros puede informar sobre una alternativa típica, pero no equivale por sí sola al contrafáctico del daño específico.
2. **Axiomatización, S operacional**, usa
   `S_op(t)=||c||_C/(||c||_C+||a_t||_E)`.
   Es una razón entre dos normas para estimar la parte atribuible a configuración heredada. El canon distingue campo y voluntad dentro de `φ₁(v_t,c_t)`, pero no deriva esta razón ni identifica esas normas como magnitudes aditivas de contribución. Como c y a_t pertenecen a espacios distintos, dividir cada norma por máximos observados no constituye una escala común invariante: el resultado depende de la muestra y de cómo se eligieron esos máximos.
3. **Axiomatización, S estructural**, reemplaza la fila de W del actor i por el promedio de las otras filas, calcula R* y R*^(i), y define
   `S_est(i)=1−D_KL(R* || R*^(i))/log(m)`.
   Esta operación mide cuánto cambia una centralidad calculada al hacer una sustitución específica en la matriz. El reemplazo por la fila promedio es una intervención modelada; no demuestra que represente un sustituto real ni el resultado bajo ausencia del actor.

#### Normalización derivada

Conservar S como **índice contrafáctico de sustituibilidad contextual**: la pregunta que lo define es si, sin i, otro nodo/factor disponible habría producido el mismo daño específico bajo las condiciones reconstruidas. Los códigos S_op y S_est deben mantenerse como operaciones auxiliares diferentes hasta demostrar la correspondencia con esa pregunta. No promediarlas ni sustituir una por otra por compartir el nombre S.

El puente `S_op≈g(S_est)` de la Proposición 3.3 no queda demostrado por el texto. La desigualdad de Pinsker da una cota superior entre distancia de distribuciones y KL; no convierte por sí sola el orden de divergencias KL en el orden de las perturbaciones de filas ni prueba monotonicidad entre dos métricas distintas. Además, la demostración invierte el orden al pasar de mayor desviación a menor S_op. Por tanto, la afirmación de que S_op puede usarse como proxy de S_est no se sigue de esa prueba.

La cota `D_KL≤log(m)` tampoco es general para dos distribuciones: KL puede superar log(m) y crecer sin cota cuando algún q_k se aproxima a cero con p_k>0. En consecuencia, la fórmula actual no garantiza `S_est∈[0,1]`; puede dar valores negativos. El rango solo podría fijarse tras especificar restricciones adicionales o una transformación cuyo significado esté definido.

**Resultado de este tramo:** el contrafáctico contextual de sustitución tiene fundamento canónico; las tres fórmulas actuales son distintas operacionalizaciones y ninguna se deduce del canon por sí sola.

### 9.2. Coeficiente de asunción α

#### Base canónica

La ontología define `φ₂` como la operación que retorna el acto al sujeto y modifica la trayectoria acumulada. `α` puede servir para registrar el grado/proporción en que la historia de actos queda integrada, siempre que se mantenga ligado a esa operación y se indique a qué actos, sujeto y período se refiere.

#### Fórmula continua de Axiomatización

El libro propone:

`α(t)= [∫₀ᵗ 1_int(τ) w(τ) p(τ)dτ] / [∫₀ᵗ w(τ)dτ]`,

con `1_int∈{0,1}`, `p∈[0,1]`, `w≥0`. Si el denominador es finito y estrictamente positivo, entonces la expresión es un promedio ponderado de `1_int p` y cumple `0≤α(t)≤1`. Esa cota sí se deriva de la fórmula y de sus hipótesis.

La expresión es compatible con la ontología como **resumen escalar del registro de integración** si:
- `1_int` se asigna a cada evento/collapse mediante la operación de `φ₂`, no por comparar un evento con el vector I(t);
- `p` está definido como grado de integración del evento y no como otro concepto;
- `w` pondera la relevancia temporal sin contar como asumido lo que la ontología clasifica como no integrado.

En Axiomatización, `RSC(t)\I(t)` vuelve a usarse para definir `1_int`; la dificultad de tipos señalada en §4 sigue vigente. La regla debe referirse a un subconjunto de eventos integrados o a una variable de integración por evento.

#### Fórmula discreta

Para un solo colapso, con `w(τ)=δ(τ−t_i)`, la propiedad de muestreo de Dirac reduce la media continua a:

`α(a_i)=p_pres·p(t_i)`.

Si `p(t_i)=f(t_i)g(t_i)`, resulta:

`α(a_i)=p_pres·f(t_i)·g(t_i)`.

Esta reducción es algebraicamente válida bajo las condiciones de borde de la delta y si la definición de `p=f g` se mantiene. Para múltiples eventos discretos, la versión de sistema es:

`α(t)= [Σ_i w_i·p_pres,i·f_i·g_i] / [Σ_i w_i]`.

No es igual a la media aritmética simple de los `α(a_i)` salvo que todos los eventos tengan igual peso. La agregación por dominio `α_D=(1/|A_D|)Σ_i α(a_i)` es, por tanto, una decisión de ponderación distinta de la integral general.

#### Normalización

Mantener `α_i` como índice de integración/asunción de los actos del nodo i en un expediente y período especificados. La ontología sí justifica que α se refiera a `φ₂`; no convierte automáticamente el valor en porcentaje de responsabilidad causal externa. Para comparar α con R* hay que fijar una transformación y la misma unidad/denominador.

### 9.3. Déficit Δ

Los libros proponen dos expresiones incompatibles:

`Δ_i=R*_i−α_i`,

y

`Δ_i=R*_i(1−α_i)`.

No son identidades algebraicamente equivalentes. Si `α_i` es una **fracción interna de la cuota causal de i**, la cantidad asumida en la escala global es `R*_i α_i`; su complemento resulta:

`Δ_i=R*_i−R*_iα_i=R*_i(1−α_i)`.

Si, en cambio, `α_i` ya es una magnitud absoluta en la misma escala global que R*, la resta `R*_i−α_i` es dimensionalmente posible, aunque el significado de α y las condiciones para interpretarla como “asunción” deben estar definidos de esa manera.

La fórmula continua de Axiomatización describe α como proporción ponderada de colapsos del actor que han sido integrados; no como cuota absoluta del resultado total. Por eso, **la normalización más directa para un déficit proporcional es** `Δ_i=R*_i(1−α_i)`, con `α_i∈[0,1]`. En esta lectura `0≤Δ_i≤R*_i`; no puede ser negativo. La lectura de Δ negativo como “sobreasunción” pertenece a la forma de diferencia absoluta y no se conserva en la forma multiplicativa.

No se debe usar una forma u otra indistintamente. La elección aquí es coherente si el objetivo es medir qué parte de la cuota externa R* aún no está integrada por φ₂. Los usos donde α significa valor monetario, pago, reparación o acto legal requieren una transformación por dominio; no se pueden insertar directamente en la misma resta.

**Resultado de este tramo:** `α` es un resumen escalar compatible con la operación canónica de `φ₂` bajo una definición por evento; para el déficit de la cuota causal, `Δ=R*(1−α)` expresa el residuo proporcional. `R*−α` solo corresponde a otro contrato, donde α ya es una cuota absoluta comparable.



## 10. Espacios formales, φ₁ y distribución de modos

### 10.1. Espacio de Hilbert y embedding

Axiomatización adopta un espacio de Hilbert separable E para definir normas, productos internos, la integral de Bochner y la convergencia del método de potencias. La completitud, separabilidad y elección de producto interno son **estructura matemática añadida para formalizar operaciones**; no se deducen por sí mismas de la ontología del ego.

Para conectar una aplicación con E, el Axioma 0 postula `emb: Outputs→E` y pide que preserve relaciones de orden/similitud relevantes. Esta es una condición de modelado explícita. En la normalización, toda cantidad que entre en una fórmula vectorial debe declarar qué dato representa, qué regla lo inserta en E y qué propiedad del dato conserva.

### 10.2. Tipo de φ₁

La fórmula canónica es `φ₁(v_t,c_t)	o a_t`; la historia acumulada aparece como argumento de `φ₂(a_t,I(t))). Axiomatización amplía φ₁ a `φ₁:V×C×H→A` y, además, incluye una referencia a I(t) dentro de v_t. Esa versión puede ser un modelo computacional expandido, pero no es una mera reescritura de la firma canónica: coloca historia en el input de φ₁ y puede contarla dos veces.

**Normalización:** conservar como firma ontológica `φ₁:V×C→A`. Si un modelo concreto requiere que la historia afecte la producción del acto, explicitar si esa historia forma parte de v_t o si se introduce una extensión de φ₁; no incluirla en ambos sitios de manera implícita. La actualización egoica posterior sigue pasando por `φ₂`.

### 10.3. Softmax sobre los seis modos

Axiomatización propone logits `z_k` y:

`h_k(v_t)=exp(z_k)/Σ_{j∈K}exp(z_j)`, `K={1,…,6}`.

De la fórmula sí se derivan positividad y normalización `Σ_k h_k=1`. El cambio de las sigmoides independientes a softmax corrige correctamente el defecto de que seis sigmoides puedan sumar cualquier valor entre 0 y 6. Esa corrección algebraica no demuestra que las seis posiciones ontológicas sean probabilidades empíricas. La interpretación de `h_k` como distribución probabilística requiere definir la correspondencia de cada logit con una posición de la voluntad y qué significan los parámetros.

**Normalización:** conservar softmax como formalización de una distribución sobre seis modos cuando ese sea el objeto que se pretende modelar; distinguir “distribución del modelo” de “probabilidad observada/estimada” y fijar los parámetros por la semántica del sistema. La suma uno de softmax no convierte por sí sola puntuaciones en frecuencias o probabilidades validadas.

## 11. Integral de Bochner y actualización de φ₂

### 11.1. Existencia de la integral

Axiomatización define:

`I(t)=∫₀ᵗ c(τ)w(τ)dτ∈E`.

La existencia de la integral de Bochner se sigue si E es Banach, c es fuertemente medible e integrable, w es medible y el producto es integrable. Las hipótesis del libro (c esencialmente acotada, w medible y acotada, intervalo temporal finito) bastan para esa existencia. Es un teorema matemático válido **dentro de esas hipótesis**.

Su correspondencia con el I(t) canónico requiere que `c(τ)w(τ)` represente el aporte de cada ciclo que φ₂ integró. Si c representa todos los colapsos producidos, el integrando debe incluir la operación de integración correspondiente; de otra forma, I acumula también lo que la ontología distingue de lo asumido. La integral de Bochner formaliza la suma continua de vectores; no determina por sí misma qué eventos acepta φ₂.

### 11.2. Irreversibilidad

El Teorema 2.1 de Axiomatización intenta derivar que `||I(t₂)−I(t₁)||>0` si `w>0` y `c
e0` en un conjunto de medida positiva. Ese paso no se desprende de la no nulidad puntual del integrando: en un espacio vectorial, contribuciones no nulas pueden cancelarse en la integral. Por ejemplo, en E=ℝ, `c=1` en la primera mitad del intervalo y `c=−1` en la segunda, con w=1, produce integral cero aunque c nunca sea cero en esos tramos.

La ontología de irreversibilidad histórica no equivale automáticamente a monotonía de la norma de un vector integral. Si I es una trayectoria acumulada de historia, su representación debe preservar que los actos asumidos ocurrieron incluso cuando sus componentes vectoriales se compensen. El teorema actual afirma una propiedad más fuerte que la que sus hipótesis demuestran.

### 11.3. Registro RSC y diferencia

`RSC(t)={c(τ):0≤τ≤t}` es llamado conjunto de colapsos producidos. Como imagen de una función, un conjunto pierde multiplicidad y orden cuando dos tiempos producen el mismo c; la integral temporal, en cambio, depende de esos tiempos y pesos. Para conservar la historia necesaria, el registro debe ser una secuencia/medida de eventos identificados por tiempo, actor y aporte, no solo el conjunto de valores de c.

Tampoco se puede formar `RSC(t)\I(t)` cuando RSC es un conjunto de eventos y I un vector acumulado. La operación correcta debe separar el conjunto de eventos producidos del de eventos integrados y reservar I para su agregación. Así se puede calcular α sobre eventos sin confundir inventario con suma.

### 11.4. Regla de umbral para φ₂

Axiomatización postula la actualización:

`φ₂(a,I)=I+δ(a)·1_{eval(a,I)>θ}`.

Esta es una formalización discreta de aceptación/rechazo: si se cumple el umbral, añade δ(a); si no, deja I igual. La aritmética es válida si `δ(a)∈E` y `eval` es una función bien definida. Pero la forma aditiva y la decisión binaria son supuestos de modelo; la ontología canónica presenta φ₂ como integración/asunción y la fórmula general no impone ese umbral binario. Para usarla como instancia, `eval`, `θ` y `δ` deben representar esa operación, y la historia rechazada debe permanecer registrada sin incorporarse a I.



## 12. Alcance externo de α y lectura de Δ

### 12.1. Evidencia de φ₂ y acceso del tercero

La definición canónica de φ₂ describe una operación interna de asunción. *Areópago* distingue esa operación de la pertenencia causal externa: el tercero puede reconstruir actos y cadenas, pero no observa directamente la asunción interna (cap. V, pp. 36–37, y discusión del acceso asimétrico). Por eso, en una contabilidad externa, los documentos pueden probar actos, expresiones y compromisos observables; no se identifican automáticamente con el estado interno de φ₂.

En la tabla 4.1 de Axiomatización, la profundidad `f) se obtiene del número de documentos que “confirman la integración” y el alcance `g) del número de dominios afectados. La operación es calculable una vez definidos los conteos, pero contar documentos no equivale por definición a medir la integración en I(t): un mismo contenido puede duplicarse entre documentos, y el número de dominios alcanzados no expresa necesariamente la profundidad de asunción. Por su parte, `n_ref` se ancla a niveles E0–E8 mediante intervalos de cantidad documental, lo que mezcla clasificación de evidencia con número de documentos.

**Normalización:** presentar `f) y `g) como reglas operativas de evidencia solo si esa es la magnitud que el expediente quiere medir. Para llamarlas medida de φ₂, la regla debe identificar observables que demuestren la integración del acto y mantener el acceso asimétrico que establece el canon. Los valores `0.3,0.6,1.0` y los intervalos de conteo son anclajes de la operación, no se derivan de la fórmula de la mediación bis.

### 12.2. Separar fracción interna de cuota causal y responsabilidad atribuida

Hay tres cantidades que los libros tienden a escribir con símbolos cercanos:

- `α_i): grado/proporción de integración de los actos propios del nodo i mediante φ₂;
- `R*_i): cuota relativa de posición/influencia causal calculada por el modelo de grafo;
- `L_i): cuota de responsabilidad que un tercero, una institución o un tribunal asigna a i.

No son la misma cantidad. El canon hace depender la imputación externa del acto y de la posición causal; la asunción interna de φ₂ es otra operación. Para convertir el grado de integración `α_i∈[0,1]` en una cantidad comparable con `R*_i), puede definirse dentro del modelo:

`A_i := α_i R*_i`  (cuota causal de i integrada por φ₂),

y entonces:

`Δ_i := R*_i − A_i = R*_i(1−α_i)`.

Esta lectura mantiene `Δ_i≥0) y expresa la porción de la cuota causal de i que no ha integrado. Es el contrato coherente si `α_i` es fracción de la cuota propia de i. Debe tratarse como definición de la relación cuantitativa entre R* y α, no como una identidad ontológica independiente del significado de R*.

La versión `R*_i−α_i` solo es comparable si el símbolo que se resta ya es una **cantidad absoluta** `A_i) en la misma escala global, no un grado de integración entre 0 y 1. Si además se quiere medir sobreasignación o carga impuesta a un actor, eso corresponde a comparar `L_i) con `R*_i), por ejemplo `Ω_i:=L_i−R*_i); no debe interpretarse como φ₂ ni como déficit de asunción interna.

### 12.3. Teoremas de Δ bajo cada contrato

- Para `Δ_i=R*_i−α_i), con ambos en [0,1], la cota `Δ_i∈[−1,1]) es correcta. El signo negativo significa únicamente `α_i>R*_i`; llamarlo “sobreasunción” requiere la definición del denominador de α. No demuestra que i haya cargado una responsabilidad que pertenece a otro.
- Para `Δ_i=R*_i(1−α_i)), con `R*_i,α_i∈[0,1]), se obtiene `0≤Δ_i≤R*_i≤1). El caso negativo queda excluido por construcción, así que no puede usarse para detectar chivo expiatorio ni transferencia de carga.
- La identidad diferencial `dΔ_i/dt=dR*_i/dt−dα_i/dt) solo corresponde a la primera definición. Para la forma multiplicativa:
  `dΔ_i/dt=(1−α_i)dR*_i/dt−R*_i dα_i/dt`.
  Ambas requieren diferenciabilidad; si los nodos/aristas cambian discretamente, se usa la diferencia entre versiones del modelo y no una derivada continua sin especificar interpolación.
- La Proposición 5.2 de Axiomatización (`Δ_i<0) y grafo completo implican que existe j con `Δ_j>0)) no se sigue de sus propias hipótesis. El libro afirma que `ΣR*=1), pero no impone `Σα=1`; por ello no hay conservación de suma que obligue a que exista otro déficit positivo. Contraejemplo: `R*=(0.5,0.5)), `α=(0.6,0.6)) da `Δ=(-0.1,-0.1)) con ambas componentes negativas. La inferencia “i asumió lo que pertenece a j” necesita una regla de transferencia entre nodos, que no está contenida en `Δ_i=R*_i−α_i).

**Normalización adoptada en este registro:** usar `α_i) para integración interna relativa y `A_i=α_iR*_i) para la cuota integrada global; usar `Δ_i=R*_i(1−α_i)) para residuo causal no integrado; reservar una variable distinta como `L_i) para atribución externa y `Ω_i=L_i−R*_i) si se quiere medir sobreasignación. Estos símbolos separan las operaciones que el canon mantiene separadas.

## 13. Escala de conocimiento, Fisher y Cramér–Rao

La Parte VII de *Axiomatización* agrega un modelo estadístico de observación Bernoulli. No se deriva de la ontología: formaliza una hipótesis concreta sobre cómo se observa una de las posiciones (h_k).

Si (X\sim\mathrm{Ber}(p(\theta))), la información de Fisher correcta para el parámetro escalar θ es
\[
\mathcal I_1(\theta)=\frac{[p'(\theta)]^2}{p(\theta)[1-p(\theta)]}.
\]
La expresión del libro (h_k(1-h_k)/\tau^2) solo coincide bajo el modelo logístico binario (p=h_k=\sigma((\theta-\theta_k)/\tau)), con pendiente (p'=p(1-p)/\tau). No se obtiene de una softmax de seis modos sin especificar el muestreo: tratar cada (h_k) como Bernoulli independiente ignora que las seis probabilidades suman uno y que las categorías son mutuamente excluyentes. Para una observación categórica (K\sim\mathrm{Categorical}(h_1,\ldots,h_6)), debe usarse la matriz de Fisher multinomial del vector de parámetros; sus componentes dependen de los gradientes de todos los logits.

Bajo condiciones regulares, (n) observaciones independientes y el modelo Bernoulli anterior, son correctas las cotas marginales:
\[
\mathrm{Var}(\widehat\theta)\ge\frac{1}{n\mathcal I_1(\theta)},\qquad
\mathrm{Var}(\widehat p)\ge\frac{p(1-p)}n.
\]
Al multiplicarlas se obtiene τ²/n² para ese modelo particular, y por tanto
\[
\sqrt{\mathrm{Var}(\widehat\theta)\mathrm{Var}(\widehat p)}\ge\frac{\tau}{n}.
\]
El libro luego presenta (n(\Delta I\,\Delta h)\ge4\tau^2). Esa desigualdad no se deriva: en la prueba la cota directa es (\tau), no (4\tau^2); el paso que introduce el factor 4 mezcla máximos separados y cambia además la potencia/unidad de τ. La corrección publicable es conservar la cota demostrada (\Delta I\Delta h\ge\tau/n), condicionada al modelo, o retirar la REC fuerte. τ_eff=τ/\sqrt n es una definición de escala compatible con el error de una media muestral, pero no convierte por sí misma (I(t)), una integral acumulativa, en promedio de (n) observaciones.

## 14. Sustitución estructural y supuesta cota espectral

El índice
\[
S_{est}(i)=1-\frac{D_{KL}(R^*\Vert R^{*(i)})}{\log m}
\]
es una medida de cambio de distribución al sustituir un nodo/fila. Su rango ([0,1]) no está garantizado: (D_{KL}) puede exceder λog (m), así que (S_{est}<0); KL también exige soporte compatible y una convención cuando hay ceros. El índice no equivale al contra-fáctico canónico “si retiro esta condición, ¿desaparece el daño?”. Debe renombrarse como sensibilidad de centralidad por sustitución, dejando separada la necesidad causal (N_i(D)).

La cadena del Lema 8.1 no demuestra la cota (R^*(E)\le(1-S_{est})/(m-1)). La cota de Pinsker (con la convención usual) sí relaciona KL con distancia total; sin embargo, el Lema A.3 supone una relación Lipschitz entre cambio de fila y cambio del eigenvector sin probar una cota inferior de estabilidad, y escribe el factor del gap en el sentido incorrecto. Davis–Kahan aplica directamente a matrices simétricas/hermitianas bajo condiciones de separación espectral; (W) es generalmente no simétrica, de modo que ese teorema no se puede invocar tal cual. En A.5 la corrección ε no queda acotada por 0.01 a partir de las hipótesis indicadas, y se pasa de una estimación alrededor de (1/m) a una cota sin ese término. La tabla numérica no remedia el salto.

**Normalización:** conservar (S_{est}) solo como descriptor calculado por perturbación y reportar (R^*(i)), (R^{*(i)}), KL, soporte, gap y método numérico. Eliminar del texto de resultados las cotas y teoremas 8.1–8.4 que dependen de A.5, salvo que se reemplacen por hipótesis y una demostración válidas para la clase de matrices efectivamente usada.

El Lema 8.2 tampoco se sigue de (R^*(D)>R^*(E)): para inferir (R^*(D)>1/m) hay que saber que D es el máximo global entre los (m) nodos. Que D supere a un ejecutor particular no basta.

## 15. Axiomas de visibilidad, TIC e índice de inversión

Las reglas
\[
V(i)=n_{doc}(i)/n_{total},\quad \phi(V)=1-(1-V)^{1.54},\quad
\psi(x)=0.21x^{-0.55}
\]
son operacionalizaciones/ajustes añadidos, no consecuencias de φ₁/φ₂. (V) mide proporción de documentos que mencionan al nodo, no fuerza causal ni evidencia independiente; el conteo es sensible a duplicados y tamaño del expediente. ψ diverge en (x=0) y el coeficiente 0.21 no garantiza que ψ permanezca en ([0,1]). Para uso numérico se necesita una función acotada, dominio explícito, regla de cero y una calibración identificable. Los valores α_vol, β, (h) y límites usados en los teoremas son supuestos de escenario; sin datos y procedimiento de estimación reproducibles, no son resultados demostrados.

El TIC está condicionado por dichas reglas y por cotas que no quedaron probadas; por ello las conclusiones Δ(D)>0 y Δ(E)<0 no son teoremas generales. Pueden presentarse como **proposición condicional del modelo**: si se imponen cotas explícitas (R_D\ge r_D), (R_E\le r_E), α_D\le a_D), α_E\ge a_E), entonces la inversión se sigue exactamente cuando (r_D>a_D) y (r_E<a_E). Esto aísla las condiciones suficientes sin simular que la ontología fija sus números.

La definición
\[
I_{inv}=\frac{|\Delta_D|}{|\Delta_E|}
=\frac{R_D-\alpha_D}{\alpha_E-R_E}
\]
solo vale cuando la inversión ya existe (Δ_D>0, Δ_E<0) y el denominador es distinto de cero. Si no, usar el cociente de valores absolutos y etiquetarlo como razón de brechas, no como índice de inversión. La monotonía en (S_{est}) no sale de una cota superior: una cota no determina la derivada del valor real de (R_E). Tampoco “decrece en (V(D)/V(E))” se deduce de ser φ creciente; el cociente introduce dependencia no probada y (V(E)=0) lo hace indefinido. La expresión “fraude annona inevitable” es una definición/diagnóstico condicional, no un teorema ontológico.

## 16. Modelo predictivo, logits y clausura

La regresión logística
\[
P(y=1\mid\Psi,c)=\sigma(\beta^T\Phi(\Psi,c))
\]
es un modelo estadístico admisible si se definen observaciones, variables y estimación. La matriz de diseño puede contener Ψ; esto no vuelve a cada coeficiente una medida ontológica ni convierte la predicción en imputación causal.

El Lema 9.1 afirma que (\ell_k=\logit(h_k)) es lineal en (I) cuando cada umbral θ_k es lineal. En softmax,
\[
\ell_k=z_k-\log\sum_j e^{z_j};
\]
el término log-suma-exp generalmente es no lineal en (I). Además, la afirmación de que ese término “no depende de (I)” contradice (z_j(I)). Solo en casos especiales (por ejemplo, dos modos, o pendientes iguales con cancelación apropiada) se obtiene linealidad. La normalización es retirar esa conclusión general y ajustar Φ explícitamente, usando logits como transformaciones observadas o una base no lineal.

La tabla τ→error mínimo no es fórmula deducida ni cota universal. τ no determina por sí sola el error Bayes: también importan prevalencia, separación de logits, ruido y especificación del predictor. Mantenerla únicamente como calibración empírica con datos, tamaño muestral y protocolo.

La clausura de (Ego(t)) (Teorema 10) es topología abstracta y no produce una fórmula de responsabilidad. Para usar compacidad/Bolzano–Weierstrass hacen falta acotación y espacio de dimensión finita (o hipótesis de compacidad en dimensión infinita); un conjunto cerrado en Hilbert no es por sí solo compacto. Esta parte puede quedar como resultado formal separado si las hipótesis se declaran correctamente.

## 17. Fórmulas de daño y beneficio: unidad, partición y atribución

El cálculo base del daño es
\[
D_{total}=T_{invertido}+T_{impedido}+\Delta T_{trayectoria}.
\]
Es una suma admisible solo si los tres términos se expresan en una misma unidad y corresponden a componentes mutuamente excluyentes del contrafáctico. Las etiquetas “daño emergente”, “lucro cesante” y “trayectoria” no demuestran que no haya solapamiento: una pérdida salarial futura puede aparecer en lucro cesante y trayectoria a la vez. Se debe definir cada componente como una partición de la diferencia entre trayectoria sin daño y trayectoria observada, con horizonte, descuento y regla anti doble conteo. La fórmula integral del §6.5 mezcla una diferencia instantánea (X(t_0^-)-X(t_0^+)), una integral de niveles y una integral descontada; sus unidades no coinciden si (D(t)) es nivel de bienestar, y los intervalos escritos tampoco garantizan que los rubros del libro sean disjuntos. Se normaliza como una única integral del déficit de bienestar más un salto inicial, o como una contabilidad por partidas, sin sumar ambos enfoques.

La conversión (D_{vital}=M/w_{ref}) es aritméticamente válida si (w_{ref}) tiene unidades monetarias/hora y se fija periodo, moneda real, población y base temporal. Es una conversión de unidad por convención del libro; no es un número de horas efectivamente sustraídas a una persona ni una consecuencia de φ₁/φ₂. El componente generacional ΣL_esperada(k)p(k|j) exige definir una cohorte contrafáctica finita y evitar contar descendencia potencial de varias víctimas en común; de lo contrario crece sin cota al extender generaciones. El componente supervivientes (L(1-q_{real})) requiere una línea base (q_{sin,daño}): la fórmula adecuada de pérdida relativa sería (L\max(0,q_{sin,daño}-q_{real})), con escalas de calidad definidas.

Para beneficio, (AD_{B,i}=R^*_{B,i}B_{total}) es una asignación proporcional añadida. (R^*_B) debe calcularse en un grafo específico del proceso de beneficio y sumar 1 en su población de nodos. La brecha Δ_B=R^*_B-β repite el problema dimensional de (R^*-α): si β es monto reembolsado, comparar primero montos (B_i^{causado}-B_i^{restituido}); si β es tasa relativa, definir (B_i^{restituido}/B_i^{causado}). Beneficio y daño son cuentas separadas y no se cancelan sin regla de compensación.

## 18. Índices agregados y herencia

El índice (J=1-\sum_i|R^*_i-\alpha_i|) está normalizado por ΣR*=1, pero el rango publicado es erróneo si α_i solo se restringe individualmente a [0,1]. Entonces (J\ge 1-m), y puede ser negativo (por ejemplo, (R^*=(1,0,0)), α=(0,1,1) da (J=-1)). (J=1) sí equivale a coincidencia componente a componente; (J=0) no significa “injusticia completa”: también ocurre para muchas configuraciones intermedias. Si se desea interpretar distancia entre distribuciones, exigir α en el simplex y usar (J_{TV}=1-\frac12\sum_i|R^*_i-\alpha_i|\in[0,1]). Si α representa asunción y no distribución, no normalizarla artificialmente: reportar (L_1) y Δ por nodo.

El índice (I_d=(R_d^*-α_d)/\max(1-\bar\alpha_{ej},\varepsilon)) es una razón ad hoc de brechas. No es necesariamente 0 cuando α_d=R_d^*: el numerador sí da cero entonces; puede ser negativo si el diseñador sobreasume; diverge por convención al saturarse α_ej. α promedio ponderada por R* de ejecutores requiere definir qué nodos cuentan como ejecutores y renormalizar sus pesos. Conviene rotularlo “razón de brecha del diseñador” y reportar numerador, denominador y ε.

Para herencia, (PH(t)=R^*_{hist}CI(t)HB(t)(1-RI(t))), las tres curvas exponenciales y (t_{presc}=\inf\{t\ge t_0:PH(t)<\varepsilon\}) son una dinámica propuesta, no derivación del canon. Los factores deben estar en [0,1], tener interpretación operacional, y no contar dos veces reformas dentro de (CI) y (RI). Con parámetros constantes, el umbral se obtiene resolviendo esa función; si las reformas son históricas, (\Delta RI(t)) debe ser una función acumulada definida. Las fechas numéricas de ejemplo dependen directamente de tasas escogidas, así que son escenarios, no estimaciones. “Prescripción ontológica” conviene tratar como nombre de indicador de umbral del modelo y no como conclusión de ontología.

La ecuación unificada (\sum_iw_{pos,i}|\Delta_i|f(S_i,t_i,CI_i)) es una familia de puntuaciones. Los pesos (w_{pos}), el factor (f) y sus instancias por dominio requieren definición y calibración; además, multiplicar Δ ya calculado por (1-S) puede descontar dos veces la sustituibilidad si esta ya intervino para definir responsabilidad neta. Presentarla como índice exploratorio dependiente de parámetros, nunca como igualdad exacta de “la injusticia”.

**Estado del cálculo hasta aquí:** del canon se extraen la cadena causal doblemente mediada, el análisis de condiciones necesarias, la atribución ordinal por posición y la distinción entre causalidad/asunción interna e imputación externa. La escala (R^*), los índices (S), (J), (I_d), las curvas históricas y la conversión monetaria son contratos de medición añadidos. Pueden operacionalizarse sin alterar la ontología, pero cada uno necesita unidades, reglas de entrada y una interpretación acotada. Para cerrar el inventario siguen pendientes las familias de fórmula por dominio (clínica, epidemiología, finanzas, historia/beneficio, diagnóstico/prometeo) y los algoritmos/casos numéricos que las instancian.


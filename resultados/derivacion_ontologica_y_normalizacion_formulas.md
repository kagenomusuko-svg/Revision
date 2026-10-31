# Derivación ontológica y normalización de las fórmulas
## Documento de trabajo acumulativo

**Versión:** 0.3  
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


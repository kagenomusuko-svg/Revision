# Derivación ontológica y normalización de las fórmulas
## Documento de trabajo acumulativo

**Versión:** 0.1  
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


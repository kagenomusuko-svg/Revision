# Puente entre la aritmética de Prometeo y Perron–Frobenius

**Estado:** reconstrucción matemática verificable; no constituye modificación del canon ontológico.  
**Fecha:** 31 de octubre de 2026.  
**Destino:** documento técnico complementario de la *Derivación ontológica y normalización de las fórmulas*.  
**Criterio editorial:** distinguir estrictamente (i) proposiciones de los textos, (ii) cálculos comprobados, (iii) formalizaciones propuestas y (iv) hipótesis todavía sin probar.

## 1. Pregunta y fuentes cotejadas

**Pregunta:** ¿puede justificarse la elección de Perron–Frobenius a partir de la aritmética causal de *El método Prometeo* y de la posición causal propuesta en *Areópago*, sin cambiar la ontología ni atribuir a un cálculo propiedades que no posee?

Fuentes directas:

- [*Areópago*, capítulo 4, sección III.C](https://github.com/kagenomusuko-svg/publicaciones/blob/main/reivindicacion-ontologica-del-ego/afrodita-areia/areopago/09.md): proporcionalidad según la **capacidad del nodo para determinar las condiciones de operación de los demás**, no según proximidad temporal; el canon requiere ordenación contextual, pero no prescribe una magnitud numérica única.
- [*Areópago*, capítulo 5](https://github.com/kagenomusuko-svg/publicaciones/blob/main/reivindicacion-ontologica-del-ego/afrodita-areia/areopago/10.md): prioridad **condicional** del diseño sobre la ejecución, atendiendo a necesidad del marco y sustituibilidad del ejecutor.
- [*Areópago*, capítulo 6](https://github.com/kagenomusuko-svg/publicaciones/blob/main/reivindicacion-ontologica-del-ego/afrodita-areia/areopago/11.md): especificidad con que el diseño determinó el resultado.
- *El método Prometeo: imputación causal para juristas y abogados*, edición 2026, §3.4, pp. impresas 74–78 (páginas 88–92 del PDF aportado): ejemplo del banco y cálculo por rondas.
- [*Axiomatización del sistema de la doble mediación*, Parte VI](https://github.com/kagenomusuko-svg/publicaciones/blob/main/metrologia-causal/axiomatizacion/09.md), definición 6.1 y teorema 6: autovector dominante de la matriz transpuesta.
- [Documento acumulativo de normalización](derivacion_ontologica_y_normalizacion_formulas.md), §§7, 22 y 26.

**Conclusión de alcance:** hay una **razón ontológica para medir el alcance causal de un nodo sobre otros**. Que esa razón seleccione un único autovector es una afirmación adicional que debe demostrarse. La formulación espectral no queda descartada; su dominio de aplicación debe precisarse.

## 2. Reproducción exacta de la aritmética del ejemplo de Prometeo

El caso tiene cinco nodos: banco **B**, departamento de riesgos **R**, asesores **A**, protocolo o instrumento **P** y resultado dañino **C**. El resultado C no participa como actor en la normalización de la ronda inicial.

Los pesos centrales publicados son:

| Arista | Peso | Arista | Peso |
|---|---:|---|---:|
| B → P | 0.90 | B → R | 0.69 |
| B → A | 0.86 | P → A | 0.64 |
| R → C | 0.70 | A → C | 0.49 |
| P → C | 0.64 | B → C | 0.80 |

Fijando el orden de actores $(B,R,A,P)$, la matriz de influencia **entre actores**, donde la fila es el origen y la columna el destino, es:

$$
W=\begin{pmatrix}
0&0.69&0.86&0.90\\
0&0&0&0\\
0&0&0&0\\
0&0&0.64&0
\end{pmatrix},
\qquad
d=\begin{pmatrix}0.80\\0.70\\0.49\\0.64\end{pmatrix}.
$$

El vector $d_i=w(i\to C)$ recoge las aristas directas desde cada actor al resultado.

**Ronda 0.** Se inicializa $x^{(0)}=(0.25,0.25,0.25,0.25)^\top$.

**Ronda 1.** Se computan influencias **entrantes** y se normalizan:

$$
u=W^\top x^{(0)}
=(0,\;0.1725,\;0.375,\;0.225)^\top,\qquad
\mathbf1^\top u=0.7725.
$$

$$
x^{(1)}=\frac{u}{\mathbf1^\top u}
=(0,\;0.22330097,\;0.48543689,\;0.29126214)^\top.
$$

Por construcción, el banco recibe cero en esta ronda: no tiene predecesores en el grafo.

**Ronda 2 publicada.** Para los tres nodos no diseñadores se multiplica su cuota de la ronda 1 por su arista directa al resultado; para B se introduce su peso directo $d_B=0.80$, **sin** multiplicarlo por $x_B^{(1)}=0$:

$$
q^{\mathrm{Prom}}=
\begin{pmatrix}
d_B\\ x_R^{(1)}d_R\\x_A^{(1)}d_A\\x_P^{(1)}d_P
\end{pmatrix}
=
\begin{pmatrix}
0.800000\\0.156311\\0.237864\\0.186408
\end{pmatrix}.
$$

Entonces:

$$
R^{\mathrm{Prom}}=\frac{q^{\mathrm{Prom}}}{\mathbf1^\top q^{\mathrm{Prom}}},\qquad
\mathbf1^\top q^{\mathrm{Prom}}=1.3805825.
$$

| Nodo | Aritmética verificada con pesos no redondeados | Porcentaje publicado (redondeado) |
|---|---:|---:|
| B | 57.9466 % | 58.0 % |
| R | 11.3221 % | 11.3 % |
| A | 17.2293 % | 17.2 % |
| P | 13.5021 % | 13.5 % |

**Resultado demostrado:** estas cifras se siguen de las dos rondas y la regla especial para el banco. El método es reproducible como aritmética finita. **No** es una simple aplicación reiterada de una única matriz a un vector: introduce una contribución directa nueva en la segunda fase, e interrumpe la iteración.

**Advertencia de tipado:** el porcentaje es una **cuota del puntaje generado por el algoritmo**. Interpretarlo directamente como porcentaje de daño causado exige una regla de identificación causal y reparto del daño, no solo la normalización $\sum R_i=1$.

## 3. Por qué esas dos rondas no son todavía el autovector de Perron–Frobenius

Con la matriz $W$ anterior se verifica:

$$
W^3=0,\qquad \rho(W)=0.
$$

Es una matriz no negativa **nilpotente**, porque el grafo histórico de actores es acíclico. No es irreducible ni primitiva.

Además, si se intenta usar $W^\top x=\lambda x$ con $\lambda>0$, la componente correspondiente al banco satisface:

$$
(W^\top x)_B=0=\lambda x_B\quad\Longrightarrow\quad x_B=0.
$$

Así, un eigenvector de **influencia entrante** no puede atribuir una componente positiva al nodo fuente B mientras B carezca de predecesores. Esta es una demostración directa de la incompatibilidad con el objetivo de dar cuenta de la **capacidad del banco para determinar a otros**.

La definición 6 de *Axiomatización* agrega un nodo sumidero sin aristas salientes. Esa estructura impide exigir simultáneamente irreducibilidad global. La matriz que tiene filas de actores con suma uno, pero fila del sumidero igual a cero, tampoco es estocástica por filas en su totalidad; por ello no puede deducirse para ella $\lambda_1=1$ usando la propiedad global $W\mathbf1=\mathbf1$.

**No es una refutación del criterio causal de *Areópago*.** Es una incompatibilidad entre una clase de grafos, una orientación del autovector y las hipótesis de un teorema que se desea utilizar.

## 4. Formalización propuesta: propagación causal finita orientada hacia el resultado

Para conservar la intuición aritmética —un actor adquiere alcance causal al determinar sucesores que a su vez determinan el resultado—, definimos un **puntaje de alcance causal propagado**, y no lo denominamos todavía cuota de responsabilidad.

Sea $W\ge0$ la matriz de actor a actor, $d\ge0$ el vector de conexión directa al resultado y $\beta\ge0$ un factor de propagación declarado. Para un grafo acíclico de longitud máxima $L$ entre actores, proponemos:

$$
c_\beta:=\sum_{k=0}^{L}\beta^kW^kd.
$$

Sus componentes se interpretan recursivamente:

$$
(c_\beta)_i=d_i+\beta\sum_jw_{ij}(c_\beta)_j.
$$

El término $d_i$ representa la incidencia directa; $w_{ij}(c_\beta)_j$ representa **una ruta de influencia desde i a través de j hacia el daño**. No exige que el nodo i reciba aristas entrantes. Conserva por eso la prioridad *potencial* del nodo que diseña condiciones para varios ejecutores, siempre que la evidencia y los pesos lo respalden.

Cuando $W$ es nilpotente, la serie termina exactamente y:

$$
c_\beta=(I-\beta W)^{-1}d
$$

para todo $\beta$ finito. La inversión existe porque los autovalores de $W$ son cero; la fórmula inversa es una notación compacta de sumas y multiplicaciones finitas, no un nuevo postulado ontológico.

**Demostración:** multiplicar la suma finita por $(I-\beta W)$ deja $d-\beta^{L+1}W^{L+1}d=d$, porque $W^{L+1}=0$.

### Cotejo numérico con el ejemplo, para $\beta=1$

$$
d=(0.80,\;0.70,\;0.49,\;0.64)^\top,
$$

$$
Wd=(1.4804,\;0,\;0,\;0.3136)^\top,
$$

$$
W^2d=(0.28224,\;0,\;0,\;0)^\top.
$$

Por tanto:

$$
c_1=d+Wd+W^2d=
(2.56264,\;0.70,\;0.49,\;0.9536)^\top.
$$

Normalizando **solo para obtener una comparación numérica**:

| Nodo | Puntaje de alcance $c_i$ | Cuota del puntaje $c_i/\sum_jc_j$ |
|---|---:|---:|
| B | 2.56264 | 54.45 % |
| R | 0.70000 | 14.87 % |
| A | 0.49000 | 10.41 % |
| P | 0.95360 | 20.26 % |
| **Total** | **4.70624** | **100 %** |

**Importante:** el 54.45 % NO reemplaza al 58.0 % de Prometeo. Son resultados de **operadores diferentes** sobre las mismas aristas. Esta comparación permite formular con precisión qué se conserva (el banco como nodo de mayor alcance en este caso) y qué cambia (la magnitud de las cuotas).

**Limitación sustantiva:** este índice suma productos por caminos. Si varias rutas representan el mismo mecanismo, pueden contarse varias veces; al subdividir una arista con nodos instrumentales puede cambiar el reparto normalizado. Deben probarse la independencia de mecanismos, el tratamiento de solapamientos y la invariancia ante representaciones equivalentes antes de convertir el puntaje en fracción de daño.

## 5. El puente demostrable con Perron–Frobenius

La propagación finita puede extenderse a grafos que tienen **retroalimentación real**, sin fingir que un grafo causal acíclico es fuertemente conexo. Para una matriz $W\ge0$ y $0\le\beta<1/\rho(W)$:

$$
c_\beta=(I-\beta W)^{-1}d
=\sum_{k=0}^{\infty}\beta^kW^kd.
$$

**Proposición (puente resolvente–Perron, condicional).** Supóngase que $W$ es no negativa e irreducible, que $\rho(W)>0$, que $d\ge0$ no es el vector cero y que $r>0$, $\ell>0$ son autovectores de Perron derecho e izquierdo, normalizados por $\ell^\top r=1$. Entonces:

$$
\boxed{\lim_{\beta\uparrow1/\rho(W)}
\frac{c_\beta}{\mathbf1^\top c_\beta}
=\frac{r}{\mathbf1^\top r},\qquad Wr=\rho(W)r.}
$$

**Demostración breve.** El eigenvalor $\rho(W)$ de una matriz no negativa irreducible es algebraicamente simple. Al acercarse $\beta$ a $1/\rho(W)$ por debajo, la resolvente admite el término dominante

$$
(I-\beta W)^{-1}
=\frac{r\ell^\top}{1-\beta\rho(W)}+O(1).
$$

En consecuencia:

$$
c_\beta=\frac{(\ell^\top d)r}{1-\beta\rho(W)}+O(1).
$$

Como $\ell^\top d>0$, al normalizar por la suma de componentes se obtiene el límite indicado. Fin de la demostración.

**Interpretación precisa.** Cuando hay retroalimentación efectivamente modelada y se admite un horizonte de propagación que se aproxima al umbral espectral, el **autovector derecho** emerge como **límite de una familia de sumas de caminos hacia el resultado**. Esto es un puente matemático real entre propagación y Perron–Frobenius, no una afirmación de identidad inmediata.

Para el método de potencias directo, una hipótesis suficiente más fuerte es que $W$ sea **primitiva**. No se debe confundir la convergencia de la resolvente normalizada con la convergencia de todas las iteraciones de potencias: en matrices irreducibles periódicas, las potencias pueden oscilar.

Para un grafo histórico acíclico, $\rho(W)=0$ y **no existe ese límite crítico de Perron**. La suma de caminos es finita y perfectamente calculable; no es legítimo añadir aristas causales ficticias solamente para que opere el teorema.

## 6. La dirección de las aristas decide qué magnitud se obtiene

Con $W_{ij}=w(i\to j)$:

- $W^\top x$ acumula **influencia recibida** por cada nodo desde sus predecesores; un nodo fuente puede quedar en cero.
- $Wd$ propaga **relevancia hacia atrás desde el resultado**, asignando a cada origen lo que alcanza a través de sus sucesores.
- $Wr=\rho r$, bajo las hipótesis correspondientes, caracteriza una centralidad espectral **de influencia saliente**.
- $W^\top r=\rho r$ caracteriza una centralidad espectral **de influencia entrante**.

Las dos últimas centralidades no son idénticas en general. Por tanto, la elección entre $W$ y $W^\top$ no es tipográfica ni puede resolverse únicamente por normalización: se fija mediante **la pregunta causal**.

## 7. Instrumentos sin voluntad y atribución al actor

En *Prometeo*, el nodo P (protocolo) conserva 13.5 % como nodo instrumental, aunque el propio manual dice que su influencia debería imputarse causalmente al banco que lo diseñó. No basta con mostrar esa cuota instrumental: se requiere una **regla explícita, sin duplicación**, para trasladarla al actor.

Una opción contable **condicional**, si se acredita que toda la cuota de P se asigna a B, es el mapa conservativo:

$$
\begin{pmatrix}R_B^{actor}\\R_R^{actor}\\R_A^{actor}\end{pmatrix}
=
\underbrace{\begin{pmatrix}
1&0&0&1\\
0&1&0&0\\
0&0&1&0
\end{pmatrix}}_{H}
\begin{pmatrix}R_B^{Prom}\\R_R^{Prom}\\R_A^{Prom}\\R_P^{Prom}\end{pmatrix}.
$$

En el ejemplo, esto daría aproximadamente $R_B^{actor}=71.45\%$, $R_R^{actor}=11.32\%$ y $R_A^{actor}=17.23\%$. **No es una conclusión del manual ni una adjudicación definitiva.** Es una transformación contable que requiere la regla causal $H$ sustentada por el expediente. Tampoco resuelve automáticamente el reparto de las rutas mediadas que ya están incluidas en otros componentes (por ejemplo, P → A). La clasificación del instrumento y la contabilidad por caminos necesitan reconciliarse para evitar duplicaciones.

## 8. Pruebas que debe superar la futura elección de operador

1. **Conservación semántica:** el índice debe medir una propiedad que corresponda a la posición causal, no a la visibilidad de documentos o a un simple número de conexiones.
2. **Causalidad contextual:** la necesidad del nodo para un daño específico se contrasta aparte con el contrafáctico pertinente. Ni centralidad entrante ni saliente lo demuestran automáticamente.
3. **Diseño y ejecución:** en condiciones pertinentes al postulado de *Areópago*, comprobar si el orden cuantitativo refleja la jerarquía reconstruida; no introducir forzosamente que B sea superior mediante una regla circular.
4. **Pesos:** mantener separadas la confianza evidencial $e_{ij}$ y la intensidad de determinación $w_{ij}$. La escala documental E0–E8 no determina por sí sola la intensidad causal.
5. **Representación y rutas:** detectar doble conteo cuando hay caminos solapados o nodos instrumentales, y comprobar sensibilidad ante subdivisión de aristas.
6. **Incertidumbre:** los escenarios mínimo, central y máximo por sí solos no prueban que el orden se conserve en **todo** el hiperrectángulo de pesos. Se requiere optimización, garantía matemática o muestreo descrito como exploratorio.
7. **Contraste de modelos:** ejecutar sobre los mismos grafos el operador literal de Prometeo, la propagación finita y (solo donde corresponda) el espectral. Informar resultados **sin** declararlos equivalentes a priori.
8. **Validación causal y jurídica:** ninguna suma de puntajes demuestra por sí misma que el porcentaje sea la parte material del daño ni determina su exigibilidad.

## 9. Resultado provisional y decisión de reconstrucción

**Demostrado aquí:** (a) las cifras del ejemplo del capítulo 3 se reproducen; (b) sus rondas son una regla finita híbrida, no un eigenvector fijo de Perron; (c) el grafo de actores del ejemplo es nilpotente y el enfoque $W^\top$ de influencia entrante asigna cero al banco; (d) una suma finita de caminos hacia el resultado expresa matemáticamente influencia propagada desde el origen; (e) bajo hipótesis adicionales explícitas, la **resolvente normalizada converge al autovector derecho de Perron–Frobenius**.

**No demostrado:** que las cuotas resultantes midan fracciones empíricas del daño; que la suma de caminos sea invariante al modo de representar el grafo; que el método literal de rondas y el operador de caminos coincidan; que el grafo ontológico de todo caso deba ser primitivo; o que los pesos E0–E8 tengan una interpretación causal cardinal ya calibrada.

**Orientación propuesta:** no cambiar la ontología ni retirar Perron–Frobenius. Primero preservar el cálculo aritmético original como *operador Prometeo por rondas*. Después estudiar la familia de propagación por caminos como posible puente formal. Utilizar la expresión espectral de Perron–Frobenius **cuando se cumplan sus condiciones**, con orientación de aristas y significado del índice expresamente justificados. Solo después decidir qué operador puede denominarse $R^*$ en un expediente de imputación y con qué grado de exigibilidad epistémica.

---

### Nota para la normalización editorial

Este documento complementa y precisa las secciones 7, 22 y 26 del inventario principal; no sustituye las definiciones canónicas. El hallazgo no es «Perron–Frobenius carece de fundamento ontológico», sino «la elección de una medida de alcance causal tiene motivación ontológica, y falta demostrar qué realización matemática satisface el contrato semántico y las hipótesis técnicas pertinentes».
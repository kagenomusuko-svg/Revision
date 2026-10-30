# Registro de comprobaciones matemáticas — v2.0

Todos los ejemplos están contenidos en `comprobaciones_matematicas_v2_0.py`. Requieren Python 3 y NumPy. Se usan cálculos exactos/sencillos o eigenvectores numéricos para verificar contraejemplos; no sustituyen una prueba general.

## MC-01 — Proposición 5.2, M10 pp. 34–35
**Enunciado:** Δ_i<0 en grafo completo implica algún Δ_j>0. **Hipótesis del texto:** R* no negativo/suma uno; α_i independientes en [0,1]; no conservación de Σα. **Cálculo:** W de 2×2 con entradas .5; R*=(.5,.5); α=(.8,.8); Δ=(-.3,-.3). **Resultado:** contraejemplo admisible y exacto. **Dependencia:** es apoyo explicativo del TIC, no premisa explícita de pruebas Thm8.1–8.2.

## MC-02 — Teorema 6, M10 pp. 38–41
**Objeto:** W aumentada con fila D=0. **Cálculo:** [[.4,.3,.3],[.2,.5,.3],[0,0,0]] tiene filasums (1,1,0), W1=(1,1,0); eigenvalores no obligan λ=1 para Wᵀ. **Resultado:** falla hipótesis/objeto de matriz completa; no se concluye imposibilidad universal para una submatriz distinta.

## MC-03 — W frente a Wᵀ
W=[[.9,.1],[.4,.6]]. **Resultados:** eigenvector derecho de W (.5,.5), de Wᵀ (.8,.2). **Implicación:** orientación cambia índice; hace falta semántica de filas/columnas.

## MC-04 — Pesos sin normalizar
W bruto [[9,1],[20,80]] da eigenvector derecho aprox (.01383497,.98616503). Normalizar filas → [[.9,.1],[.2,.8]] da (.5,.5). **Implicación:** normalización altera la clasificación.

## MC-05 — Lema 8.1, M10 pp.58–60; Ap.A
W de cinco filas iguales a p=(.30,.25,.15,.15,.15), estrictamente positiva. Reemplazar una fila por promedio de restantes no cambia W. KL=0, S_est=1, pero R_E=.25. **Resultado:** cota total R_E≤0 es falsa. Revisión del Ap.D.3 identifica luego R*_net, magnitud distinta; no repara el lema total.

## MC-06 — Lema 8.2
p=(.19,.18,.30,.20,.13) suma uno; matriz de filas idénticas tiene vector PF p. D=.19 es mayor que E=.18 pero menor que 1/5. **Resultado:** una comparación D>E no implica D>1/m; sí lo implica ser máximo global estricto, condición usada en la prueba.

## MC-07 — Contracción Banach, M01 pp.798–799
W=[[0,1,0],[.5,0,.5],[.4,0,.6]] es primitiva: la matriz es irreducible y hay lazo, por lo que aperiodicidad. Para e1,e2, las columnas normalizadas W e1/||...|| y W e2/||...|| tienen soportes disjuntos, distancia TV=1 antes y después. **Resultado:** no hay contracción estricta de una iteración en TV. Esto no niega convergencia de potencia bajo condiciones PF; refuta la demostración Banach tal como está formulada.

## MC-08 — ψ calibrada M10 Ap.B.1
ψ(x)=.21x^(-.55): ψ(.05)≈1.091; ψ(.01)≈2.644; no definida en 0; por tanto no mapea [0,1] a [0,1] como se declara sin restricciones/capado. Ajuste informado con n=3 no establece validación externa.

## MC-09 — Apéndice A (M10)
La desigualdad t ln t ≥ (t−1)+(t−1)^2/2 falla en t=2: 1.3863 < 1.5. Pinsker puede ser cierto por otros fundamentos. Davis–Kahan 1970 es un teorema de perturbación para operadores hermitianos; aplicarlo a matriz genérica no normal requiere justificación adicional.

## Dependencias afectadas
La cota de masa total de L8.1 no sustenta Thm8.2/8.3 ni las aplicaciones que usan el total; Thm8.1 usa L8.2 y límites paramétricos; Thm8.4 incluye premisas adicionales respecto de su formulación resumida. La versión neta R*_net puede sobrevivir como objeto nuevo, sujeto a definición y prueba propia. P5.2 es separable del esqueleto formal mostrado de TIC, aunque su narrativa de “compensador” queda sin base.

## Referencias primarias / estándar
Davis, C. & Kahan, W. M. (1970), “The Rotation of Eigenvectors by a Perturbation. III”, *SIAM Journal on Numerical Analysis* 7(1), DOI: https://doi.org/10.1137/0707001.
Rubin, D. B. (1974), “Estimating Causal Effects of Treatments in Randomized and Nonrandomized Studies”, *Journal of Educational Psychology* 66(5), 688–701.
Pearl, J. (1995), “Causal Diagrams for Empirical Research”, *Biometrika* 82(4), 669–688.
Pearl, J. (2010), “Causal Inference”, *Proceedings of the 3rd Annual ACM/IEEE Symposium on Logic in Computer Science*, 2010.

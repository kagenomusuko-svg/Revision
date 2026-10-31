"""Reproduce el ejemplo aritmetico del Metodo Prometeo y un puente espectral.

Datos: El metodo Prometeo, cap. 3, paginas impresas 74-78.
Las dos familias de puntajes son diferentes; no interpretar ninguna
como fraccion empirica de dano sin un modelo causal adicional.
Dependencias: solo la biblioteca estandar de Python.
"""

from math import isclose, sqrt

NODOS = ('B', 'R', 'A', 'P')
W = (
    (0.0, 0.69, 0.86, 0.90),
    (0.0, 0.0, 0.0, 0.0),
    (0.0, 0.0, 0.0, 0.0),
    (0.0, 0.0, 0.64, 0.0),
)
DIRECTO = (0.80, 0.70, 0.49, 0.64)


def accion(matriz, vector):
    return tuple(sum(a * b for a, b in zip(fila, vector)) for fila in matriz)


def transpuesta(matriz):
    return tuple(zip(*matriz))


def normalizar(vector):
    total = sum(vector)
    if total <= 0:
        raise ValueError('No es posible normalizar un vector de masa nula')
    return tuple(x / total for x in vector)


def prometeo_dos_rondas():
    uniforme = (0.25,) * 4
    ronda_1 = normalizar(accion(transpuesta(W), uniforme))
    q = (DIRECTO[0],) + tuple(ronda_1[i] * DIRECTO[i] for i in (1, 2, 3))
    return ronda_1, q, normalizar(q)


def propagacion_hacia_resultado():
    """c = d + Wd + W^2d; W^3 es nulo en este grafo."""
    term = DIRECTO
    total = [0.0] * 4
    for _ in range(4):
        total = [x + y for x, y in zip(total, term)]
        term = accion(W, term)
    assert all(abs(x) < 1e-12 for x in term)
    return tuple(total), normalizar(total)


def limite_espectral_ejemplo():
    """Ejemplo independiente con feedback autentico entre dos nodos."""
    a = ((0.4, 0.5), (0.3, 0.4))
    d = (1.0, 0.1)
    rho = 0.4 + sqrt(0.15)
    x = (0.5, 0.5)
    for _ in range(400):
        x = normalizar(accion(a, x))
    beta = 0.999 / rho
    # (I - beta*A) c = d: solucion exacta de sistema 2x2.
    x11, x12 = 1 - 0.4 * beta, -0.5 * beta
    x21, x22 = -0.3 * beta, 1 - 0.4 * beta
    det = x11 * x22 - x12 * x21
    c = ((x22 * d[0] - x12 * d[1]) / det,
         (-x21 * d[0] + x11 * d[1]) / det)
    y = normalizar(c)
    assert max(abs(i - j) for i, j in zip(x, y)) < 0.0005
    return rho, x, y


def main():
    ronda, bruto, publicado = prometeo_dos_rondas()
    assert isclose(sum(ronda), 1.0)
    assert isclose(sum(bruto), 1.3805825242718446, abs_tol=1e-11)
    assert isclose(publicado[0], 0.57946554, abs_tol=1e-8)
    assert isclose(publicado[1], 0.11322082, abs_tol=1e-8)
    assert isclose(publicado[2], 0.17229255, abs_tol=1e-8)
    assert isclose(publicado[3], 0.13502110, abs_tol=1e-8)
    alcance, cuotas = propagacion_hacia_resultado()
    assert all(isclose(a, b, abs_tol=1e-10) for a, b in
               zip(alcance, (2.56264, 0.70, 0.49, 0.9536)))
    print('Nodos:', NODOS)
    print('Prometeo, ronda 1:', ronda)
    print('Prometeo, porcentajes:', tuple(round(x * 100, 4) for x in publicado))
    print('Propagacion, puntajes:', alcance)
    print('Propagacion, porcentajes:', tuple(round(x * 100, 4) for x in cuotas))
    print('Ejemplo separado de feedback: radio, PF, resolvente:', limite_espectral_ejemplo())
    print('Todas las verificaciones se completaron.')


if __name__ == '__main__':
    main()

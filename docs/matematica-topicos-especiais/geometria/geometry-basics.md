# Geometria Básica

Em programação competitiva, a geometria é um tópico que envolve o estudo de figuras geométricas, tanto em 2D quanto em 3D, incluindo conceitos como pontos, linhas, polígonos, círculos, superfícies, poliedros, entre outros. Muitas vezes é necessário implementar algoritmos geométricos para resolver problemas que envolvem interseções, áreas, perímetros, distâncias, ângulos e outras propriedades geométricas.

Para isso, existem diversos algoritmos e estruturas dedicados a resolver problemas geométricos de forma eficiente. Abaixo estão alguns conceitos e algoritmos básicos de geometria que são frequentemente utilizados em programação competitiva.

## Definições Básicas

Alguns elementos são muito frequentes em problemas de geometria e aparecem em diversas definições e algoritmos.

```cpp
const ld EPS = 1e-9;

using poligono = vector<ponto>;

struct ponto {
    ld x, y;
};

struct circulo {
    ponto central;
    ld r;
};
```

## Pontos, Vetores e Operações Básicas

### Operações com Pontos e Vetores
```cpp
ponto soma(ponto a, ponto b){ return {a.x + b.x, a.y + b.y}; }

ponto dif(ponto a, ponto b) { return {a.x - b.x, a.y - b.y}; }

ponto mult(ponto a, ld k) { return {a.x * k, a.y * k}; } //ESCALAR

ponto div(ponto a, ld k) { return {a.x / k, a.y / k}; } // ESCALAR

ld norma2(ponto a) { return a.x * a.x + a.y * a.y; }

// Módulo ou norma de um ponto ou vetor
ld norma(ponto a) { return sqrt(norma2(a)); }

// Distância entre dois pontos
ld dist(ponto a, ponto b) { return norma(dif(a, b)); }

// Tornar um vetor unitário
ponto normalizar(ponto a) { ld n = norma(a); return {a.x / n, a.y / n}; }

// Rotaciona o ponto a em torno da origem por um ângulo ang (em radianos)
ponto rotacionar(ponto a, ld ang) {
    ld c = cos(ang), s = sin(ang);
    return {a.x * c - a.y * s, a.x * s + a.y * c};
}
```

### Produto Escalar
```cpp
ld produto(ponto a, ponto b) {
    return a.x * b.x + a.y * b.y;
}
```

### Produto Vetorial
```cpp
ld cross(ponto a, ponto b) {
    return a.x * b.y - a.y * b.x;
}
```

## Retas

```cpp
//INTERSECCAO 2 RETAS
bool intersecao_retas(ponto a1, ponto b1, ponto a2, ponto b2, ponto &p) {
    ponto r = dif(b1, a1);
    ponto s = dif(b2, a2);
    ld det = cross(r, s);
    if (fabsl(det) < EPS) return false; // PARALELAS OU COINCISAS
    ld t = cross(dif(a2, a1), s) / det;
    p = soma(a1, mult(r, t));
    return true;
}

// INTERSECCAO 2 SEGMENTOS
bool intersecao_segmentos(ponto a1, ponto b1, ponto a2, ponto b2, ponto &p) {
    ponto r = dif(b1, a1);
    ponto s = dif(b2, a2);
    ld det = cross(r, s);

    if (fabsl(det) < EPS) {
        if (fabsl(cross(dif(a2, a1), r)) > EPS) return false;
        if (max(min(a1.x, b1.x), min(a2.x, b2.x)) <= 
            min(max(a1.x, b1.x), max(a2.x, b2.x)) + EPS &&
            max(min(a1.y, b1.y), min(a2.y, b2.y)) <= 
            min(max(a1.y, b1.y), max(a2.y, b2.y)) + EPS) {
            p = a2; 
            return true;
        }
        return false;
    }

    ld t = cross(dif(a2, a1), s) / det;
    ld u = cross(dif(a2, a1), r) / det;

    if (t < -EPS || t > 1+EPS || u < -EPS || u > 1+EPS) return false;
    p = soma(a1, mult(r, t));
    return true;
}

//DETERMINA SE UM PONTO ESTA A ESQUERA DE UM ARESTA
bool left(ponto a, ponto b, ponto p) {
    return cross(dif(b, a), dif(p, a)) >= -EPS;
}
```

## Polígonos e Círculos
```cpp
// AREA DE POLIGNO
ld area(vector<ponto> &P) {
    ld A = 0;
    for (int i = 0; i < (int)P.size(); i++) {
        int j = (i + 1) % P.size();
        A += P[i].x * P[j].y - P[j].x * P[i].y;
    }
    return fabsl(A) / 2.0;
}

// INTERSECCAO DE POLIGNOS CONVEXOS 
vector<ponto> intersecao_poligonos(vector<ponto> P, vector<ponto> Q) {
    for (int i = 0; i < (int)Q.size(); i++) {
        ponto A = Q[i], B = Q[(i+1)%Q.size()];
        vector<ponto> novo;
        for (int j = 0; j < (int)P.size(); j++) {
            ponto C = P[j], D = P[(j+1)%P.size()];
            bool dentroC = left(A, B, C);
            bool dentroD = left(A, B, D);

            if (dentroC && dentroD) novo.push_back(D);
            else if (dentroC && !dentroD) {
                ponto inter;
                intersecao_retas(C, D, A, B, inter);
                novo.push_back(inter);
            }
            else if (!dentroC && dentroD) {
                ponto inter;
                intersecao_retas(C, D, A, B, inter);
                novo.push_back(inter);
                novo.push_back(D);
            }
        }
        P = novo;
        if (P.empty()) break;
    }
    return P;
}

//INTERSECAO RETA CIRCULO
vector<ponto> intersecao_reta_circulo(ponto a, ponto b, circulo c) {
    ponto d = dif(b, a);
    ponto f = dif(a, c.central);
    ld A = produto(d, d);
    ld B = 2 * produto(f, d);
    ld C = produto(f, f) - c.r * c.r;
    ld delta = B*B - 4*A*C;

    vector<ponto> ans;
    if (delta < -EPS) return ans;
    delta = max(delta, (ld)0.0);

    ld t1 = (-B - sqrt(delta)) / (2*A);
    ld t2 = (-B + sqrt(delta)) / (2*A);

    if (0 <= t1 && t1 <= 1) ans.push_back(soma(a, mult(d, t1)));
    if (0 <= t2 && t2 <= 1 && fabsl(t1-t2) > EPS) ans.push_back(soma(a, mult(d, t2)));
    return ans;
}

// INTERSECCAO 2 CIRCULOS
vector<ponto> intersecao_circulos(circulo c1, circulo c2) {
    vector<ponto> ans;
    ld d = dist(c1.central, c2.central);
    if (d > c1.r + c2.r + EPS) return ans;
    if (d < fabsl(c1.r - c2.r) - EPS) return ans;
    if (d < EPS && fabsl(c1.r - c2.r) < EPS) return ans; // infinitos pontos

    ld a = (c1.r*c1.r - c2.r*c2.r + d*d) / (2*d);
    ld h = sqrt(max((ld)0.0, c1.r*c1.r - a*a));
    ponto P = soma(c1.central, mult(dif(c2.central, c1.central), a/d));
    ld rx = -(c2.central.y - c1.central.y) * (h/d);
    ld ry =  (c2.central.x - c1.central.x) * (h/d);

    ans.push_back({P.x + rx, P.y + ry});
    if (h > EPS) ans.push_back({P.x - rx, P.y - ry});
    return ans;
}
```

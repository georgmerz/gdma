# Kapitel 5 - Matrizen



## 4.1 Lernziele
In diesem Abschnitt lernen wir die folgenden Dinge:

- 
- 
- 
- 

:::{admonition}  Lernziele
:class: note

- 
- 
- 
- 
:::

## 4.2 Was ist eine Matrix - z.B. ein Graustufenbild.
Eine Matrix ist nichts kompliziertes. Im Wesentlichen handelt es sich um eine tabelleraische Anordnung von Zahlen mit Spalten und Zeilen um die wir runde Klammern machen.
Das kann so aussehen:
```{math}
\begin{pmatrix} 1&3&8\\ 1&9& 13 \end{pmatrix}
```
Oder aber wenn wir es mit vielen Daten zu tun haben auch mal so:
![](images/big_matrix.png)

Matrizen spielen eine Wichtige Rolle immer wenn es um Daten geht. So lassen sich Datentabellen als Matrizen interpretieren, wenn die Werte rein aus Zahlen bestehen. 
Matrizen spielen ebenso in der Bildverarbeitung eine Wichtige Rolle.
Am einfachsten wird diese Verbindung bei Graustufenbildern.

Die Pixel des Bildes ergeben die tabellarische Anordnung. Der Wert wird durch die Intensität des einzelnen Pixels gegeben.

So ergibt beispielsweise folgendes Bild:

![](images/schnupper.png)

Folgende Matrix:

![](images/matrix_schnupper.png)


**Skalare Multiplikation**

Wir können nun das Bild bearbeiten in dem Wir die Matrix verändern.
Beispielsweise können wir jeden Wert mit 2 Multiplizieren: 

![](images/2_matrix.png)

Was bedeutet diese Operation auf der Ebene des Bildes?

Es ist eine Erhöhung des Kontrasts:

![](images/contrast_schnupper.png)

**Matrix Addition**
Sei nun ein weiteres Bild gegeben:

![](images/thb_logo.png)

Wir nehmen nun weiter an, dass beide Bilder und damit auch die zugehörigen Matrizen die gleiche Größe besitzen.
Wir wollen nun beide Bilder übereinanderlegen. Dies können wir durch Addition der beiden entsprechenden Matrizen schaffen. D.h. in jeder Komponente addieren wir einfach die beiden Zahlen miteinander, so dass eine neue Matrix der gleichen Größe entsteht.
![](images/addition_matrix.png)


## 4.3 Matrixnotation
In diesem Kapitel wollen wir uns mit der Matrixschreibweise bekannt machen und einige Formale Notationen einführen.

### Matrizen
Wir verwenden als Namen für Matrizen häufig Großbuchstaben. Zum Beispiel


```{math}
B=\begin{pmatrix} 1&3&8\\ 1&9& 13 \end{pmatrix}
```
Die Matrix $B$ hat in diesem Fall 2 Zeilen und 3 Spalten. Wir nennen sie auch eine $2\times 3$ Matrix.

Wir schreiben eine Allgemeine $m\times n$ Matrix wie folgt hin:

```{math}
A = \begin{pmatrix}
a_{11} & a_{12} & \ldots & a_{1n} \\
a_{21} & a_{22} & \ldots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \ldots & a_{mn}
\end{pmatrix}
```
Wir nennen $m\times n$ auch die **Dimension** der Matrix A.

Obige Struktur bedeutet, dass wenn wir für eine Matrix $A$ den Wert $a_{ij}$ schreiben, dass wir den Wert in der $i$-ten Zeile und der $j$-ten Spalte meinen.


**Frage**

Im obigen Beispiel was ist $b_{12}$?

**Antwort:**
```{toggle}
$b_{12}=3$
````

Im nächsten Schritt müssen wir definieren welchen Wertebereich die einzelnen Zahlen in der Matrix haben sollen.
In der Regel wollen wir dass die Zahlen in $\mathbb{R}$ sind.

Wir schreiben dann für die Menge aller Möglichen $m\times n$  Matrizen mit reellen Zahlen
```{math}
\mathbb{R}^{m\times n}
```

### Vektoren

Eine $n\times 1$ Matrix nennen wir **Spaltenvektor** oder **Vektor**. 
Zum Beispiel $v=\begin{pmatrix} 1\\2\\3\\4 \end{pmatrix}$.
Wir schreiben statt $\mathbb{R}^{n\times 1}$ einfach nur $\mathbb{R}^n$.

Eine $1\times n$ Matrix nennen wir **Zeilenvektor**.
Zum Beispiel $v=\begin{pmatrix} 1 & 2 & 3 & 4 \end{pmatrix}$.
Spalten- und Zeilenvektoren bezeichnen wir in der Regel mit einem kleinen lateinischen Buchstaben (z.B. $v,w,u$).


### Skalar

Fall wir im Kontext der Matrizen und Vektorrechnung betonen wollen, dass es sich bei einem Objekt um ein einzige Zahl (z.B. in $\mathbb{R}$) handelt. Wir schreiben, dann häufig einen kleinen griechischen Buchstaben um das zu kennzeichnen (z.B. $\lambda \in \mathbb{R}$)

### Besondere Matrizen

Wir wollen noch zwei Besondere Matrizen einführen, die es verdienen eine abkürzende Schreibweise zu bekommen.

Zunächst die sogenannte, **Nullmatrix**.
$\mathbf{0}_{mn} \in \mathbb{R}^{m\times n} $. Dies bezeichnet eine $m\times n$ Matrix, welche nur aus Nullen besteht. Ist im Kontext klar, welche Dimension $m\times n$ gemeint ist, so schreiben wir abkürzend auch nur $\mathbf{0}$.

Zum Anderen die sogenannte **Einheitsmatrix**.

```{math}
E_n\begin{pmatrix}
1 & 0 & \ldots & 0 \\
0 & 1 & \ldots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \ldots & 1
\end{pmatrix}\in \mathbb{R}^{n\times n}
```
Dies ist eine spezielle Art von Matrix, bei der die Diagonalelemente 1 sind und alle anderen Elemente 0.



## 4.3 Skalare Multiplikation und Matrixaddition

Die skalare Multiplikation und die Matrixaddition sind fundamentale Rechenoperationen für Matrizen.
Wir starten zunächst mit der Matrixaddition.

### Matrixaddition

````{prf:definition}
Gegeben seien zwei Matrizen $A,B\in \mathbb{R}^{m\times n}$ mit derselben Dimension $m \times n$. Die Addition von $A$ und $B$, dargestellt als $A + B$, ergibt eine neue Matrix $C$ der gleichen Dimension $m \times n$, wobei jedes Element $c_{ij}$ in $C$ definiert ist als:
```{math}
c_{ij} = a_{ij} + b_{ij} \quad \text{ für alle} 1 ≤ i ≤ m \text{ und } 1 ≤ j ≤ n.
```
````
Machen wir dazu ein einfaches Beispiel.

````{prf:example}
```{math}
\begin{pmatrix}
2 & 4 & 6 & 8 \\
1 & 3 & 5 & 7 \\
0 & -1 & -2 & -3 \\
\end{pmatrix}
+
\begin{pmatrix}
-1 & -3 & -5 & -7 \\
4 & 2 & 0 & -2 \\
3 & 1 & -1 & -3 \\
\end{pmatrix}
=
\begin{pmatrix}
1 & 1 & 1 & 1 \\
5 & 5 & 5 & 5 \\
3 & 0 & -3 & -6 \\
\end{pmatrix}

```
````


### Skalare Multiplikation
````{prf:definition}


Sei $ A\in \mathbb{R}^{m\times n}$ eine $m \times n$ Matrix ist und $\lambda\in \mathbb{R} $ ein Skalar. Dann ist die skalare Multiplikation $C=\lambda\cdot A$ eine $m \times n$ Matrix, bei der 
```{math}
c_{ij}=\lambda\cdot a_{ij} \quad \text{ für alle} 1 ≤ i ≤ m \text{ und } 1 ≤ j ≤ n.
```
````
Machen wir dazu ein einfaches Beispiel.

````{prf:example}
Sei $A$ eine $2 \times 3$ Matrix und $\lambda = 3$ ein Skalar. Die skalare Multiplikation von $A$ mit $\lambda$ ergibt:

```{math}
\lambda A = 3 \cdot \begin{pmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
\end{pmatrix}
= \begin{pmatrix}
3 \cdot 1 & 3 \cdot 2 & 3 \cdot 3 \\
3 \cdot 4 & 3 \cdot 5 & 3 \cdot 6 \\
\end{pmatrix}
= \begin{pmatrix}
3 & 6 & 9 \\
12 & 15 & 18 \\
\end{pmatrix}
```
````
### Rechengesetze der Addition und skalaren Multiplikation 
Seien $A,B,C\in \mathbb{R}^{m\times n}$, sowie $\lambda,\mu\in \mathbb{R}$.

Dann gelten folgende Rechenregeln:

Matrixaddition:
1. Kommutativgesetz: $A + B = B + A$
2. Assoziativgesetz: $(A + B) + C = A + (B + C)$
3. Nullmatrix: $A + \textbf{0} = A$
4. Negation: $A + (-A) = \mathbf{0}$

Skalare Multiplikation:

5. Assoziativgesetz: $(\lambda \mu)A = \lambda(\mu A)$
6. Distributivgesetz (Skalar): $(\lambda + \mu)A = \lambda A + \mu A$
7. Distributivgesetz (Matrix): $\lambda (A + B) = \lambda A + \lambda B$
8. Einheitselement: $1\cdot A = A$
9. Skalare Multiplikation mit Null: $0\cdot A = \mathbf{0}$

## 4.4 Transposition von Matrizen
Das Transponieren von Matrizen bedeutet die Spalten und Zeilen zu vertauschen. Das heißt aus einer $m\times n$ Matrix wird eine $n\times m$ Matrix die wir mit $A^T$ bezeichnen.
Genauer definieren wir:
````{prf:definition}
Sei $A\in \mathbb{R}^{m\times n}$. Dann ist $C=A^T$ die $n\times m$ Matrix mit 
```{math}
c_{ij}=a_{ji} \quad \text{ für alle} 1 ≤ i ≤ n \text{ und } 1 ≤ j ≤ m.
```
````

````{prf:example}



Sei
```{math}
A = \begin{pmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
\end{pmatrix}
```

Die Transposition von $A$, erhalten wir, indem wir die Zeilen von $A$ zu den Spalten von $A^T$ und die Spalten von $A$ zu den Zeilen von $A^T$ werden:

```{math}
A^T = \begin{pmatrix}
1 & 4 \\
2 & 5 \\
3 & 6 \\
\end{pmatrix}
```
````
**Frage:**
Was ist die doppelte Transposition einer Matrix: $(A^T)^T$?


**Antwort:**
```{toggle}
$(A^T)^T=A$
```

## 4.5 Matrixmultiplikation
Wir haben bisher die Addition und die skalare Multiplikation von Matrizen kennengelernt. Dabei waren die Definitionen sehr natürlich. Das was wir mit Zahlen normalerweise machen übertragen wir auf Matrizen, in dem wir es komponentenweise durchführen.

Die Multiplikation von Zwei Matrizen funktioniert aber auf eine andere Art und weise.

Wir bauen die Multiplikation schrittweise auf.

### Vektor mal Vektor
Die einfachste Möglichkeit einer Matrixmultiplikation ist die Multiplikation eines Zeilenvektors mit einem Spaltenvektor.
Dies entspricht dem aus der Analytischen Geometrie bekannten **Skalarprodukt**.

Sei dazu $v=\begin{pmatrix} a_1 & a_2 & \dots & a_n \end{pmatrix}\in \mathbb{R}^{1\times n}$ und 
$w=\begin{pmatrix} b_1 \\ b_2 \\ \vdots \\ b_n \end{pmatrix}\in \mathbb{R}^{n\times 1}$.

Dann definieren wir

```{math}
v\cdot w=v=\begin{pmatrix} a_1 & a_2 & \dots & a_n \end{pmatrix}\cdot w=\begin{pmatrix} b_1 \\ b_2 \\ \vdots \\ b_n \end{pmatrix} =a_1\cdot b_1 + a_2\cdot b_2 + \dots + a_n\cdot b_n.
```

````{prf:example}
Sei

```{math}
v = \begin{pmatrix} 1 & 2 & 3 \end{pmatrix} \quad \text{und} \quad w = \begin{pmatrix} 4 \\ 5 \\ 6 \end{pmatrix}
```
Das Skalarprodukt wird berechnet, indem die entsprechenden Elemente der beiden Vektoren multipliziert und summiert werden:

```{math}
v \cdot w = \begin{pmatrix} 1 & 2 & 3 \end{pmatrix}\cdot \begin{pmatrix} 4 \\ 5 \\ 6 \end{pmatrix} = (1 \cdot 4) + (2 \cdot 5) + (3 \cdot 6) = 4 + 10 + 18 = 32
```
````

### Matrix mal Vektor

Die Situation "Matrix mal Vektor" hatten wir schon im Kapitel Lineare Gleichungen.

![](images/matrix_vector.png)

Wir sehen anhand der obigen Gleichung, dass die Situation Matrix mal Vektor sich so verhält dass ein neuer Vektor entsteht. Die einzelnen Komponenten sind nun die Skalarprodukte der Zeilen der Matrix mit dem Vektor, welcher multipliziert wird.

Formal ausgedrückt heißt das:


Sei $A\in \mathbb{R}^{m\times n}$ und $v\in \mathbb{R}^{n\times 1}$. 

Dann ist $w=A\cdot v \in \mathbb{R}^{m\times 1}$ und es gilt:
```{math}
w_i = a_{i*}\cdot v \quad \text{ für } i=1,\dots, m
```
wobei $a_{i*}\in \mathbb{R}^{1\times n}$ die $i$-te Zeile von $A$ ist.



Auch hierzu gucken wir uns ein kurzes Beispiel an 

````{prf:example}

Angenommen, wir haben die Matrix $A$ und den Vektor $v$ gegeben:

```{math}
A = \begin{pmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
\end{pmatrix} \quad \text{und} \quad v = \begin{pmatrix}
2 \\
3 \\
4 \\
\end{pmatrix}
```

Um die Multiplikation von $A$ und $v$ durchzuführen, multiplizieren wir jede Zeile von $A$ mit dem entsprechenden Element von $v$ und summieren die Produkte. Das Ergebnis ist ein neuer Vektor $w$:

```{math}
w=A \cdot B = \begin{pmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
\end{pmatrix} \begin{pmatrix}
2 \\
3 \\
4 \\
\end{pmatrix} = \begin{pmatrix}
(1 \cdot 2) + (2 \cdot 3) + (3 \cdot 4) \\
(4 \cdot 2) + (5 \cdot 3) + (6 \cdot 4) \\
\end{pmatrix} = \begin{pmatrix}
2 + 6 + 12 \\
8 + 15 + 24 \\
\end{pmatrix} = \begin{pmatrix}
20 \\
47 \\
\end{pmatrix}
```

Das Ergebnis der Multiplikation von $A$ und $v$ ist der Vektor $w = \begin{pmatrix} 20 \\ 47 \end{pmatrix}$. Beachte, dass die Anzahl der Spalten in $A$ der Anzahl der Zeilen in $v$ entsprechen muss, um die Multiplikation durchführen zu können.
````

### Matrix mal Matrix 

Als letztes betrachten wir nun das Produkt zweier Matrizen $A$ und $B$.

Die erste frage, die sich stellt ist: Welche Dimensionen dürfen $A$ und $B$ haben, damit wir sie miteinander multiplizieren können.

```{math}
(m\times n)\cdot (n\times k) = (m\times k) \quad \text{ (Dimensionsformel)}
```

Die obige Formel beschreibt, dies. Demnach muss die Anzahl der Spalten der ersten Matrix (die Anzahl der Zwischenprodukte) mit der Anzahl der Zeilen der zweiten Matrix (ebenfalls die Anzahl der Zwischenprodukte) übereinstimmt.

Aber wie berechnet man das Produkt von zwei Matrizen:


````{prf:definition}
Sei $A\in \mathbb{R}^{m\times n}$ und $B\in \mathbb{n\times k}$. Dann ist das Produkt $C=AB$ definiert durch

```{math}
c_{ij}=a_{i*}\cdot b_{*j}=a_{i1}b_{1j}+a_{i2}b_{2j}+\dots + a_{in}b_{nj} 
```
Dabei ist $a_{i*}\in \mathbb{R}^{1\times n}$ die $i$-te Zeile von $A$ und $b_{*j}\in\mathbb{R}^{n\times 1}$ die $j$-te Spalte von $B$.


````
Das heißt das Produkt $A\cdot B$ ist die Matrix $C$, dere $i,j$-te Komponente $c_{ij}$ das Skalarprodukt aus dem $i$-ten Zeilenvektor von $A$ und dem $j$-ten Spaltenvektor von $B$ ist.

Hier noch ein einfaches Beispiel
````{prf:example}

Angenommen, wir haben die Matrix $A$ der Dimension $2\times 3$ und die Matrix $B$ der Dimension $3\times 2$:

```{math}
A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix} \quad \text{und} \quad B = \begin{pmatrix} 7 & 8 \\ 9 & 10 \\ 11 & 12 \end{pmatrix}
```

Um das Produkt $AB$ zu berechnen, multiplizieren wir jede Zeile von $A$ mit jeder Spalte von $B$ und summieren die entsprechenden Produkte. Das Ergebnis ist eine neue Matrix $C$ der Dimension $2\times 2$:

```{math}
C = AB = \begin{pmatrix} (1 \cdot 7) + (2 \cdot 9) + (3 \cdot 11) & (1 \cdot 8) + (2 \cdot 10) + (3 \cdot 12) \\ (4 \cdot 7) + (5 \cdot 9) + (6 \cdot 11) & (4 \cdot 8) + (5 \cdot 10) + (6 \cdot 12) \end{pmatrix} = \begin{pmatrix} 58 & 64 \\ 139 & 154 \end{pmatrix}

```

````

Es gibt auch viele gute externe Quellen, die einem gut erklären wie man zwei Matrizen miteinander multiplizieren kann.

Z.B.

- <a href=https://youtu.be/uIykRXQhQtE> hier </a>
- <a href=https://studyflix.de/mathematik/matrizen-multiplizieren-1521> hier </a>


## 4.6 Gesetze der Matrixmultiplikation

Es seien $A,B,C$ Matrizen deren Produkt so definiert ist, dass untere Produkte existieren.
Sei weiter $\lambda\in \mathbb{R}$.
Dann gelten die folgenden Gesetze der Matrixmultiplikation:

- $(A \cdot B) \cdot C =  A \cdot (B \cdot C)  = A \cdot B \cdot C $
- $(\lambda A) \cdot B =  A \cdot (\lambda B)  = \lambda (A \cdot B)$
- $A \cdot E =  E \cdot A  = A$
- $A \cdot \textbf{0} =  \textbf{0} \cdot A  = \textbf{0}$
- $A \cdot(B + C) =  A \cdot B + A \cdot C$
- $(A+B) \cdot C = A \cdot C + B \cdot C$
- $(A \cdot B)^T =  B^T \cdot A^T$


**ACHTUNG**

Es gilt **nicht** 
```{math}
AB = BA.
```

D.h. es gibt **kein Kommutativgesetz** für Matrizen.
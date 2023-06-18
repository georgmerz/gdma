# Kapitel 6 - Lineare Transformationen in der Ebene



## 6.1 Lernziele

In diesem Abschnitt wollen wir lineare Transformationen in der Ebene mittels Matrizen genauer untersuchen.
:::{admonition}  Lernziele
:class: note

- Zusammenhang zwischen einer $2\times 2$ Matrix und einer geometrischen Transformationen
- Skalierungsmatrizen interpretieren und anwenden.
- Spiegelung als Matrixtransformation interpretieren und anwenden.
- Rotation als Matrixtransformation interpretieren und anwenden.
- Praxisbeispiel für die Bildbearbeitung in Python kennenlernen
::::::


## 6.2 Einführung

Wir konzentrieren uns in diesem Kapitel vor allem auf den $\mathbb{R}^2$. D.h. wir betrachten Transformationen in der Ebene. 

Wir zeigen zunächst wie wir Matrizen $A\in \mathbb{R}^{2\times 2}$ als geometrische Transformationen interpretieren können.

Dies geschieht durch folgende Interpretation von Matrizen als Abbildungen.

````{prf:definition}
Sei $A\in \mathbb{R}^{m\times n}$, so ist die **lineare Transformation** von $A$ definiert als die folgende Funktion
```{math}
T_A\colon \mathbb{R}^n \to \mathbb{R}^m \quad v\mapsto A\cdot v.
```
Wir nennen die Matrix zu der linearen Transformation $T_A$ die **Abbildungsmatrix**.

Falls $A\in \mathbb{R}^{2\times 2}$, so nennen wir die entsprechende lineare Transformation eine **lineare Transformation in der Ebene**.
````
````{prf:remark}
Obige Definition ist wohldefiniert. Dafür betrachten wir einmal kurz die Dimensionen.

Wenn $A\in \mathbb{R}^{m\times n}$ und $v\in \mathbb{R}^n=\mathbb{R}^{n\times 1}$ so gilt nach der Dimensionsformel ($(m\times n)\cdot (n\times 1)$), dass das Ergebnis die Dimension $(m\times 1)$ besitzt, also ein $m$-dimensionaler Spaltenvektor.

Für $A\in \mathbb{R}^{2\times 2}$ bedeutet dies, dass wir einen 2-dimensionalen Vektor auf einen 2-dimensionalen Vektor abbilden.

````
Lineare Transformationen (der Ebene) haben die folgende Eigenschaft, die charakteristisch für Linearität steht.

````{prf:theorem}
Sei $A\in\mathbb{R}^{2\times 2}$ eine Matrix und $T_A$ die zugehörige lineare Transformation.

- Der Nullvektor wird wieder auf den Nullvektor abgebildet.
- Geraden werden wieder auf Geraden abgebildet.
- Parallel Geraden bleiben Parallel.

````
````{prf:example}
Nach obigem Satz sehen wir, dass die Translation/Verschiebung eines Objektes **keine** lineare Transformation darstellt, da der Nullvektor nicht wieder auf den Nullvektor abgebildet wird.

Wir werden jedoch sehen, dass die folgenden Transformationen linear Transformationen darstellen:
- Spiegelung
- Skalierung
- Rotation

````

```{prf:example}

Sei $A=\left(\begin{array}{ll}1 & 2 \\ 2 & 1\end{array}\right)$. 

Um die Lineare Transformation genauer zu verstehen ist es häufig hilfreich sich zu Visualisieren wie die Vektoren $e_1=\left(\begin{array}{c} 1 \\ 0 \end{array}\right)$ und $e_2=\left(\begin{array}{c} 0 \\ 1\end{array}\right)$ transformiert werden. Wie man leicht nachrechnet werden diese auf die Vekotoren $Ae_1=\left(\begin{array}{c}1\\2\end{array}\right)$ und $Ae_2=\left(\begin{array}{c}2\\1\end{array}\right)$, transformiert.
![](images/transform/ex1_basis.png)

Wir können nun auch betrachten was passiert wenn wir die Punkte eines Dreiecks transformieren:
![](images/transform/ex1_triangle.png).

Wir sehen, dass das Dreieck wieder ein Dreieck ist, aber die Längen und Winkel sich unterscheiden. 
Wir sehen, aber auch das beide Dreiecke den Nullpunkt beinhalten.
```


## 6.3 Skalierung als lineare Transformation.



Skalierung bedeutet Strecken und Stauchen von geometrischen Objekten.

Mittels der skalaren Multiplikation mit einem positiven $lambda>0$ können wir via $ v\mapsto \lambda \cdot v$ eine einfache mathematische Beschreibung von Streckung und Stauchung. Sie ist eine Streckung falls $\lambda >1$ und eine Stauchung falls $\lambda <1$

In Matrixform können wir dies auch so schreiben:
```{math}
S(\lambda,\lambda)=\left(\begin{array}{ll}\lambda & 0 \\ 0 & \lambda\end{array}\right).
```


Wollen wir in $x$ und $y$ Richtung mit verschiedenen Streckungsfaktoren arbeiten so können wir allgemein eine Streckungsmatrix via
```{math}
S(\lambda,\mu)=\left(\begin{array}{ll}
\lambda & 0 \\
0 & \mu
\end{array}\right) \text { für } \lambda, \mu>0
```
Machen wir wieder ein Beispiel:

````{prf:example}
Wir betrachten nun die Matrix
```{math}
S(2,3)=
\left(\begin{array}{ll}
2 & 0 \\
0 & 3
\end{array}\right)
```
Wieder betrachten wir zunächst die transformierten Basisvektoren
![](images/transform/ex2_basis.png)

Und nun ein transformiertes Dreieck
![](images/transform/ex2_triangle.png)

Wir sehen, dass die Grundlinie des Dreiecks sich verdoppelt, und die Höhe des Dreiecks sich verdreifacht.

````

## 6.4 Spiegelung als lineare Transformation

Spiegelung lassen sich auch als lineare Transformationen abbilden. Dabei gibt es drei Möglichkeiten in der Ebene zu spiegeln:

- Punktspiegelung
- Spiegelung an der $y$-Achse
- Spiegelung an der $x$-Achse

Ähnlich wie Dehnung/Streckung lassen sich die Matrizen mit Diagonalmatrizen darstellen. Nur dieses mal erlauben wir auch explizit negative Zahlen.

Hier ist der Überblick über die Spiegelung:

|                 | Matrix                                    | geom. Bedeutung                 |
|-----------------|-------------------------------------------|---------------------------------|
| S(-1, 1)        | $\begin{pmatrix}-1 & 0 \\ 0 & 1\end{pmatrix}$               | Spiegelung an der y-Achse       |
| S(1, -1)        | $\begin{pmatrix}1 & 0 \\ 0 & -1\end{pmatrix}$               | Spiegelung an der x-Achse       |
| S(-1, -1)       | $\begin{pmatrix}-1 & 0 \\ 0 & -1\end{pmatrix}$             | Punktspiegelung am Ursprung     |


````{prf:example}
Wir betrachten nun die Matrix
```{math}
S(-1,1)=
\left(\begin{array}{ll}
-1 & 0 \\
0 & 1
\end{array}\right)
```
Also die Spiegelung an der $y$-Achse
Wieder betrachten wir zunächst die transformierten Basisvektoren
![](images/transform/ex3_basis.png)

Und nun ein transformiertes Dreieck
![](images/transform/ex3_triangle.png)

Wir sehen, dass das transformierte Dreieck identisch mit dem ursprünglichen Dreieck ist, da es Achsensymmetrisch zur $y$-Achse ist.

Wir können zum Beispiel den unteren Punkt nehmen und dies nachvollziehen:
```{math}
\left(\begin{array}{rr}
-1 & 0 \\
0 & 1
\end{array}\right)\left(\begin{array}{c}
0 \\
-1
\end{array}\right)=\left(\begin{array}{c}
0 \\
-1
\end{array}\right)

```
D.h. der Punkt bleibt wo er ist.

Es kann nun leicht nachgerechnet werden, dass die beiden anderen Punkte miteinander tauschen.
````

## 6.5 Rotation als lineare Transformation


Die Rotation ist die Komplizierteste Variante der linearen Transformation.
Dabei stellt sich zunächst die Frage in Welche Richtung und welchen Winkel. Dabei ist wichtig, dass Mathematisch positive Richtung immer gegen den Uhrzeigersinn darstellt. Wenn wir also von einer Drehung um 90° sprechen, dann meinen wir eine Drehung um 90° gegen den Uhrzeigersinn.

Wir betrachten zunächst ein Beispiel.

````{prf:example}

Wir wollen die 90°-Drehung als Matrix darstellen. Dafür müssen wir überlegen auf welche Vektoren wir die beiden Basisvektoren $e_1=\left(\begin{array}{c} 1 \\ 0 \end{array}\right)$ und $e_2=\left(\begin{array}{c} 0 \\ 1 \end{array}\right)$ abgebildet werden. $e_1$ muss auf den Vektor $\left(\begin{array}{c} 0 \\ 1 \end{array}\right)$ abgebildet werden und $e_2$ auf $\left(\begin{array}{c} 0 \\ -1 \end{array}\right)$.

Damit ergibt sich folgende Matrix:
```{math}
A=\left(\begin{array}{rr}
0 & -1 \\
1 & 0
\end{array}\right)
```
Und es ergeben sich folgende Bilder:

![](images/transform/ex3_basis.png)

Und nun ein transformiertes Dreieck
![](images/transform/ex3_triangle.png).

````


Wir haben nun die Rotation für 90° gesehen. Doch was ist die Allgemeine Formel.

Diese fassen wir im folgenden Satz zusammen.

````{prf:theorem}
Der Ausdruck $R(\varphi)$ bezeichnet eine Rotation um den Winkel $\varphi$ mit dem Ursprung als Rotationszentrum. Sie lässt sich durch folgende Matrix darstellen.
```{math}
R(\varphi)=\left(\begin{array}{cc}
\cos \varphi & -\sin \varphi \\
\sin \varphi & \cos \varphi
\end{array}\right)
```

````

Hier ist eine Tabelle mit den Wichtigsten Rotationsmatrizen:
| Winkel ($\theta$) | Rotationsmatrix ($R(\theta)$)                                              | geom. Bedeutung                        |
|------------------|----------------------------------------------------------------------------|----------------------------------------|
| $0^\circ$        | $\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$                              | Keine Rotation (Identitätsmatrix)       |
| $90^\circ$       | $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$                              | Rotation um $90^\circ$  |
| $180^\circ$      | $\begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}$                             | Rotation um $180^\circ$                |
| $270^\circ$      | $\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$                              | Rotation um $270^\circ$ |


## 6.6 Hinterinanderschaultung von Linearen Transformationen

Angenommen wir wollen eine Kombination aus den obigen linearen Transformationen machen. Dann stellt sich die Frage, wie wir die zugehörige Matrix bekommen. Wollen wir zum Beispiel erst Rotieren und dann Skalieren.

Der folgende Satz liefert dafür die entsprechende Antwort.

````{prf:theorem}

Seien $A,B\in \mathbb{R}^{2\times2}$. Seien $T_A$ und $T_B$ die entsprechenden linearen Transformationen.
Sei weiter $A\cdot B$ das Produkt der beiden Matrizen und $T_{A\cdot B}$ die entsprechende lineare Transformation.
Dann gilt:
```{math}
T_A\circ T_B = T_{AB}
```
Anders ausgedrückt: die Hinterinanderausführung von zwei linearen Transformationen entspricht auf der Ebene der Matrizen der Matrixmultiplikation.
````

Auch hierfür wollen wir ein Beispiel betrachten:
````{prf:example}
Wir wollen in diesem Beispiel zunächst um 90° Drehen und dann an der $y$-Achse spiegeln.
Die entsprechende Matrix ist dann laut obigem Satz:
```{math}
S(-1,1)\cdot R(90°) = \left(\begin{array}{cc}
-1 & 0 \\
0 & 1
\end{array}\right)\left(\begin{array}{rr}
0 & -1 \\
1 & 0
\end{array}\right)
= \left(\begin{array}{rr}
0 & 1 \\
1 & 0
\end{array}\right)

```

Beachte auch hier dass wir von rechts nach links lesen. rechts steht die Rotation, weil wir diese als erste ausführen.

Schauen wir uns nun die entsprechenden Bilder an

Zunächst die Transformation auf den Basisvektoren:
![](images/transform/ex5_basis.png)

Und nun auf unser Standard Dreieck:
![](images/transform/ex5_triangle.png)
Auf dem ersten Blick sieht das nun so aus wie eine Drehung um 90° in mathematisch negativer Richtung oder im Uhrzeigersinn. Dies liegt aber an der Symmetrie des Dreiecks. 
Betrachten wir ein weiteres Dreieck:
![](images/transform/ex5_triangle2.png)
Hier sehen wir, dass es keine Rotation ist. 

Sehen Sie wie man die Transformation geometrisch zusammenfassen kann?
**Antwort:**
```{toggle}
Es ist die Spiegelung um die Winkelhalbierende des ersten Quadranten, oder der Gerade $y=x$.
```


````





# Kapitel 1 - Mengenlehre

## 1.1 Lernziele
In diesem Kurs lernen wir die folgenden Dinge:

- Schreibweise/Syntax in der Mengenlehre
- Beschreibung von Mengen
- Mengenoperationen (Schnitt, Vereinigung, kartesisches Produkt)
- Mächtigkeit/Kardinalität einer Menge


:::{admonition}  Lernziele
:class:note

- Sie haben ein Verständnis für den Begriff der Menge und können diesen intuitiv verstehen.
- Sie können sicher mit den Grundoperatoren der Mengenlehre umgehen und können aus bekannten Mengen mittels Mathematischer Sprache neue Mengen konstruieren.
- Sie können den Aufbau der Natürlichen Zahlen als Mengen nachvollziehen
- Sie haben ein Verständnis für die Paradoxien der naiven Mengenlehre und können dies mit den Zermelo Fraenkl Axiomen in Verbindung bringen
:::


## 1.1 Definition einer Menge

Zu erklären was eine Menge denn wirklich ist, ist garnicht so einfach, aber das gilt vor allem wenn man es exakt mathematisch definieren will. Intuitiv ist es gar nicht so  schwer.
So gibt es beispielsweise folgende Definition von *Georg Cantor* aus dem Jahre 


````{prf:definition}
:label: my-definition2
"Eine Menge ist eine Zusammenfassung bestimmter wohlunterschiede- ner Objekte unserer Anschauung oder unseres Denkens - welche die Elemente der Menge genannt werden - zu einem Ganzen."            

````

Das klingt in der Tat nicht sehr Mathematisch Exakt, aber soll uns zu Beginn erstmal reichen.

Wichtige Folgerungen aus der obigen Definition sind:

- Die Objekte einer Menge heißen **Elemente**
- Die **Elemente** müssen alle verschieden sein
- In der Definition von Cantor spielt die Reihenfolge **keine** Rolle 

````{prf:example}
:label: Mengen
Folgendes sind Beispiele für Mengen:
- \( A:=\{0,1,2,3,4\} \)
- $B:=\{a,b,c,d,e,f,g\} $
- $C:=\{ 👍, 👮🏿 , 🇧🇱 , 🔨\}  $
````

**Beobachtungen**:

- Wie Sie sehen können Elemente einer Menge ganz unterschiedlicher Natur sein. Sie können Zahlen, Buchstaben, oder auch Zeichen sein. Wichtig ist nur, das sie unterscheidbar sind und eindeutig.

- Um eine Menge aus endlich vielen Elementen hinzuschreibne nutzen wir geschweifte Klammern ($ \{ \} $).


**Frage:**

Kann ein Element einer Menge auch selbst eine Menge sein?

**Antwort:**
```{toggle}
**Ja!** Denn Mengen sind eindeutig und unterscheidbar. Damit können Sie auch selbst Mengen sein. Wir werden am Ende dieses Kapitels sogar sehen, dass wir die komplette Mathematik auf der Grundlagen von Mengen aufbauen können.

```
````{prf:example}
:label: Mengen von Mengen
Folgendes sind Beispiele für Mengen von Mengen:
- $D:=\{ \{0,1\} ,\{2,3,4\}\} $
- $E:=\{\{ 0,1,2,3,4 \} \} $
````
## 1.2 Notation



Eine ungewöhnliche Menge  ist die folgende:

````{prf:definition}
:label: my-definition
Diejenige Menge, die **kein** Element enthält wird die *leere Menge** genant und mit
\begin{align*}
 \{ \} \text{ oder } \varnothing 
\end{align*}
bezeichnet.
````

Als nächstes führen wir das Symbol $\in $ und $\notin$ ein.


```{prf:definition}
:label: element
Wir schreiben $x\in M$. Falls  $x$ ein Element von $M$ ist.
Wir schreiben $x\in M$ falls $x$ kein Element von $M$ ist.

````


````{prf:example}
:label: elementbsp
Betrachten wir unsere Beispielmengen
- :math: A:=\{0,1,2,3,4\} 
- $B:=\{a,b,c,d,e,f,g\} $
- $C:=\{ 👍, 👮🏿 , 🇧🇱 , 🔨\}  $
- $D:=\{ \{0,1\} ,\{2,3,4\}\} $
- $E:=\{\{ 0,1,2,3,4 \} \} $

Dann gilt z.B.:

- $0 \in A$
- $5 \notin A$.
- $a\in B$
- \{ 0,1,2,3,4 \} \in E
- \{0,1\}

````
$\sum_{k=0}$



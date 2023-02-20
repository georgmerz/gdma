#!/usr/bin/env python
# coding: utf-8

# # Matrixmultiplikation
# 
# In diesem Google Colab Notebook werden wir uns vor allen Dingen mit der Matrixmultiplikation beschäftigen. Wir werden die Matrixmultiplikation von Hand mittels Schleifen nachimplementieren.
# 

# ## 1. Vektoren und Matrizen in Numpy
# 
# 
# 
# 

# - Numpy ist das wichtigste Werkzeug in Python wenn es um Matrizen und Vektoren geht.
# 
# - Numpy ist nicht das schnellste Paket um in Python mit Vektoren zu rechnen es ist aber das Intuitivste
# 
# - **Ziel** in diesem Kurs ist es alle Algorithmen und Berechnungen nur mit den einfachsten Numpy Werkzeugen durchzuführen
# 

# ### 1. Schritt (numpy importieren)
# 
# Zunächst müssen wir numpy importieren und es mit einem kürzel versehen. In der regel verwendet man dafür np.

# In[1]:


import numpy as np


# ### 2. Schritt(Vektoren und Matrizen definieren)
# 
# Sagen wir zum Beispiel wir wollen folgende Vektoren und Matrizen in Numpy definieren: 
# 
# $\vec{w}=\begin{pmatrix} 1 & 2 & 3 \end{pmatrix}\in \mathbb{R}^{1\times3 },\quad \vec{v}=\begin{pmatrix} 2 \\ 0 \\ 1 \end{pmatrix}\in \mathbb{R}^{3\times 1} \quad 
# A=\begin{pmatrix} 1&1&0 \\ 0&1&1 \\ 1&0&1 \end{pmatrix}\in \mathbb{R}^{3\times 3}$
# 

# In[2]:


w=np.array([1,2,3])
w


# In[3]:


v=np.array([[2],[0],[1]])
v


# In[4]:


A=np.array([[1,1,0],[0,1,1],[1,0,1]])
A


# Falls wir nicht mehr sicher sind welche Dimension unsere Matrix bzw. unser Vektor hat. Können wir dies mittels `np.shape(A)` abfragen:

# In[5]:


np.shape(A)


# ### 3. Schritt

# In[6]:


### 3. Schritt


# Wollen wir nun beispielsweise $a_{12}$ von $A$ bestimmen. Also den zweiten Eintrag der ersten Zeile so können wir dies mittels Eckigen klammern machen.
# 
# **Achtung**: Python beginnt bei **0** zu zählen. In der Mathematik wird für indizes häufig mit 1 gestartet. D.h. $a_{12}$ entsprich dann `A[0,1]`

# In[7]:


A[0,1]


# In[8]:


w[0]


# Bei Spaltenvektoren müssen wir um eine Zahl zu bekommen noch den zweiten Index mitnehmen. D.h. wenn wir  𝑣3
# v
# 3
#   bekommen wollen müssen wir folgendes schreiben:

# In[9]:


v[2,0]


# # 2 Grundrechenarten in Numpy

# ### Addition
# 
# Matrizen und Vektoren können sehr einfach addiert und subtrahiert werden. Dafür können wir einfach die gewöhnliche `+`und `-` verwenden.

# In[10]:


A+A


# In[11]:


v+v


# **Achtung**
# 
# Wenn Sie zwei Vektoren/Matrizen mit unterschiedlichen Dimensionen addieren kommt keine Fehlermeldung.

# In[12]:


A+v


# In[13]:


v+w


# Konnten Sie eine Logik festellen? Gar nicht so einfach oder?

# ### Multiplikation von Matrizen
# 
# In diesem Abschnitt wollen wir die Matrixmultiplikation so wie wir sie im Kurs gelernt haben implementieren auf der Ebene der Matrix Elemente.
# 
# 

# #### Matrix mal Vektor
# 
# Sei $A=\begin{pmatrix} a_{11}&\dots &a_{1k} \\ \vdots &\ddots&\vdots \\ a_{n1}&\dots & a_{nk} \end{pmatrix}\in \mathbb{R}^{n\times k}$ sowie $v=\begin{pmatrix}v_1 \\ \vdots \\ v_k \end{pmatrix}$.
# Sei weiterhin $w=\begin{pmatrix}w_1 \\ \vdots \\ w_n \end{pmatrix}\in \mathbb{R}^n$
# 
# Dann gilt folgende Formel für die Elemente von $C$.
# 
# $w_i=\sum_{j=1,\dots n}a_{ij}v_j$.

# Schauen wir nun wie wir das in Numpy umsetzen können.
# 
# 1. Versuch Wir multiplizieren mit `*`

# In[14]:


A*v


# In[15]:


v.shape


# Ist das Richtig also gilt:
# 
# 
# 
# $\begin{pmatrix} 1&1&0 \\ 0&1&1 \\ 1&0&1 \end{pmatrix}\begin{pmatrix} 2 \\ 0 \\ 1 \end{pmatrix}=\begin{pmatrix} 2&2&0 \\ 0&0&0 \\ 1&0&1\end{pmatrix} $

# **Antwort:** NEIN. Stimmt schon von den dimensionen natürlich nicht!
# 
# 

# Ok. Dann berechnen wir das eben Selbst mithilfe einer einfachen Schleife.

# In[16]:


def matrix_times_Vector(A,v):
  n,k=A.shape
  
  w=np.zeros((n,1))   # initialisiere das Ergebnis mit einem 0 Vektor der Dimension n,1 
  for i in range(k):      
    for j in range(n):
      w[i]+= A[i,j]*v[j,0]
  return w


# In[17]:


matrix_times_Vector(A,matrix_times_Vector(A,v))


# **Aufgaben**
# 
# 
# *   Bestimmen Sie mit Hilfe der Obigen Funktion den Vektor $a=A\cdot A \cdot v$
# *   Bestimmen Sie mit Hilfe der obigen Funktion den Vektor $b=A\cdot w^T$. *Hinweis: Sie können für $w^T$ die Funktion `np.atleast_2d(w).T` benutzen* 
# 
# 

# In[18]:


a = # Insert Text here

b = # Insert Text here


# #### Matrix mal Matrix

# Sei $A=\begin{pmatrix} a_{11}&\dots &a_{1k} \\ \vdots &\ddots&\vdots \\ a_{n1}&\dots & a_{nk} \end{pmatrix}\in \mathbb{R}^{n\times k}$ sowie $B=\begin{pmatrix} b_{11}&\dots &b_{1m} \\ \vdots &\ddots&\vdots \\ b_{k1}&\dots & b_{km} \end{pmatrix}\in \mathbb{R}^{k\times m}$.
# Sei weiterhin $C=\begin{pmatrix} c_{11}&\dots &c_{1m} \\ \vdots &\ddots&\vdots \\ c_{n1}&\dots & c_{nm} \end{pmatrix}\in \mathbb{R}^{n\times m}$.
# 
# Dann gilt folgende Formel für die Elemente von $C$.
# 
# $c_{ij}=\sum_{s=1,\dots k}a_{is}b_{sj}$.

# Auch hier gucken wir uns wieder an wenn wir nun z.B. $A^2$ bestimmen mit `A*A

# In[61]:


A*A


# Stimmt das? Ist $\begin{pmatrix} 1&1&0 \\ 0&1&1 \\ 1&0&1 \end{pmatrix}  \begin{pmatrix} 1&1&0 \\ 0&1&1 \\ 1&0&1 \end{pmatrix}=\begin{pmatrix} 1&1&0 \\ 0&1&1 \\ 1&0&1 \end{pmatrix}$?

# **Antwort:** Nein!

# In[77]:


def matrix_times_matrix(A,B):
  n,k=A.shape
  k,m=B.shape
  C=np.zeros((n,m))

  for i in range(n):
    for j in range(m):
      for s in range(k):
        C[i,j]+=A[i,s]*B[s,j]


  return C



# In[81]:


matrix_times_matrix(np.atleast_2d(v).T,A)


# **Aufgaben**
# 
#  - Bestimmen Sie nochmals $A\cdot A \cdot v$ mithilfe der neuen Funktion `matrix_times_matrix(A,B)`
#  - Bestimmen Sie nochmals $v^T\cdot A$ mithilfe der neuen Funktion.

# 

# In[76]:





# [Linktext](https://)

# 

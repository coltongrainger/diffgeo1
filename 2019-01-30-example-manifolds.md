---
title: Examples of Smooth Manifolds
author: Colton Grainger (MATH 6230 Differential Geometry)
date: 2019-01-24
revised: 2019-01-29
nonumbering: true
bibliography: /home/colton/coltongrainger.bib
---

## Assignment due 2019-01-30

### [@Lee03, number 1.18]

\gvn Let $M$ be a topological manifold. 

\wts Two smooth atlases for $M$ determine the same smooth structure if and only if their union is a smooth atlas.

\pf ($\Rightarrow$) Let $\sA$, $\sB$ be two smooth atlases on a topological manifold. Say that $\sA \cup \sB$ is a smooth atlas. Then the unique maximal smooth atlas $\overline{\sA \cup \sB}$, which certainly contains $\sA$ and $\sB$, forces the conclusion: $$\overline{\sA} = \overline{\sA \cup \sB} = \overline{\sB},$$ that is, both $\sA$ and $\sB$ determine the same smooth structure on $M$.

($\Leftarrow$) Say that $\sA$ and $\sB$ are smooth atlases that determine the same smooth structure on $M$. For contradiction, suppose that $\sA$ and $\sB$ are not compatible, so that their union contains at least $(U, \phi) \in \sA$ and $(V, \psi) \in \sB$ for which $U \cap V \neq \emptyset$ and $$\phi(U \cap V) \xrightarrow{\phi^{-1}} U \cap V \xrightarrow{\psi} \psi(U \cap V)$$ is *not* a diffeomorphism. Now 
\begin{align*}
(U, \phi) &\in \sA \subset \overline{\sA}, \text{ and }\\
(V, \psi) &\in \sB \subset \overline{\sB},
\end{align*}
so either 

- $\overline{\sA} = \overline{\sB}$ is not smooth, or 
- $\overline{\sA} \neq \overline{\sB}$ are not the same smooth structures.

Both conclusions are contrary to our hypotheses, so it had better be that $\sA$ and $\sB$ are compatible! \qedsymbol


### [@Lee03, number 1-6]

\gvn Let $M$ be a nonempty topological manifold of dimension $n \ge 1$. 

\wts If $M$ has a smooth structure, then it has uncountably many distinct ones.

\pf We construct uncountably many distinct smooth structures on $M$.

step of construction | justification
--- | ---
1. Say $\sA$ is a maximal smooth atlas on $M$. | Hypothesis.
2. Of the charts in $\sA$, take a countable basis of regular coordinate balls and form the smooth atlas $\{(B_i, \phi_i)\}$. | Every smooth manifold has a countable basis of regular coordinate balls. [@Lee03, p. 15]
3. Form an open, locally finite, refinement $\{V_j\}$ of the cover $\{B_i\}$. | $\{B_i\}$ is an open cover of paracompact $M$.
4. For each $V_j$, choose $(B_i, \phi_i)$ such that $V_j \subset B_i$ and define $\psi_j := \phi_i\lvert_{V_j}$. | 
5. Note that $\{(V_j, \psi_j)\}$ is a smooth atlas. | $\{V_j\}$ covers $M$. For each pair $\psi_k$, $\psi_\ell$, in the atlas, the transition map $\phi_k \circ \psi^{-1}_\ell$ is (the restriction of) a diffeomorphism.
6. Consider a point in $M$, a neighborhood of this point, and take all $V_1, \ldots, V_n$ of $\{V_j\}$ which meet this neighborhood. | $\{V_j\}$ is locally finite, $M$ is non-empty.
7. Remove an open set $V_k$ from $V_1, \ldots, V_n$ if $V_k$ is not covered by $\{V_1, \ldots, \hat{V_k}, \ldots, V_n\}$. | Choice.
8. Repeat step 7 until there's a open $V$ from the initial $n$ that's not covered by those open sets of the initial $n$ remaining. | Finite recursion.
9. Choose a point $p \in V$ such that $p$ is not in any other open set of those remaining after step 8. | 
10. Note the atlas $\{(V_j, \psi_i)\}$ from step 5, with $\{(V_1, \psi_1), \ldots, (V_n, \psi_n)\}$ removed, with $\{\text{charts remaining after step 8}\}$ adjoined, is smooth. |
11. Moreover, the smooth atlas in step 10 has a particular chart $(V, \psi)$ such that $p \in V$ alone. | $p \in V$, yet $p \notin V_1, \ldots, \hat{V}, \ldots, V_n$.
12. Consider the image of $V$ and $p$ in $\RR^n$ under the map $\phi \colon B \to \hat{B} \subset \RR^n$, where $B$ is the regular coordinate ball chosen in step 4 to contain $V$. | 
13. Diffeomorph $\hat{B}$ to itself so that $\phi(p) \in \hat{V}$ is mapped to the origin. Denote this diffeomorphism by $g$. | WLOG, say $\hat{B}$ is a unit ball centered at the origin. Then $g$ is a tangent map $\hat{B} \to \RR^n$, followed by a rigid translation in $\RR^n$, finished with an inverse tangent map $\RR^n \to \hat{B}$.
14. For all reals $s > 0$ such that $s \neq 1$, there's a function $F_s$ that homeomorphs $\hat{B}$ to itself. | $F_s \colon x \mapsto \abs{x}^{s-1} x$.
15. The restriction of $F_s \circ g$ to the punctured unit ball $\hat{B} \setminus \{0\}$, *is indeed* a diffeomorphism of $\hat{B} \setminus \{0\}$. | Partial derivatives of all orders exist for both $F_s$ and its inverse $F_{1/s}$.
16. When $s \neq 1$, $F_s \circ g$ is either *not smooth* at the origin or *fails to have a smooth inverse*. | Either $F_s$ or $F_s^{-1}$ fails to be of class $C^\infty$ on $\hat{B}$. There's no good linear approximation of the norm of a vector at the origin.
16. Define $\psi_s$ as the restriction of the composite $F_s \circ g \circ \phi$ to $V$. | 

I claim $(V, \psi_s)$ is *compatible* with any other chart $(V', \psi')$ from the atlas constructed in step 10. Why? Because $V \cap V'$ does not contain $p$, whence the transition map $\psi' \circ\psi_s^{-1}$ where $$\psi_s(V \cap V') \xleftarrow{\psi_s} V \cap V' \xrightarrow{\psi'} \psi'(V \cap V')$$ is a diffeomorphism. Yet, for distinct parameters $s, t \in \RR^+ \setminus\{1\}$, the charts $(V, \psi_s)$ and $(V, \psi_t)$ are *not compatible* with each other. Why? Because $p \in V$. The transition map $\psi_t \circ\psi_s^{-1}$, $$\hat{V} \xleftarrow{\psi_s} V \xrightarrow{\psi_t} \hat{V}$$ is not differentiable at $\psi_s(p)$. We conclude there's a unique smooth structure on the topological manifold $M$ for each value of the parameter $s \in \RR^+ \setminus\{1\}$. \qedsymbol

### [@Lee03, number 1-7]

\gvn Let $N$ denote the *north pole* $(0,\ldots, 0, 1) \in S^n \subset \RR^{n+1}$, and let $S$ denote the *south pole*. Define the *stereographic projection* $\sigma \colon S^n \setminus \{N\} \to \RR^n$ $$\sigma\left(x^1, \ldots, x^{n+1}\right) = \frac{(x^1, \ldots, x^n)}{1 - x^{n+1}}.$$ Let $\tilde{\sigma}(x) = -\sigma(-x)$ for $x \in S^n \setminus \{S\}$.

\wts

a. For $x \in S^n \setminus \{N\}$, $\sigma(x) = u$, where $(u, 0)$ is the point where the line through $N$ and $x$ intersects the linear subspace where $x^{n+1} = 0$. (There's a similar intersection for $\tilde{\sigma}$. Find it.)

b. $\sigma$ is bijective, and its inverse is $$\sigma^{-1}(u^1, \ldots, u^n) = \frac{(2u^1, \ldots, 2u^n, \abs{u}^2 - 1)}{\abs{u}^2 + 1}.$$

c. We compute the transition map $\tilde{\sigma} \circ \sigma^{-1}$ and verify that the atlas consisting of the two charts $(S^n \setminus \{N\}, \sigma)$ and $( S\setminus \{S\}, \tilde{\sigma})$ defines a smooth structure on $S^n$.

d. This smooth structure is the same as the one defined in Example 1.31 (spheres).

### [@Lee03, number 1-8]

\gvn By identifying $\RR^2$ with $\CC$, we can think of the unit circle $S^1$ as a subset of the complex plane. An *angle function* on a subset $U \subset S^1$ is a continuous map $\theta \colon U \to \RR$ such that $e^{i\theta(z)} = z$ for all $z \in U$. 

\wts 

- There exists an angle function $\theta$ on an open subset $U \subset S^1$ if and only if $U \neq S^1$. 
- For any such angle function, $(U, \theta)$ is a smooth coordinate chart for $S^1$ with its standard smooth structure.

## References

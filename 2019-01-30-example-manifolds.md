---
title: Examples of Smooth Manifolds
author: Colton Grainger (MATH 6230 Differential Geometry)
date: 2019-01-24
revised:
nonumbering: true
bibliography: /home/colton/coltongrainger.bib
---

## Assignment due 2019-01-30

### [@Lee03, number 1.18]

\gvn Let $M$ be a topological manifold. 

\wts Two smooth atlases for $M$ determine the same smooth structure if and only if their union is a smooth atlas.

### [@Lee03, number 1-6]

\gvn Let $M$ be a nonempty topological manifold of dimension $n \ge 1$. 

\wts If $M$ has a smooth structure, then it has uncountably many distinct ones. (Hint: for any $s > 0$, $F_s(x) = \abs{x}^{s-1}x$ defines a homeomorphism from $B^n$ to itself, which is a diffeomorphism if and only if $s =1$.)

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

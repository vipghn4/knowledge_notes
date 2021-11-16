* *Intuition of curl*.
    * *Solving for curl*. Since $\nabla\times \mathbf{F}\in\mathbb{R}^3$, we have that
        
        $$(\nabla\times \mathbf{F}) = \mathbf{I}_3\cdot (\nabla\times \mathbf{F}) = \begin{bmatrix}
        \lim_{A_x\to 0} \frac{1}{|A_x|} \oint_C \mathbf{F}\cdot d\mathbf{r}_x\\
        \lim_{A_y\to 0} \frac{1}{|A_y|} \oint_C \mathbf{F}\cdot d\mathbf{r}_y\\
        \lim_{A_z\to 0} \frac{1}{|A_z|} \oint_C \mathbf{F}\cdot d\mathbf{r}_z\end{bmatrix}$$
    
    * *Extreme cases*. Assume that the magnitudes of the vectors within the vector field $\mathbf{F}$ are fixed, and their orientations are allowed to change, then
        * *Maximum curl*. $\mathbf{F}$ reaches maximum curl when 
            
            $$\forall p\in\mathbb{R}^3,\cos[\mathbf{F}(p), d\mathbf{r}(p)]=1$$
            
            i.e. if $A$ has circular shape, then $\mathbf{F}$ will be circular as illustrated below

            <div style="text-align:center">
                <img src="https://i.imgur.com/kNZguH9.png" width="350">
                <figcaption>Vector field with maximum curl</figcaption>
            </div>

        * *Minimum curl*. $\mathbf{F}$ reaches maximum curl when $\oint_C \mathbf{F}(p) \cdot d\mathbf{r}(p)=0$, i.e.

            $$\forall p\in\mathbb{R}^3,\mathbf{F}(p)=\mathbf{c}$$

            for some constant vector $\mathbf{c}$

            <div style="text-align:center">
                <img src="https://i.imgur.com/lj2swUp.png" width="350">
                <figcaption>Vector field with minimum curl</figcaption>
            </div>
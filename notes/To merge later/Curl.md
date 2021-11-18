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
* *Formulation of curl under Cartesian coordinates*.

    $$\begin{aligned}
    (\nabla\times \mathbf{F})_x&=\frac{\partial F_z}{\partial y} - \frac{\partial F_y}{\partial z}\\
    (\nabla\times \mathbf{F})_y&=\frac{\partial F_x}{\partial z} - \frac{\partial F_z}{\partial x}\\
    (\nabla\times \mathbf{F})_z&=\frac{\partial F_y}{\partial x} - \frac{\partial F_x}{\partial y}\big)
    \end{aligned}$$

    * *Properties*. 
        * $\nabla \times \mathbf{F}$ is invariant under proper rotations of the coordinate axes
        * $\nabla \times \mathbf{F}$ inverts under reflection
* *Generalization to orthogonal coordinates*. Let $(u_1,u_2,u_3)$ be an orthogonal coordinates

    $$\begin{aligned}
    (\nabla\times \mathbf{F})_1&=\frac{1}{h_2 h_3} \big(\frac{\partial (h_3 F_3)}{\partial u_2} - \frac{\partial (h_2 F_2)}{\partial u_3}\big)\\
    (\nabla\times \mathbf{F})_2&=\frac{1}{h_3 h_1} \big(\frac{\partial (h_1 F_1)}{\partial u_3} - \frac{\partial (h_3 F_3)}{\partial u_1}\big)\\
    (\nabla\times \mathbf{F})_3&=\frac{1}{h_1 h_2} \big(\frac{\partial (h_2 F_2)}{\partial u_1} - \frac{\partial (h_1 F_1)}{\partial u_2}\big)
    \end{aligned}$$
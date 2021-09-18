# Gradient and Jacobian matrices intuition
**Gradients is the direction of highest local increment**:
* Assumptions:
    * $f: \textbf{R}^n \to \textbf{R}$
    * $\nabla f(x) = \begin{bmatrix} \frac{\partial f}{\partial x_1} \\ \vdots \\ \frac{\partial f}{\partial x_n} \end{bmatrix}$ is the gradient of $f$ at $x$
* Observations:
    * By using $\nabla f(x)$ to analyze the behavior of $f$ near $x$, 
    
    $\hspace{1.0cm} \rightarrow$ We are approximating $f$ by $f(y) = f(x) + \nabla f(x)^T (y - x)$
    * Consider the hyperplane $(P): f(y) = f(x) + \nabla f(x)^T (y - x)$, 
        * Imagine that $(P)$ consists of many contour lines $f(y) = c$
        * We are standing at $x$, on the contour line $f(y) = c_x$
        * Trying to move in many directions, with the same step size
        
        $\hspace{1.0cm} \rightarrow$ Moving in the direction of $\nabla f(x)$ can lead us to the highest contour level compared to other directions
* Extension: by approximating $f$ by $f(y) = f(x) + \nabla f(x)^T (y - x) + \frac{1}{2} (y - x)^T H[f(x)] (y - x)$ where $H[f(x)]$ is the Hessian of $f$
    * The highest increment direction is the direction of the eigenvector of $H[f(x)]$ corresponding to the maximum eigenvalue
    * The lowest increment direction is the direction of the eigenvector of $H[f(x)]$ corresponding to the minimum eigenvalue

**Meaning of gradients**:
* Assumptions:
    * $f: \textbf{R}^n \to \textbf{R}$
    * $\nabla f(x) = \begin{bmatrix} \frac{\partial f}{\partial x_1} \\ \vdots \\ \frac{\partial f}{\partial x_n} \end{bmatrix}$ is the gradient of $f$ at $x$
* Conclusion: $\nabla f(x)^T (y - x)$ gives the change of $f$ (approximately) when moving from $x$ to $y$

**Meaning of Jacobian matrix**:
* Assumptions:
    * $f: \textbf{R}^n \to \textbf{R}^m$
    * $D[f(x)] = \begin{bmatrix} \frac{\partial f_1}{\partial x_1} & \cdots & \frac{\partial f_1}{\partial x_n} \\ \vdots & \ddots & \vdots \\ \frac{\partial f_m}{\partial x_1} & \cdots & \frac{\partial f_m}{\partial x_n} \end{bmatrix}$ is the Jacobian of $f$ at $x$
* Conclusion: $D[f(x)] (y - x) = \begin{bmatrix} \nabla f_1(x)^T (y - x) \\ \vdots \\ \nabla f_m(x)^T (y - x) \end{bmatrix}$
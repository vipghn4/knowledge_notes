**Derivative of $f[u(x), v(x)]$**: $\frac{\partial f}{\partial u} \frac{\partial u}{\partial x} + \frac{\partial f}{\partial v} \frac{\partial v}{\partial x}$
* Explain: 
    * $\frac{\partial f}{\partial x} = \frac{f[u(x+h), v(x + h)] - f[u(x), v(x)]}{h}$ 
    
    $\hspace{0.7cm} = \frac{f[u(x+h), v(x + h)] - f[u(x+h), v(x)]}{h} + \frac{f[u(x+h), v(x)] - f[u(x), v(x)]}{h}$ 
    
    $\hspace{0.7cm} = \frac{f[u(x+h), v(x + h)] - f[u(x+h), v(x)]}{v(x+h) - v(x)} \frac{v(x+h) - v(x)}{h} + \frac{f[u(x+h), v(x)] - f[u(x), v(x)]}{u(x+h) - u(x)} \frac{u(x+h) - u(x)}{h}$ 

    $\hspace{0.7cm} = \frac{\partial f}{\partial u} \frac{\partial u}{\partial x} + \frac{\partial f}{\partial v} \frac{\partial v}{\partial x}$
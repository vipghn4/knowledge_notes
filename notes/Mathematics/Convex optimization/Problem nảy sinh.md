### Vấn đề
Giả sử ta có:
  * $x_1, x_2, x_3 \in \mathbf{R}^3$ là 3 vectors thoả mãn 3 điểm tương ứng không thẳng hàng
  * $\theta_1, \theta_2, \theta_3 \in \mathbf{R}$ là 3 scalars thoả mãn $\theta_1 + \theta_2 + \theta_3 = 1$

Xét $S = \theta_1 x_1 + \theta_2 x_2 + \theta_3 x_3 = \theta_1 x_1 + (1 - \theta_1)(\frac{\theta_2}{1 - \theta_1} x_2 + \frac{\theta_3}{1 - \theta_1} x_3)$

Ta có $\frac{\theta_2}{1 - \theta_1} + \frac{\theta_3}{1 - \theta_1} = 1$

$\hspace{1.0cm} \rightarrow \{\frac{\theta_2}{1 - \theta_1} x_2 + \frac{\theta_3}{1 - \theta_1} x_3|\theta_1 + \theta_2 + \theta_3 = 1\}$ là tập các điểm thuộc đường thẳng $d_1$ đi qua $x_2, x_3$

Giả sử $x_4$ là một điểm bất kì thuộc $d_1$, khi đó $S = \theta_1 x_1 + (1 - \theta_1) x_4$

$\hspace{1.0cm} \rightarrow S$ biểu diễn đường thẳng $d_2$ đi qua $x_1, x_4$ $\forall x_4 \in d_1$

Ta có: do $S$ biểu diễn đường thẳng $d_2$ đi qua $x_1, x_4$ $\forall x_4 \in d_1$

$\hspace{1.0cm} \rightarrow S$ không thể biểu diễn đường thẳng đi qua $x_1$ và song song với $d_1$ (đường thẳng chứa $x_2, x_3$)

Nói cách khác, tập các đường thẳng $d_2$ mà $S$ có thể biểu diễn được sẽ không chứa đường thẳng đi qua $x_1$ và song song với $d_1$

Tổng quát hơn, xét tập $D = \textbf{aff}$ $\{x_1, x_2,  x_3\} = \{\theta_1 x_1 + \theta_2 x_2 + \theta_3 x_3|\theta_1 + \theta_2 + \theta_3 = 1\}$

$\hspace{1.0cm} \rightarrow D$ không chứa đường thẳng đi qua $x_i$ và song song với đường thẳng đi qua $x_j, x_k$ $\forall$ $1 \leq i, j, k \leq 3$ và $i \neq j \neq k$ $(1)$

Mà theo lý thuyết, $D$ là tập các điểm thuộc mặt phẳng defined bởi $x_1, x_2, x_3$ $(2)$

Ta có: $(1)$ và $(2)$ mâu thuẫn nhau ???

### Lời giải
Lập luận trên chỉ đúng khi $\theta_1 \neq 1$

Trong trường hợp $\theta_1 = 1, \theta_2 = \theta_3 = -k$ thì $S = \theta_1 x_1 + k (x_2 - x_3)$ chính là đường thẳng đi qua $x_1$ và song song với đường thẳng chứa $x_2, x_3$

***
---
title: Computer graphics
tags: Computer vision
---

[toc]

# 1. Các khái niệm cơ bản
## Đối tượng cơ bản
* *Điểm ảnh (pixel)*: Đơn vị cơ bản xây dựng nên một bức ảnh trên màn hình máy tính
* *Mành (raster)*: Cách thể hiện một đối tượng, qua một tập hợp các điểm ảnh
* *Vector*. Cách thể hiện một đối tượng qua mối quan hệ không gian 2D hoặc 3D, e.g. đoạn thẳng, đoạn cong, etc.

## Các khái niệm trong đồ họa
**Tọa độ**. Xác định một đối tượng trong thế giới thực
* *Hệ tọa độ chữ nhật*
    * Hệ tọa độ 3D trái
    * Hệ tọa độ 3D phải
* *Hệ tọa độ góc*
    * Hệ tọa độ cực (2D)
    * Hệ tọa độ cầu (3D)

>**NOTE**. Thông thường, việc xác định các đối tượng được thực hiện qua một số hệ tọa độ quan hệ với nhau

**Luồng xử lý đồ họa**.
* *Mô tả*.
    * *Đầu vào*. Các đối tượng hình học để thể hiện cảnh vật
    * *Đầu ra*. Hình ảnh
* *Luồng xử lý 3D*.

<div style="text-align:center">
    <img src="/media/T1715R2.png">
</div>

* *Luồng xử lý 2D*. 

<div style="text-align:center">
    <img src="/media/5imQYGT.png">
</div>

## Một số thuật ngữ
<div style="text-align:center">
    <img src="/media/RmNlbqH.png">
</div>

**Hệ tọa độ thế giớ thực**. Cách user mô tả các đối tượng trong thế giới thực

**Mặt phẳng nhìn (view plane)**. Cảnh vật trên thế giới được chiếu lên một mặt phẳng nhìn, từ một điểm nhìn (viewpoint), e.g. camera, mắt, etc.
* *Hệ tọa độ đi kèm*
    * Hệ tọa độ mặt phẳng nhìn (view plane coordinates)
    * Hệ tọa độ máy quay (Camera coordinates)
* *Hướng nhìn*. Hướng từ điểm nhìn, dọc theo trục dương $z$ của hệ tọa độ máy quay
* *Cửa sổ (window)*. Vùng chữ nhật ta quan tâm
* *Khối nhìn (view volume)*. Khối vô hạn, tạo ra từ các tia xuất phát từ điểm nhìn tới các điểm trong cửa sổ
* *Mặt phẳng cắt xén gần / xa*. Dùng để giới hạn các đối tượng đầu ra
* *Khối nhìn đã cắt (truncated view volume)*. Khối nắm trong khối nhìn, chặn bởi hai mặt cắt xén

# 2. Các thuật toán tô phủ
## Tổng quan
**Các lớp thuật toán tô phủ**
* *Các thuật toán dựa trên đa giác*.
    * Khi phần cần tô là các đa giác, và
    * Khi ta có thể dùng phương trình toán học biểu diễn các cạnh
* *Các thuật toán dựa trên điểm*. Sử dụng khi đường viền vừa có thể là đa giác, vừa có thể là một tập các điểm

**Xác định một điểm nằm trong khu vực cần tô**
* *Option 1*. Kiểm tra tính chẵn lẻ khi kẻ một tia, từ điểm đó, và đếm số lượng giao với đường viền
    * *Áp dụng*. Các thuật toán dựa trên đa giác, và trên điểm
* *Option 2*. Bắt đầu từ điểm hạt giống, ta loang ra các điểm xung quanh mà không vượt ra khỏi viền bao
    * *Áp dụng*. Các thuật toán dựa trên điểm

**Bài toán tô phủ loang (flood fill problem)**. 
* *Giả thiết*. Với 2 màu khác nhau $c$ và $c'$, một tập các điểm $A$ có cùng màu $c$ được bao quanh bởi các điểm có màu khác $c$ và $c'$
* *Yêu cầu*. Thay màu tất cả các điểm thuộc $A$ thành $c'$

**Thuật toán tô phủ loang** giải quyết bài toán tô phủ loang

## Phương pháp
**Thuật toán tô phủ cơ bản**
```python
def BFA(x, y):
    if inside(x, y):
        set(x, y)
        BFA(x, y-1), BFA(x, y+1)
        BFA(x-1, y), BFA(x+1, y)
```

* *Nhược điểm*. 4 lần gọi đệ quy, dãn tới không hiệu quả, i.e. mỗi điểm đi qua rất nhiều lần

**Thuật toán tô phủ Smith**. Mỗi điểm đi qua 2 lần

```python
def fill(x, y):
    if not inside(x, y):
        return
    stack.push((x, y))
    while stack.not_empty():
        x, y = stack.pop()
        if inside(x, y):
            rx, lx = fill_right(x, y), fill_left(x, y)
            scan_hi(x, y, lx, rx), scan_lo(x, y, lx, rx)

def fill_right(x, y):
    while inside(x, y) and x <= XMAX:
        set(x, y)
        x += 1
    x -= 1
    return x

def fill_left(x, y):
    while inside(x, y) and x >= XMIN:
        set(x, y)
        x -= 1
    x += 1
    return x

def scan_hi(x, y, lx, rx):
    if y + 1 > YMAX:
        return
    x = lx
    while x <= rx:
        while not inside(x, y+1) and x <= rx:
            x += 1
        if x <= rx:
            stack.push(x, y+1)
            while inside(x, y+1) and x <= rx:
                x += 1
```

* *Nhược điểm*. Ta phải xét mỗi điểm 2 lần, khi ta cho cả điểm ở trên và ở dưới của điểm hiện tại vào ngăn xếp
    * *Giải thích*. Khi xét lấy điểm ở trên ra, ta lại xét lại điểm hiện tại

**Thuật toán Fishkin**. Lưu trữ thêm một số thông tin để phân biệt ba loại "vùng tối" khác nhau

# 3. Vẽ đường thẳng
## Tổng quan
**Bài toán**
* *Ràng buộc*. Mỗi pixel chỉ có thể được thắp sáng hoặc không
* *Ý tưởng*: Xấp xỉ đường thẳng một cách rời rạc, i.e. chiếu sáng các điểm gần nhất với đường thẳng

**Đường thẳng lý tưởng**
* Trông phải thẳng và liên tục
* Phải bắt đầu và kết thúc đúng điểm 
* Phải có mật độ điểm đều
* Phải có mật độ điểm không phục thuộc vào độ dài và hệ số góc của đoạn thẳng
* Phải được vẽ ra một cách nhanh chóng

## Phương pháp
**Đường thẳng đơn giản**. Dựa trên phương trình đường thẳng $y=mx+b$
* *Ý tưởng*. tăng $x$ và tìm ra  $y$
* *Ưu điểm*. Chạy tốt với những đường thằng có hệ số góc tối đa là 1
    * *Giải thích*. Với mỗi giá trị $x$, có 1 giá trị $y$
* *Nhược điểm*. Không tốt cho các đường thẳng hệ số góc lớn hơn 1
    * *Giải thích*. Với mỗi giá trị $x$, có nhiều giá trị $y$
    * *Giải pháp*. 
        * Sử dụng phương pháp đối xứng
        * Thay đổi vai trò của các trục tọa độ theo từng góc phần tám (45 độ)

**Thuật toán Digital Differential Analyzer (DDA)**. Dựa trên phương trình tham số
$$\frac{dx}{dy}=\frac{\varepsilon (x_1 - x_0)}{\varepsilon (y_1 - y_0)}=\frac{\varepsilon \Delta x}{\varepsilon \Delta y}$$
với $\varepsilon \in \mathbb{R}$
* *Ý tưởng*. Tô màu chuỗi điểm $p_{i+1}=p_i+\varepsilon\cdot(\Delta x, \Delta y)$
    >**NOTE**. Để hiển thị được, ta cần $q_i$ là các điểm với tọa độ làm tròn từ $p_i$

    >**NOTE**. Chọn đầu vào `(x0, y0)` và `dx_dt`, `dy_dt` sao cho `dx_dt < 1` và `dy_dt < 1`, i.e. khi ta tăng $t$ thêm `dt` thì ta không bị sót pixel nào 
* *Mã giả*.
    ```python
    x, y = x0, y0
    for t in range(0, 1, step):
        x = x + dx_dt
        y = y + dy_dt
        set(x, y)
    ```
* *Triển khai*. 
    * *DDA đơn giản*. Chọn `dt` là `max(dx, dy)` với `dx = x2 - x1` và `dy = y2 - y1`
    * *DDA đối xứng*. Chọn `dt` là `2^n` với `2^(n-1) <= max(dx, dy) < 2^n`
* *Nhược điểm*. Cần nhiều phép toán số thực
    * *Giải pháp*. ta cần nhiều phép số nguyên hơn

**Thuật toán Bresenham**. Trong DDA, giả sử $x$ luôn tăng lên 1, ta cần tính $y$ hiệu quả
* *Ý tưởng*. Ta có
$$\begin{aligned}
    x_i &= x_{i-1} + 1\\
    y_i &= y_{i-1} + b/a
\end{aligned}$$
* *Triển khai*. 
    * Nếu $y_0=0$, khi nào $y_i=1$? Ta sẽ làm tròn $y_i$
    * So sánh $2b, 4b, \dots$ với $a, 3a, \dots$ thay vì tính $b/a$
        * *Giải thích*. Tránh các phép tính số thực
        * *Cụ thể*. 
            * Đặt biến quyết định $d=2b-a$, i.e. 
            $$d>0 \Leftrightarrow b/a>1/2\\d\leq 0\Leftrightarrow b/a\leq1/2$$
            * Mỗi lần cần cộng thêm $2b$ vào $d$, i.e.
            $$(n+1)b/a>1/2\Leftrightarrow 2nb+2b>a$$
            * Đến khi $d>0$, trừ thêm $2a$ vào $d$, i.e.
            $$nb/a-(1+1/2)=nb/a-3/2>0\Leftrightarrow 2nb>3a$$
* *Mã giả*

    ```python
    def draw_line(start_x, start_y, end_x, end_y, a, b):
        x, y = start_x, start_y
        d = 2*b - a
        while True:
            set(x, y)
            if x == end_x:
                return
            if d >= 0:
                y += 1
                d -= 2*a
            x += 1
            d += 2*b
    ```

**Thuật toán điểm giữa**. Phù hợp hơn cho đường cong và đoạn thẳng 3D
* *Thuật toán cơ bản*. Dựa vào phương trình đường thẳng $F(x,y)=ax+by+c=0$ với $0 \leq a \leq -b$, i.e. hệ số góc thuộc $[0,1]$
    * *Quan sát*.
        * Nếu $F<0$, $(x,y)$ nằm trên đường thẳng
        * Nếu $F>0$, $(x,y)$ nằm dưới đường thẳng
    * *Ý tưởng*. Tại mỗi thời điểm
    $$\begin{aligned}
        x_{i+1} &= x_i + 1\\
        y_{i+1} &= y_i + \mathbf{1}_{f(x_i+1, y_i+1/2) > 0} 
    \end{aligned}$$
    * *Nhược điểm*.
        * Cần tìm $a,b,c$

    >**NOTE**. Các hệ số góc khác được xử lý như trong Bresenham. Đoạn thẳng đứng được xử lý riêng
* *Thuật toán điểm giữa*. Dựa vào phương trình $y=\frac{dy}{dx}x+b$ với, i.e. 
$F(x,y)=dy\cdot x - dx\cdot y + c=0$
    * *Đại lượng quyết định*: $d=F(x_p+1,y_p+1/2)$ với $x_p,y_p$ là tọa độ nguyên mới nhất
    * *Tính nhanh $d$*. 
    
    $$\begin{aligned}
        F(x_p+2,y_p+1/2)&=F(x_p+1,y_p+1/2)+dy\\
        F(x_p+2,y_p+3/2)&=F(x_p+1,y_p+1/2)+dy-dx
    \end{aligned}$$

* *Tóm tắt thuật toán*. Ở mỗi, bước ta tăng $x$ thêm $1$ và giữ nguyên $y$ cho tới khi $(x,y)$ nằm dưới đường thẳng, lúc này ta tăng $y$ lên 1 và tiếp tục như cũ

```python
dx, dy = x2 - x1, y2 - y1
d = 2*dy - dx
incrE = 2*dy
incrNE = 2*(dy - dx)
x, y = x1, y1

drawPixel(x, y)
while x < x2:
    if d <= 0:
        d += incrE
        x += 1
    else:
        d += increNE
        x, y = x + 1, y + 1
    drawPixel(x, y)
```

>**NOTE**. Ta có thể dùng thuật toán điểm giữa để vẽ đường tròn

# 4. Các thuật toán cắt xén (clipping)
## Tổng quan

<div style="text-align:center">
    <img src="/media/c2Dq9Rp.png">
    <figcaption>Khung hình trong 2D</figcaption>
</div>

**Khung hình trong 2D**. Trong 2D, thế giới là một mặt phẳng vô hạn, trong một hệ tọa độ nhất định
* *Cửa sỏ*. Một vùng trong mặt phẳng 2D mà ta quan tâm
* *View port*. Trong thiết bị hiển thị, ta xác định một vùng để hiển tại (viewport) và dùng hệ tọa độ của thiết bị
    * *Các bước*.
        1. Cắt bỏ các vật thể ngoài cửa sổ
        2. Tịnh tiến cho khớp với viewport
        3. Co giãn theo hệ tọa độ của thiết bị

**Đa giác**.
* *Các loại đa giác*
    * *Đa giác đối tượng (subject polygon)*. Đa giác được cắt
    * *Đa giác cắt (clip polygon)*. Đa giác dùng để cắt
* *Thuật ngữ*.
    * *Điểm rẽ*. Điểm nằm trên các cạnh giao của 2 vùng cắt mà cần được thêm vào, để giữ tính liên tục của đa giác ban đầu

**Các loại thuật toán cắt đường thẳng**.
* Loại dùng mã hóa các đầu đoạn thẳng, e.g. Cohen-Sutherland
* Loại dùng phương trình tham số xác định các đoạn thẳng, e.g. Cyrus-Beck, Liang-Basky, etc.

>**NOTE**. Khi ta cắt 1 đa giác bằng cách cắt từng cạnh, song ta cần tính tới các điểm rẽ (không hiệu quả)

**Các thuật toán cắt đa giác**.
* Thuật toán dựa trên điểm rẽ, e.g. Liang-Basky, etc.
    * *Ý tưởng*. Quét qua các đoạn của đa giác đối tượng và cắt mỗi đoạn đó
* Các thuật toán còn lại, i.e. tìm điểm rẽ một cách không chủ ý

## Clipping trong 2D
**Clipping trong 2D**. Cần cắt những đối tượng cơ bản theo các cạnh của cửa sổ
* Hai đầu mút trong cửa sổ ~> Chấp nhận
* Hai đầu mút ngoài cửa sổ và cùng phía ~> Loại bỏ

### Clipping đoạn thẳng
**Thuật toán Cohen-Sutherland**. Thuật toán phổ biến nhất (vì sự đơn giản của nó)

<div style="text-align:center">
    <img src="/media/EMjRuGw.png">
</div>

* *Ý tưởng*. Gán 4 bit (gọi là outcode) cho mỗi đầu mút, i.e. $c(P)=x_3x_2x_1x_0$
    * $x_1 = y > y_\text{max}$
    * $x_2 = y < y_\text{min}$
    * $x_3 = x > x_\text{max}$
    * $x_4 = x < x_\text{min}$
* *Phương pháp*. Giả sử $P$, $Q$ là đầu mút của đoạn cần cắt
    1. Mã hóa $P_1, P_2$ thành $c_1, c_2$
    2. Chấp nhận / loại bỏ (đơn giản) đoạn thẳng nếu
        * $c_1 \lor c_2 = 0$, i.e. đoạn nằm hoàn toàn trong cửa sổ
        * $c_1 \land c_2 \neq 0$, i.e. đoạn nằm hoàn toàn ngoài cửa sổ
    3. Nếu đoạn thẳng chưa được chấp nhận / loại bỏ, ta chia đoạn đó ra. sau đó quay lại B1 với những đoạn mới
        * Ta đặt

            $$\begin{cases} 
                P=P_2, Q=P_1 & c_1 = 0\\
                P=P_1, Q=P_2 & c_1\neq 0
            \end{cases}$$
        * Xác định cạnh (của đa giác cắt) để cắt bằng bit 1 trái nhất trong $c(P)$
        * Đặt $A$ là giao của $[P, Q]$ với đường để cắt
        * Lặp lại các bước với đoạn $[A, Q]$

**Thuật toán Cyrus & Beck**. A line clipping algorithm designed to be more efficient
* *Parameteric equation of a line*. $p(t)=tp_1 + (1-t)p_0$ where $t\in[0,1]$
* *Find intersection point with the clipping window*. Calculate the value $d = n\cdot (p(t) - p_E)$
    * Notation
        * $p_E$ is a point on the clipping plane $E$
        * $n$ is the normal (pointing away from interior) of the current clipping
    * Observation
        * If $d<0$, the vector pointed towards interior
        * If $d = 0$, the vector pointed parallel to plane containing $p$
        * If $d>0$, the vector pointed away from interior
* *Clipping algorithm*. 
    1. Calculate the normals of every edge
    2. Calculate the vector for the clipping line
    3. Calculate 
    $$\forall i,t=\frac{n_i \cdot (p(0) - p_{E_i})}{-n_i \cdot (p(1) - p(0))}=\frac{n_i \cdot(p_{E_i} - p(0))}{n_i \cdot (p(1) - p(0))}$$
    1. Values of $t$ are classified as entering or exiting (from all edges) via their denominators
    2. Choose one value of $t$ from each group. 
        * $t_E$ is the $t$ value for entering intersection point, i.e. the minimum of $t$ values, for which $n_i (p(1) - p(0))$ is negative, and $1$
        * $t_L$ is the $t$ value for exiting intersection point, i.e. the maximum of $t$ values, for which $n_i (p(1) - p(0))$ is positive, and $0$
    3. If the line intersects the window, we have cases
        * If $0<t_E<t_L<1$, the line is partially inside the clipping window
        * If $0\leq t_E\leq t_L \leq 1$, the line has one point inside, i.e. $t_E = t_L$, or the intersection points are on the end points of the line, i.e. $0=t_E<t_L=1$
        * If $t_E<0<1<t_L$, the line completely inside the window
        * If $t_L<t_E$, the the line is completely outside the window, i.e. 
            * When $t_E>1$ and is clipped to $1$, i.e. $t_L < t_E = 1$
            * When $t_L<0$ and is clipped to $0$, i.e. $0=t_L<t_E$

**Thuật toán Liang-Barsky**
* *Phương trình tham số đường thẳng nối $(x_1,y_1)$ và $(x_2,y_2)$*. Xét $\Delta x=x_2-x_1$ và $\Delta y = y_2-y_1$, ta có
$$\begin{aligned}
    x = x_1 + t \Delta x\\
    y = y_1 + t \Delta y
\end{aligned}$$
* *Điểm thuộc cửa sổ*. $P$ thuộc cửa sổ $W$ khi và chỉ khi
    * $x_\text{min}\leq x_1+t\Delta x \leq x_\text{max}$
    * $y_\text{min}\leq y_1+t\Delta y \leq y_\text{max}$
* *Ý tưởng*.
    * Biểu diễn lại điều kiện điểm thuộc cửa sổ
        * $-t\Delta x\leq x_1-x_\text{min}$
        * $t\Delta x\leq x_\text{max}-x_1$
        * $-t\Delta y\leq y_1-y_\text{min}$
        * $t\Delta y\leq y_\text{max}-y_1$
    * Đặt biến phụ $c_i, q_i$, ta có 4 BĐT $c_i t \leq q_i$ từ 4 điều kiện trên, i.e. $t_k=q_k/c_k$
* *Quan sát*
    * Nếu $c_k>0$, đường thẳng đi từ phía trong ra phía ngoài của biên $B_k$ khi $t$ tăng. Ta gọi $t_k$ là điểm ra
    * Nếu $c_k<0$, đường thẳng đi từ phía ngoài vào phía trong của biên $B_k$ khi $t$ tăng. Ta gọi $t_k$ là điểm vào
    * Nếu $c_k=0$, đường thẳng song song với $B_k$, i.e. $x_2 = x_1$ or $y_2 = y_1$
        * Nếu $\exists k, c_k=0, q_k<0$, đường thẳng hoàn toàn nằm ngoài cửa sổ, i.e.
            * $x_2 = x_1 < x_\text{min}$ or $x_\text{max} < x_1 = x_2$, or
            * $y_2 = y_1 < y_\text{min}$ or $y_\text{max} < y_1 = y_2$
        * Nếu $\forall k, c_k=0 \implies q_k\geq 0$, đường thẳng nằm trong cửa sổ, i.e.
            * $x_2 = x_1 \geq x_\text{min}$ and $x_\text{max} \geq x_1 = x_2$, or
            * $y_2 = y_1 \geq y_\text{min}$ and $y_\text{max} \geq y_1 = y_2$
* *Kết luận*. 
    * Loại bỏ đoạn thẳng nếu
        * Một giá trị $t$ ứng với điểm vào $>1$
        * Một giá trị $t$ ứng với điểm ra $<0$
        * Giá trị vào > giá trị ra
    * Nếu $0<t_0<t_1<1$ với $t_0$ là $t$ vào, $t_1$ là $t$ ra, ta lấy
        * $t_0 = \max(0,\max(t_\text{vào}))$
        * $t_1 = \min(1,\min(t_\text{ra}))$

### Clipping đa giác
**Clipping đa giác**. Lần lượt sử dụng các cạnh của cửa sổ để cắt đa giác

**Thuật toán Sutherland-Hodgman**. Extend each line of the clip polygon in turn, and select only vertices from the subject polygon that are on the visible side
* *Idea*. Begin with an input list of all vertices in the subject polygon
    1. One side of the clip polygon is extended infinitely in both directions
    2. The path of the subject polygon is traversed
        * Vertices from the input list are inserted into an output list if they lie on the visible side of the extended clip polygon line
        * New vertices are added to the output list where the subject polygon path crosses the extended clip polygon line
 * *Implementation*

    ```python
    output_list = subject_polygon

    for clip_edge in clip_polygon:
        input_list = output_list
        output_list.clear()

        for i in range(input_list):
            cur_point = input_list[i]
            prev_point = input_list[(i+len(input_list)-1)%len(input_list)]

            intersection = get_intersection(prev_point, cur_point, clip_edge)
            if is_visible(cur_point, clip_edge):
                if not is_visible(prev_point, clip_edge):
                    output_list.add(intersection)
                output_list.add(cur_point)
            elif is_visible(prev_point, clip_edge):
                output_list.add(intersection)
    ```
* *Advantage*. Avoid generating new data, e.g. turning points 

## Clipping 3D
**Clipping 3D**. Sử dụng thuật toán Cohen-Sutherland với mã 6 bit
* Sử dụng mã 6 bit, i.e. cắt 6 lần (6 mặt) thay vì 4 lần
* Chấp nhận đơn giản khi cả mã của 2 đầu mút là 0
* Thực hiện AND logic, loại bỏ nếu kết quả khác 0
* Với các đoạn còn lại, tìm phần giao với một mặt phẳng của khối nhìn vào thêm hai đoạn thẳng mới vào để xử lý lại

**Extended Sutherland-Hodgman**. Clip for 6 planes, rather than 4 edges

# 5. Các phép biến đổi
## Một số hệ tọa độ

<div style="text-align:center">
    <img src="/media/hrcBR1b.png">
</div>

**Một số hệ tọa độ**
* *Hệ tọa độ thế giới (world coordinates)*. Hệ tọa độ user dùng để định nghĩa các đối tượng
* *Hệ tọa độ hình dạng (shape coordinates)*. Hệ tọa độ dùng để định nghĩa hình dạng
* *Hệ tọa độ máy quay (camera coordinates)*.
    * *Perspective view*. Toàn cảnh thế giới thu được qua phép chiếu lên một mặt phẳng
    * *Các thuộc tính máy quay*.
        * Vị trí $\mathbf{p}$
        * Hướng nhìn $\mathbf{v}$
        * Hướng lên $\mathbf{w}$
        * Khoảng cách $\mathbf{d}$ từ máy quay đến mặt phẳng nhìn

## Các phép biến đổi 
**Phép biến đổi** có dạng $P' = T(P)$ với $P$ là một điểm

**Các loại biến đổi (theo bản chất)**. Continuous, one-to-one, invertible

**Các loại biến đổi (theo sự bất biến và đối xứng)**.
* *Isometry (bảo tồn khoảng cách)*. Reflection, rotation, translation
* *Similarity (bảo tồn góc)*. Uniform scale
* *Affine (bảo tồn các đường thẳng song song)*. Non-uniform scale, shear, or skew
* *Collineation (đường thẳng được giữ là đường thẳng)*. Perspective
* *Non-linear (đường thẳng trở thành đường cong)*. Twists, etc.

## Các phép biến đổi cơ bản
**Tịnh tiến**. $P' = P + T$ where
$$P=\begin{bmatrix}x\\y\end{bmatrix},\quad T=\begin{bmatrix}dx\\dy\end{bmatrix}$$

**Scaling (co dãn)**. $P' = S \cdot P$ where
$$P=\begin{bmatrix}x\\y\end{bmatrix},\quad S=\begin{bmatrix}s_x&0\\0&s_y\end{bmatrix}$$

**Shear (kéo dãn)**. $P' = S\cdot P$ where
* $S=\begin{bmatrix}1&k\\0&1\end{bmatrix}$ nếu kéo theo chiều $x$
* $S=\begin{bmatrix}1&0\\k&1\end{bmatrix}$ nếu kéo theo chiều $y$

**Rotation (quay)**. $P' = R\cdot P$ where
$$R=\begin{bmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{bmatrix}$$

**Rotation around center**.
1. Translate the polygon so that the center matches the origin
2. Rotate the polygon about the origin
3. Re-translate the rotated polygon

**Homogeneous coordinates**. $(x,y,t)$ instead of $(x,y)$, i.e. to combine translation, rotation, and scaling easily
* *Affine transformation*. Combination of translation, rotation, and scaling, i.e. $P' = T\cdot P$
* *From homogeneous to Decartes*. $(x,y,w) \leftrightarrow (x/w,y/w)$

## 3D transformations
**Idea**.
* Use homogeneous coordinates
* Use $4\times 4$ transformation matrices rather than $3\times 3$
* $z$ points outside, i.e. left-hand coordinates

# 6. Phép chiếu (projection)
**Phép chiếu**. Dùng để chuyển vật thể / cảnh 3D về thiết bị hiển thị 3D

<div style="text-align:center">
    <img src="/media/HdYioqW.png">
</div>

>**NOTE**. Cần thực hiện cắt với một khối 3D, i.e. 6 mặt phẳng tạo nên hình chóp cụt

* *Phép chiếu*. Chuyển một điểm từ hệ tọa độ $n$ chiều về hệ tọa độ $m<n$ chiều
    * *Đường chiếu (projector)*. Phép chiếu được xác định bởi các đường chiếu
    * *Center of projection*. Các đường chiếu xuất phát từ tâm chiếu, đi qua mọi điểm của vật thể, và giao với bề mặt chiếu, tạo nên ảnh chiếu
* *Các phép chiếu*.
    * Phối cảnh (perspective)
    * Song song (orthogonal)

**Phép chiếu phối cảnh**. Xác định bởi mặt phẳng chiếu và tâm chiếu
* *Đặc trưng*
    * Định luật phối cảnh gần xa, i.e. kích thước hình chiếu của một vật biến đổi theo tỉ lệ nghịch với khoảng cách từ vật tới tam chiếu
    * Điểm ảo (vanishing point). Tập các đường song song, qua phép chiếu, giao với nhau tại 1 điểm
* *Các phép chiếu phối cảnh*. Các đường thẳng song song với trục tọa độ hội tụ tại điểm biến mất của trục
    * *Ý tưởng*. Phân loại các phép chiếu dựa trên số lượng điểm biến mất, i.e. số trục cắt các mặt phẳng chiếu
    * *Các phép chiếu*.
        * Phép chiếu 1 điểm, i.e. mặt phẳng chiếu chỉ cắt 1 trục
        * Phép chiếu 2 điểm, i.e. mặt phẳng chiếu cắt 2 trục
        * Phép chiếu 3 điểm, i.e. mặt phẳng chiếu cắt 3 trục
* *Cơ sở toán học*. $P = T\cdot P$ where
$$T = \begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&1/d&0\end{bmatrix}$$
i.e. $x_p=\frac{x}{z/d},y_p=\frac{y}{z/d},z_p=d$

* *Ưu điểm*.
    * Kích thước ảnh chiếu của vật thể thay đổi theo khoảng cách đến tâm chiếu
    * Giống như máy ảnh (trông thực tế)
* *Nhược điểm*.
    * Không hữu dụng để đo đạc

**Phép chiếu song song**.
* *Cơ sở toán học*. $P = T\cdot P$ where
$$T = \begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&0&d\\0&0&0&1\end{bmatrix}$$
i.e. $x_p=x, y_p=y, z_p=d$

# 7. Mô hình hóa đối tượng
## Các dạng thể hiện 3D
**Vẽ kỹ thuật**. Phương pháp đầu tiên mô hình hoa đối tượng 3D

>**NOTE**. Đây chỉ là phương tiện liên lạc giữa con người, không liên can máy tính

* *Ý tưởng*. Thể hiện các vật thể dưới các phép chiếu thẳng
* *Nhược điểm*.
    * Khó xác định xem bao nhiêu phép chiều 2 chiều là đủ

**Thể hiện khung dây**. Biếu diễn các vật thể chỉ bằng các cạnh của chúng
* *Ưu điểm*.
    * Hình dung kết cấu bên trong mô hình 3D
    * Đơn giản, nhanh chóng
    * Cho phép nhanh chóng xem qua các thay đổi, hoặc xoay vật thể theo nhiều góc
* *Nhược điểm*. Không cho phép hình dung toàn bộ chi tiết của vật thể

**Thể hiện bề mặt qua đa giác**. Dạng 3D cơ bản nhất trong hầu hết các ứng dụng
* *Ưu điểm*. 
    * Xử lý dễ và nhanh
    * Các ứng dụng sử dụng hình khối khác đều đưa về đa giác để xử lý
    * Phù hợp với thuật toán scan-line algorithm
* *Dạng đa giác*. Tam giác hoặc tứ giác
    * *Giải thích*. Ta có thể xấp xỉ bất cứ hình nào bởi các đa giác. Để tăng độ chính xác, ta tăng số đa giác

## Thể hiện và lưu trữ đa giác
**Lưới đa giác**. Một tập hợp các đa giác, hay các mặt, kết hợp lại tạo thành lớp vỏ của một đối tượng
* *Ứng dụng*. Thể hiện vật thể 3D

**Lưu trữ lưới đa giác**. Được lưu trữ theo nhiều cách, e.g. lưu đỉnh, lưu cạnh, lưu mặt
* *Quan sát*.
    * Các đa giác kề nhau có thể chung cạnh
    * Để không có khoảng trống giữa các đa giác liền kề do quá trình tính toán số thực, các đa giác có cạnh chung nên dùng cùng giá trị tọa độ cho 2 đầu mút của cạnh chung
* *Kết luận*. Dùng cấu trúc chứa các cạnh, với tham chiếu tới các điểm
* *Ưu điểm*.
    * Tiết kiệm bộ nhớ
    * Giải quyết cạnh chung, điểm chung

>**NOTE**. Thường người ta bỏ qua danh sách cạnh, chỉ lưu trữ danh sách đỉnh và đa giác bề mặt

**Thể hiện đa giác**. 
* *Thể hiện tam giác*. Thể hiện bằng 3 đỉnh và 3 cạnh

    >**NOTE**. Nếu ta biến đổi 1 tam giác, ta phải biến đổi tọa độ của 3 điểm, i.e. 3 phép toán ma trận cho 1 tam giác
* *Thể hiện đa giác*. Để tiết kiệm không gian lưu trữ, ta lưu
    * *Quạt tam giác*. Để thêm một tam giác mới, ta chỉ cần thêm 1 đỉnh
        * *Ứng dụng*. Thể hiện các hình khối phức tạp
    * *Chuỗi tam giác*. Các tam giác xuất hiện theo chuỗi. Một tam giác mới được thể hiện là 1 điểm mới thêm vào chuỗi
        * *Ứng dụng*. Thể hiện các vật đặc

## Tạo lưới và phân tách
**Tạo lưới**. Quá trình phân tách một bề mặt phức tạp thành các đối tượng đơn giản, e..g tam giác 3D
* *Quá trình tạo lưới*. 
    * Áp dụng ở khâu tiền xử lý
    * Được lưu trữ lại trước khi đưa vào luồng xử lý đồ họa (tăng hiệu quả xử lý)

**Thuật toán phân tách đơn giản**. Chuyển các đa giác thành các quạt tam giác
* *Ý tưởng*. 
    * Giữ một đỉnh làm đỉnh chung của mọi tam giác
    * Lấy đỉnh chung và 2 đỉnh tiếp theo làm 1 tam giác

**Tạo lưới cho các bề mặt đơn giản**.
* *Các bề mặt đơn giản*. Hình cầu, hình ống, etc.
* *Option 1: Tạo lưới theo kinh / vĩ độ (hình cầu)*
    * *Nhược điểm*. Các tứ giác sinh ra có kích thước rất khác nhau
* *Option 2: Tạo lưới theo khối 8 mặt và 20 mặt*. Tạo ra các tam giác có kích thước gần bằng nhau
    * *Ý tưởng*. Xấp xỉ một hình cầu với một khối 8 mặt
    * *Phương pháp*. 
        1. Mỗi tam giác được chia ra bằng cách tạo ra đỉnh mới ở giữa các cạnh của tam giác sẵn có
        2. Nối các đỉnh mới để tạo ra 3 cạnh mới, i.e. 4 tam giác được tạo ra từ tam giác gốc
        3. Chuẩn hóa tọa độ các đỉnh mới, i.e. scale các đỉnh về khoảng cách 1 so với gốc tọa độ

**Tách đa giác thành các tam giác**. 
1. Xét 1 tam giác ABC đang có
2. Kiểm tra xem mọi điểm có nằm ngoài tam giác ABC không
3. Nếu mọi điểm nằm ngoài tam giác thì lưu tam giác và tiếp tục với đỉnh trái nhất tiếp theo, i.e. ABD
4. Nếu có 1 điểm nằm trong, tạo nên một tam giác mới với điểm nằm trong trái nhất

**Thuật toán quét đơn giản**. Sử dụng để tô màu đa giác
* *Ý tưởng*. Với mỗi đường quét (scan-line), ta tìm các giao điểm của đường quét với đa giác và tô màu phần nằm trong đa giác của đường quét

##  Mô hình khối rắn
**Mô hình khối rắn**. Khắc phục sự nhập nhằng của thể hiện khung dây
* *Cách tạo*. 
    * Quét chụp đối tượng
    * Quét cong các bản thảo 2D

**Liệt kê không gian bao phủ**. Một cách mô hình hóa đối tượng
* *Ý tưởng*. 
    * Toàn bộ không gian bao phủ được chia thành các voxels
    * Mỗi đối tượng được biểu diễn bởi một tập các voxels

    >**NOTE**. Các voxel có thể có kích thước không giống nhau và không có hình lập phương

**Mô hình khối rắn xây dựng**. Một phương pháp mô hình hóa đối tượng
* *Ý tưởng*. Sử dụng các mẫu cơ bản, là các mô hình khối rắn, và các toán tử logic, để tạo nên các bề mặt hoặc đối tượng phức tạp
    * *Các mẫu cơ bản*. Khối hộp, trụ, lăng trụ, chóp, cầu, nón, etc.
    * *Các phép logic cơ bản*. Hợp, giao, loại trừ, etc.
    
# 8. Thuật toán mặt hiện
## Tổng quan
**Các thuật toán mặt hiện**.
* *Chính xác theo đối tượng*. Với mỗi đối tượng $O$ trong thực tại, tìm phần $A$ của $O$ có thể nhìn thấy và hiển thị $A$ tương đối
* *Chính xác theo ảnh*. Với mỗi điểm ảnh trên màn hình, 
    * Xác định vị trí điểm ảnh mà đối tượng $O$ có bị tia chiếm (từ điểm nhìn) chạm tới
    * Nếu $O$ bị nhìn thấy thì hiển thị màu phù hợp
    * Nếu $O$ không bị nhìn thấy thì hiển thị màu nền
* *Ưu tiên theo danh sách*. Trung gian của 2 cách trên
    * Tính toán trước trong không gian đối tượng, thứ tự hiện của các mặt
    * Quét chuyển các đối tượng vào không gian ảnh theo thứ tự từ sau ra trước

## Phương pháp
### Ưu tiên theo danh sách
**Loại bỏ mặt quay vào trong**. Loại bỏ các cạnh chung giữa những mặt quay vào trong (mặt ẩn)
* *Mặt quay vào trong của một đối tượng*. Mặt ngược hướng với máy quay
* *Ý tưởng*. Một mặt có hướng được coi là quay vào trong (đối với vector $v$) nếu góc giữa vector pháp tuyến $n$ và $v$ nằm trong khoảng từ $0$ đến $90^o$, i.e. $n^T v \geq 0$
    * $n^T > 0$. Mặt sau
    * $n^T v < 0$. Mặt trước
    * $n^T v = 0$. Song song với hướng nhìn

>**NOTE**. Ở đây gốc tọa độ là tâm của vật

**Thuật toán ưu tiên theo danh sách Schumacker**. Gán thứ tự ưu tiên cho các mặt
* *Ý tưởng chung*.
    1. Xác định điểm nhìn
    2. Loại bỏ các mặt quay vào trong
    3. Căn cứ độ ưu tiên của các mặt còn lại để xác định mặt nào đứng trước, i.e. độ ưu tiên thâp sẽ không bao giờ bị che khuất bởi độ ưu tiên cao
    4. Áp dụng thuật toán của người thợ sơn
* *Thuật toán của người thợ sơn*. Vẽ các bề mặt theo thứ tự từ cao đến thấp
* *Nhược điểm*. Xác định thứ tự

**Thuật toán sắp xếp theo chiều sâu Newell-Newell-Sancha**. Sắp xếp các đối tượng theo chiều sâu dựa trên giá trị $z$
* *Ý tưởng*.
    1. Khởi tạo thô thứ tự ban đầu của các mặt đa giác dựa trên giá trị $z$ của đỉnh xa nhất so với điểm nhìn
    2. Bắt đầu với đa giác $P$ cuối cùng trong danh sách, i.e. đa giác xa nhất so với điểm nhìn, và đa giác tiếp theo $Q$
    3. Kiểm tra xem $P$ có thể được vẽ ra thông qua xét xem $P$ và $Q$ có tách biệt về độ sâu không
    4. Nếu (3) false, ta cần xét tập các đa giác ${QS}$ giao $P$ theo chiều sâu
    5. Thực hiện các phép thử
        * Có thể phân tách $P$ và ${QS}$ theo $x$ không ?
        * Có thể phân tách $P$ và ${QS}$ theo $y$ không ?
        * $P$ có nằm ở phần xa của ${QS}$ không ? i.e. all vertices of $P$ lie deeper than the plane of $Q$
        * ${QS}$ có nằm ở phần gần của $P$ không ? i.e. all vertices of $Q$ lie closer than the plan of $Q$
        * Hình chiếu quả $P$ và ${QS}$ có rời rạc không ?
    6. Nếu tất cả phép thử đều sai, ta hoán đối $P$ với 1 mặt trong ${QS}$ và lặp lại các phép thử

    >**NOTE**. Ta phải đánh dấu các mặt trong ${QS}$ để tránh vòng lặp vô hạn
* *Ưu điểm*. Linh hoạt hơn thuật toán Schumacker, i.e. tính toán thứ tự chiều sâu, không dựa vào thứ tự ưu tiên như Schumacker

**Thuật toán phân vùng không gian nhị phân**.
* *Ý tưởng*.
    1. Chuyển danh sách đa giác sang cấu trúc cây nhị phân
    2. Duyệt cây BSP và vẽ các đa giác ra bộ đệm khung, theo thứ tự từ sau ra trước
* *Xây dựng cây BSP*
    1. Chọn đa giác $P$ bất kì từ danh sách hiện tại, đặt vào gốc
    2. Kiểm tra các đa giác còn lại xem chúng thuộc nửa không gian nào, chia bởi $P$
        * Nếu cùng phía điểm nhìn, ta gán chúng vào cành bên trái
        * Nếu khác phía, ta cán vào cành bên phải
        * Nếu giao với $P$ thì chia đôi đa giác này bởi $P$ và gán mỗi nửa đa giác vào cành con tương ứng
    3. Lặp lại bước trên với 2 cành con trái và phải
* *Chọn đa giác để chia*.
    * *Quy tắc tham lam*. Chọn đa giác sẽ trở thành gốc của cây con tiếp theo, sao cho chỉ phải cắt bỏ số lượng ít nhất các đa giác khác, i.e. ngăn cây BSP lớn hơn đáng kể danh sách đưa vào

        >**NOTE**. Thật ra, chỉ cần chọn đa giác tốt nhất trong 1 số các đa giác ngẫu nhiên
* *Ưu điểm*. Tốt khi mô hình ít thay đổi, chỉ có điểm nhìn bị đổi

### Chính xác theo ảnh
**Thuật toán Warnock**. Cố gắng tìm những cửa sổ có cùng màu sắc / cường độ trên màn hình, i.e. khu vực liên kết
* *Ý tưởng*. Thực hiện các thử nghiệm sau trên đa giác bất kì $P$
    * $P$ có tách biệt với cửa sổ không
    * $P$ có bao cửa sổ không
    * $P$ có giao một phần với cửa sổ không
    * $P$ có nằm trong cửa sổ không
    * $P$ có nằm trước các đa giác khác không ?
* *Phương pháp*
    1. Khởi tạo danh sách cửa sổ $L$, toàn bộ cửa sổ màn hình
    2. Với mỗi $W\in L$, tìm cửa sổ thỏa mãn
        * Tất cả đa giác tách biệt với $W$, i.e. vẽ $W$ với màu nền
        * Chỉ một đa giác $P$ giao với $W$, i.e. vẽ $P \cap W$ với màu $P$ và phần còn lại của $W$ với màu nền
        * Tìm được một đa giác bao quanh $W$ và nằm trước các đa giác giao với $W$, i.e. tô $W$ với màu của đa giác
    3. Với các $W$ khác
        * Ta chia $W thành 4 cửa sổ  con đều nhau và đưa vào $L$
        * Lặp lại quá trình xử lý tới khi ta hạ kích thước cửa sổ xuống thành 1 điểm 
* *Các phép thử*
    * *Kiểm tra cứa sổ tách biệt với đa giác*. Sử dụng hộp bao
    * *Kiểm tra cửa sổ nằm trong đa giác*. Thay tọa độ đỉnh của cửa sổ vào công thức cạnh đa giác
    * *Kiểm tra cứa sổ giao đa giác*. Cạnh của đa giác giao với cạnh cửa sổ
    * *Kiểm tra đa giác nằm trong cửa sổ*
    * *Kiểm tra $P$ nằm trước các đa giác khác trong cửa sổ*

>**NOTE**. Các cửa sổ không nhất thiết là hình chữ nhật

**Thuật toán Weiler-Atherton**. Sử dụng cửa sổ con để tạo sự cân xứng cho hình dạng của đa giác

**Thuật toán bộ đệm Z**. Ghi lại thông tin về độ sâu hiện thời của mỗi điểm
* *Ý tưởng*. 
    * Lưu thông tin về độ sâu hiện thời của mỗi điểm
    * Nội suy z trong quá trình tính toán
    * Lưu trữ một ma trận độ sâu tương ứng với ảnh đầu ra
    * Mỗi khi xử lý 1 đa giác, so sánh với các giá trị z đang lưu trữ
    * Lưu lại giá trị màu của những điểm gần nhất
* *Bộ đệm Z*. Mảng 2 chiều chứa độ sâu hiện tại
    1. Khởi tạo bộ đệm ảnh với màu nền
    2. Khởi tạo bộ đệm Z với z = max của mặt phẳng clipping
    3. Cần tính z cho mỗi điểm bằng cách nội suy từ đỉnh đa giác
    4. Cập nhật cả bộ đệm ảnh và bộ đệm Z
* *Kết hợp với thuật toán dòng quét*. Giảm bộ nhớ cần lưu trữ, i.e. $H\times W$ so với $W$
    * *Đoạn và nhịp*. Nhịp là nơi một đoạn giao cắt với dòng quét
    * *Câu hỏi*. Đoạn nào là đoạn hiện?
    * *Ý tưởng*
        1. Chia đường quét thành các nhịp
        2. Trong mỗi nhịp, xác định đoạn có thể nhìn được bằng cách kiểm tra độ sâu của chúng theo công thức mặt phẳng
    * *Vấn đề*. Chọn nhịp sao cho tốt nhất

**Thuật toán dòng quét Watkins**. Một thuật toán dòng quét trong không gian ảnh đặc biệt hiệu quả
* *Ý tưởng*. Để đầu mút phải của nhịp hiện tại biến đổi và cố định đầu mút trái
* *Các bước*.
    1. Bắt đầu với đầu mút phải xa nhất
    2. Lấy ra các đoạn mới từ danh sách đã sắp xếp theo $x$
    3. Điều chỉnh dần đầu mút phải về bên trái đến khi thu được một nhịp đơn giản, đủ để tính được đoạn nào là đoạn hiệ
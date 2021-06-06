---
title: Hanh's talk
tags: Mathematics
---

<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
* [Question](#question)
* [Toán học trong ML](#toán-học-trong-ml)
<!-- /TOC -->

#### Question
**1.** Proofs or intuitions? How to practice both skills?

**2.** If we just focus on intuition, how can we prove something, e.g. our intuition?

**3.** How long should one stick around a problem related to proof and intuition? What to do next when we stop sticking around, i.e. ask for solution or leave things there for later considerations?
* *Examples*. Prof. Truyen Tran said that the maximum time for sticking around a problem is 1 day, then just leave things there and we can come back connecting the dots after being mature enough about the field

**4.** Quora users suggested that the best way to learn mathematics is to practice as much as we can. What is the purpose of practicing in the sense of improving proofs and intuitions?

**5.** When facing a mathematical problem, e.g. prove an inequality or a theorem, how can we survey for ideas or solutions, i.e. GG cannot understand latex words
* *Examples*. Prof. Truyen Tran (from A2I2 lab, Deakin university) said that he used to have a look at all inequalities listed by Wikipedia to search for an appropriate one, which fits his needs

**6.** The best way to start learning something?

**7.** The best way to read a mathematical text book, or book? To deeply understand everything with intuitions and proofs, or just to get to know things?
* *Examples*.
    * Dr. Long Q. Tran said that we just have to get to know the concepts and methods, without remembering them in details. Because once we know they exists, we can search for them with GG
    * Prof. Truyen Tran said that something is not important that we should understand

**8.** What is the objective when doing research? To come up with a new thing or to learn something?
* *Examples*. Prof. Truyen Tran said that the being researcher is to maximize what we can learn per time unit

**9.** What should be done first? To find a problem of interest or to build a solid background, i.e. overview

# Toán học trong ML
**Motivation**
* ML for manifold
    * When controlling robot hands, i.e. control degrees of freedom
* *Idea*. Input an MRI image, output the probability of cancer
    * *Problem*. Understand the mechanism of MRI, i.e. we cannot do ML upon something we do not understand
* *Question 1*. What is MRI
    * Inject điện từ into body and capture the điện từ phát ra từ bệnh nhân
* *Solving a problem principle*.
    1. Learn about the aspects of the problems, i.e.
        * Learn about how an MRI image is constructed
            * MRI relates to DRUM problem, i.e.
                * MRI.
                * DRUM.
                    * Cơ bản.
                        * Mô tả.
                            * Khi gảy 1 dây đàn thì phát âm thanh ở dạng sóng âm (sau khi phân tích phổ bằng Fourier)
                            * Bài toán. từ các sợi dậy khác nhau, khôi phục lại bản nhạc (inverse Fourier)
                            * Câu hỏi. Chiều dài dây đàn là bao nhiêu
                        * Input. Sóng âm tạo ra bởi sợi dây đàn
                        * Output. Chiều dài sợi dây đàn
                    * Nâng cao. Lấy búa gõ vào 1 sợi dây thép được căng ra phủ da trâu >>> ra sóng âm
                        * Câu hỏi. Từ âm thanh tạo ra, ta khôi phục được hình dáng hình dáng sợi thép hay không?
                    * Tổng quát. Cho âm thanh tạo ra, ta có thể tạo ra hình dáng của nguồn phát âm được hay không?
                    * Mở rộng. Cho não người, dùng 1 trường điện từ cực lớn E tác động vào não sau đó ngắt trường điện từ lại, từ đó tạo ra dao động trong não (sóng điện từ)
                        * Bài toán. Xây dựng hình ảnh não người từ sóng điện từ thu được
                        * Phát hiện bệnh. Dựa vào 1 tần số điện từ đặc biệt để chẩn đoán bệnh
                            * Example. Nếu trống bị mọt thì sẽ tạo ra âm thanh khác hẳn
                * Đẳng cấu. 2 bài toán y hệt nhau về bản chất
                    * Bước 1. Phát triển mô hình toán cho toy models
                    * Bước 2. Bê mô hình toy sang bài toán cụ thể & mô tả bằng ngôn từ trong lĩnh vực khác
                * Cách convert problem cơ bản sang problem nâng cao khác.
                    * Bước 1. Nghĩ xem lambda_1, lambda_2, etc. là gì (eigenvalue của Laplacian)
                    * Bước 2. Đặt câu hỏi: 2 cái trống khác nhau có đưa đến cùng 1 âm thanh hay không, i.e. cho 1 âm thanh có thể tìm lại được cái trống hay không?
                        * Nếu từ 1 âm thanh đưa ra được n (n >= 2) cái trống thì problem thất bại, tuy nhiên
                            * Ta suy ra n cái trống đó sẽ sinh ra cùng 1 âm thanh
                            * Kết hợp các phương pháp khác ta sẽ suy ra trống nào là trống tạo âm thanh
                        * Thí nghiệm. Cho 2 chiếc trống với hình dạng khác nhau được chọn trước, 2 chiếc trống này tạo ra cùng 1 âm thanh
                            * Suy luận 1.
                                * Nếu chỉ nghe âm thanh thì ko biết trống loại nào
                                * Nếu ta có 2 ảnh MRI thì người có u chỗ này, người có u chỗ kia, i.e. không phân biệt được u của 2 chỗ
                            * Suy luận 2.
                                * Từ âm thanh suy ra thể tích, chu vi của cái trống, etc. (not hình dáng)
                                * Mục đích của MRI là từ MRI khôi phục được hình dạng não người
                            * Suy luận 3.
                                * 2 cái trống dù ko phân biệt được nhưng ko phân biệt được tới mức độ nào
                                * Từ MRI ra vị trí khối u bị sai >>> Ta cần đi từ não ra MRI
                            * Suy luận 4. Làm AI trên MRI >>> toang
                        * Kết luận. Cần phát triển công cụ mới
* *Cách tiếp cận bài toán cái trống*.
    1. Từ lambda_i (eigenvalue) suy ra Delta f (Laplace operator), i.e. Delta f = lambda_i f
        * Mặt phẳng ~> vector space  ~> inner product space ~> normed space ~> metric space ~> topology (i.e. open sets - gần nhau)
            * "Gần nhau". Trong 1 số trường hợp, ta không thể define 1 metric cho 1 topological space, do vậy ta dựa vào open set

                ~> Gần nhau là như nào?
            * Timf hiểu về hội tụ (topology)
        * Mặt phẳng ~> metric space dx ~> độ dài dx^2 + dy^2 (Riemann geometry)
        * Mặt phẳng ~> area (measurable space)
        * Mặt phẳng bị đục 1 lỗ (incomplete space) ~> Không còn là mặt phẳng nữa
        * Mặt phẳng bị bẻ cong (Riemann geometry)
            * Thể nào là mặt phẳng cong or độ cong? Mặt phẳng có đồng chất hay ko?

                ~> Phát triển công cụ toán học để định nghĩa sự cong
    * Riemann geometry ~> Cấu trúc khoảng cách đặt trên 1 đường hoặc 1 mặt nào đó
    * Manifold ~> 1 cấu trúc đc đặt lên trên 1 đường hoặc 1 mặt nào đó

---

**Tích chập**. $f$ chập $g$ tại $x$ là ... (định nghĩa Wiki)
* *Intuition*. Xe lăn đường, i.e. 1 cái xe đi đường Trường Chinh sẽ bị xóc nếu bánh xe của nó quá bé, bánh càng bé càng xóc, i.e. nó bị rơi vào ổ gà

    ~> Tích chập = tịnh tiến + weighted sum
* *Convolution (Đập đường)*. Khi bánh xe lăn qua thì đất đá bị cán ra, rải ra
    * Gaussian kernel, i.e. bánh lăn đường sẽ tạo áp lực lớn nhất lên điểm hiện tại, càng xa bánh lăn áp lực càng giảm
* *Khái niệm*. $f$ chập $g$ là ta trừ đi 1 điểm, i.e. $f(x-y)$, thì trọng số tương ứng sẽ là $g(y)$

    ~> Convolution = trung bình có trọng số của các phép tịnh tiến
* *Lọc (xử lý ảnh)*. Xử lý ảnh = có 1 hàm $f$ (ảnh) được xử lý = 1 hàm $g$
    * *Thực tiễn*. $f*g$ là tịnh tiến $f$ 1 đoạn (trái phải trên dưới) và chia trung bình

        >**NOTE**. Thời xưa, nta tính tay phép nhân mệt nên nta nghĩ đến phép + trên miền log

        >**NOTE**. Tư duy đơn giản hóa tính toán này rất oke

    * *Fourier*. Biến đổi convolution thành phép nhân
        * Bước 1. Biến đổi ảnh từ miền space sang miền frequency
        * Bước 2. Tính product của Fourier transforms
        * Bước 3. Biến miền frequency thành lại miền space
    * Suy luận 1. Mọi mạng neuron thông thường = 1 mạng neuron tích chập (qua Fourier transform)
        * Mạng convnet rất phù hợp & nhạy cảm với tịnh tiến trên các miền liên tục (dựa vào phép tịnh tiến, qua Fourier transform, )
        * Mạng neuron thường phù hợp & nhạy cảm với giá trị

---

**Câu hỏi**. Làm sao đọc MRI xong biết đường mà đọc về DRUM
* Bước 1. Đọc xem MRI là gì
* Bước 2. Tưởng tượng đến cái trống
* Bước 3. Đơn giản hóa bài toán nữa, i.e. constraint the problem more and more, đến khi ta biết lời giải hoặc biết GG lời giải

**Idea**. Không bao giờ giải bài toán trực tiếp, i.e. tìm kim trong phòng sáng thành thạo trước rồi mới tìm kim trong phòng tối
* Lý giải. Tìm kim trong phòng sáng ko được thì tìm sao được kim trong phòng tối

**Đạo hàm**. Bâc 1 ~ vận tốc, Bậc 2 ~ gia tốc

**Vector space**. Bất cứ tập objects có thể định nghĩa phép cộng và phép nhân vô hướng
* VD.
    * Mặt phẳng, ko gian 3 chiều, 1D
    * Computer science example. 1 mảng int hoặc float 2 chiều
* Xử lý data.
    * Copy & paste dữ liệu từ DB ra ngoài (copy paste như nào thì tùy ý)
    * Xử lý data ~> Phải sử dụng ĐSTT, i.e. map từ input ra output (map như nào tùy ý)
* Ánh xạ. Cho $f: R^n \to R^m$ ~> Có bao nhiêu kiểu hàm f, i.e. null (hoặc kernel) (vứt đi) and range
    * Định lý cơ bản 1 của ĐSTT. Từ 1 tập vector và 1 ánh xạ, ta phải định nghĩa được null space và range
    * Ánh xạ f từ R^n vào chính nó, e.g. dùng 1 ánh xạ tác động vào 1 ảnh để cho ra 1 ảnh
        * Có 1 đường tròn, ta kéo dãn đường tròn theo các phương khác nhau
        * Vậy mọi ánh xạ tuyến tính nên được biểu diễn ở dạng kéo dãn các chiều khác nhau, i.e. SVD

            >**NOTE**. Trong hầu hết trường hợp, mỗi eigenvalue ~ 1 eigenvector

        * Nếu ta biết eigenvectors của 1 linear operator f thì ta sẽ chuyển basis của ta về eigenvectors >>> khi áp dụng linear operator ta chỉ đơn giản kéo dãn các eigenvectors này sau đó sum up lại là xong
* Tổng quát hóa bài toán chéo hóa ma trận
    * Ta coi 1 số hàm $f$ giống như 1 ma trận $A$, khi đó trị riêng (ma trận) ~> giá trị riêng (hàm số) của $f$
        * Cách hiểu mới hơn "thế nào là trị riêng của 1 ma trận". Giống với trị riêng của 1 hàm f (theo a Hạnh nghĩ thế), i.e. trị riêng ~ giá trị của hàm số theo 1 phương nào đó
        * Không gian riêng (matrix) ~> vùng (func)
    * Câu hỏi. Tại sao trị riêng của func là tập giá trị của func?
        * Hàm số. Môn cơ lượng tử coi 1 hàm là 1 ma trận vô hạn chiều
        * Trị riêng của 1 ma trận là giá trị của 1 hàm số, i.e. với mỗi giá trị x thì f(x) là 1 ma trận và ta có
            * f(x).v = lambda.v thì lambda là trị riêng của f(x). Tức f(x) = lambda
            * Nếu f(x) có nhiều trị riêng thì f(x) = (lambda1, lambda2, ...)
        * Cách nhìn này là 1 cách nhìn cụ thể của function, ko phải tổng quát
     * Câu hỏi. Ma trận là tổng quát hóa của 1 hàm theo 1 nghĩa nào đó
        * Khi tôi đập trống, tôi nghe được lambda1, ..., lambdan ~> Ta cho 1 hàm f và xác định tập giá trị riêng của hàm f
        * Nghịch lý. f*g = f*g nhưng A*B \neq B*A ~> Cái quái gì vậy?
            * Solution. Coi matrix là suy rộng của function (quantumn mechanic)

**Metric space**. Quá trừu tượng, không ai làm việc trực tiếp trên đó vì ko có tính ứng dụng
* Cần định nghĩa metric, e.g. đường chim bay, đường bộ, đường thủy, etc.
* Đường thẳng. là 1 đường cong bất kì nối giữa 2 điểm và có khoảng cách bé nhất
    * VD. Đường đi ngắn nhất từ nhà đến trường
* Câu hỏi. Khoảng cách có thể thay đổi theo thời gian ko? Có

    ~> Conditional metric space
* Vấn đền. Ta cho 1 sequence các metrics khác nhau thì các sequence này sẽ hội tụ như thế nào?

**Proof**.
* Proof giống như 1 file exe còn intuition là source code, i.e. khó dịch ngược, dễ dịch xuôi
* Proof là bản release còn intuition là bản dev
* Khi có intuition kiểu gì cũng ra proof

**Có những thứ phải làm tay 1 lần trong đời nó mới dễ**

**Toán học**
* Tu luyện các công cụ phức tạp hoa lá có sẵn >>> Chuyên gia
* Nhìn vấn đề cũ bằng cách nhìn mới >>> Thiên tài

**Cơ học lượng tử**. Cho 1 vật bé vô cùng, ta ko đo được vị trí và xung lượng của vật đó

Không bao giờ có tiêu chuẩn chung cho cả 1 ngành, nếu ta nhìn 1 vấn đề theo 1 cách khác và đưa ra 1 solution tốt hơn hẳn thì sẽ là chuyên gia top

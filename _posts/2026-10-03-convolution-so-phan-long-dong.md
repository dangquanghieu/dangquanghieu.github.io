---
layout: post
title: "Convolution - Số phận long đong của một thuật ngữ"
date: 2026-10-03
math: true
---

Lĩnh vực Tín hiệu và hệ thống / Xử lý tín hiệu có một thuật ngữ quan trọng: "convolution". Dịch trực tiếp từ này qua tiếng Việt
sẽ là "chập". Thuật ngữ này được dùng cho phép toán cơ bản nhất trong một hệ thống LTI, phép chập.

Trong trường hợp rời rạc, công thức của phép toán này như sau

$$
\begin{equation}\label{eq:dt_conv}
x[n] * h[n]: = \sum_{k=\infty}^\infty x[k]h[n-k]
\end{equation}
$$

Trong trường hợp liên tục, công thức sẽ thay đổi đi một chút

$$
\begin{equation}\label{eq:ct_conv}
x(t) * h(t): = \int_{\tau=\infty}^\infty x(\tau)h(t-\tau) d\tau
\end{equation}
$$

Ta thấy hai công thức trên về bản chất là một, nên người ta vẫn dùng chung dấu * để biểu diễn, khi đó sẽ gọi chung là "phép chập", hoặc đơn giản hơn: "chập". Chẳng hạn, ta có thể nói $x(t)$ chập với $h(t)$. 

Hai công thức trên vẫn có khác biệt, một trường hợp tính tổng, trường hợp kia tính tích phân. 
Do vậy, khi cần phân biệt rõ ràng, người ta sẽ gọi phép toán trong
$\eqref{eq:dt_conv}$ là *tổng chập*, còn phép toán trong $\eqref{eq:ct_conv}$ là *tích phân chập*.

Tuy nhiên, thuật ngữ này từng có một tên gọi khác, và có lẽ hiện giờ vẫn được dùng phổ biến. Đó là từ *tích chập*. Nó xuất hiện trong những cuốn sách đầu tiên về Xử lý tín hiệu số của khoa Điện tử - Viễn thông, ĐHBK HN vào giữa những năm 1990, trong đó tiêu biểu là cuốn "Xử lý số tín hiệu" của thầy Nguyễn Quốc Trung.  Thủa đó, BK (và các trường đại học VN) đều chưa có môn Tín hiệu và hệ thống. Do vậy, môn XLTH sẽ đảm nhiệm luôn phần THHT rời rạc. Khi đó "convolution" được dịch là "tích chập". Phải nói luôn là dịch như này không sai, thuật ngữ này trong tiếng Pháp là *produit de convolution* (thầy Trung là "dân" tiếng Pháp), ngay cả một số ít tài liệu tiếng Anh vẫn dùng từ *convolution product*. Tuy nhiên, gần như tuyệt đại đa số những tài liệu về Tín hiệu và hệ thống, cũng như về Xử lý tín hiệu số trên thế giới (bằng tiếng Anh) thì lại không sử dụng từ này, chỉ đơn thuần là *convolution*. 

Nếu chỉ sử dụng từ *tích chập* riêng cho trường hợp rời rạc thì hoàn toàn ổn, nhưng khi bắt đầu giảng dạy môn Tín hiệu và hệ thống, khi cần phân biệt, so sánh với trường hợp liên tục thì gặp vấn đề. Nếu giữ nguyên *tích chập* thì ta không thể gọi phép toán cho trường hợp rời rạc là *tổng tích chập*, cho trường hợp liên tục là *tích phân tích chập* được. Đơn giản là rất ngang tai :)

Vậy nên, mặc dù là học trò của thầy Trung, tôi đã *tự tiện* dùng các từ *chập, phép chập, tổng chập, tích phân chập* khi giảng dạy môn THHT, kể cả môn XLTH nữa. Bản thân đồ án tốt nghiệp đại học của tôi (năm 1999, dưới sự hướng dẫn của thầy Trung) cũng là về *mã chập* (convolutional codes), ngay hồi đó đã không dùng từ *mã tích chập* nhé (bởi vì cũng rất ngang tai!)

Chưa hết. Tiếp tục số phận long đong của thuật ngữ này. Vào thủa AI / Deep Learning bắt đầu nổi lên (giữa những năm 2010), một (vài) cựu sinh viên ĐT-VT đã nhanh chóng tiếp nhận kiến thức mới, dịch sang tiếng Việt và chia sẻ với cộng đồng khoa học VN. Cụm từ "CNN" được dịch thành "mạng nơ-ron tích chập", và cho đến nay vẫn được sử dụng rộng rãi. Không vấn đề gì hết!

Tuy nhiên, bản thân từ "convolution" dùng trong CNN lại không chính xác. Cộng đồng khoa học trên thế giới, và cả thầy Andrew Ng. trong khóa học Machine Learning nổi tiếng cũng đã thừa nhận rằng dùng thuật ngữ "convolution" ở đây là sai. Từ đúng phải là "correlation" - *phép tương quan*. 

$$
\begin{equation}\label{eq:corr}
x_1[n] * x_2[n]: = \sum_{m=\infty}^\infty x_1[m]x_2[m-n]
\end{equation}
$$

Mới nhìn thì thấy $\eqref{eq:corr}$ rất giống với $\eqref{eq:dt_conv}$. Khác biệt ở đây là ở biến số của số hạng cuối cùng. Phép chập cần phải thực hiện lấy đối xứng, sau đó mới dịch, nhân, cộng. Trong khi đó, phép tương quan không có phần lấy đối xứng, mà thực hiện dich, nhân, cộng luôn. Trong một số trường hợp đặc biệt, khi bản thân $x_2[n]$ đã đối xứng, thì phép tương quan có kết quả giống như phép chập; nhưng vẫn không thể sử dụng các tính chất như giao hoán, kết hợp. 

Tóm lại, dùng "convolution" thay cho "correlation" ở đây là không chính xác về mặt khoa học. Người ta có thể sử dụng theo thói quen nhưng cần phân biệt rõ, tránh sai sót khi nghiên cứu chuyên sâu về CNN / Deep Learning. 

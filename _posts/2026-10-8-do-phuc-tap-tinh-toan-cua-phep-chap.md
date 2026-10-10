---
layout: post
title: "Độ phức tạp tính toán của phép chập"
date: 2026-10-08
math: true
---

Xét hệ thống LTI rời rạc với đầu vào $x[n]$, đáp ứng xung $h[n]$ có chiều dài lần lượt là $L$ và $P$. 
Khi đó đầu ra $y[n]$ được tính bằng phép chập (còn gọi là tổng chập) như sau

$$
\begin{equation}\label{eq:dt_conv}
y[n] = \sum_{k=\infty}^\infty x[k]h[n-k]
\end{equation}
$$

Đây là phép toán cơ bản nhất trong *Tín hiệu và hệ thống*, và trong *Xử lý tín hiệu số*. 
Câu hỏi đặt ra là phép chập này có độ phức tạp tính toán như thế nào? Cụ thể hơn là nếu tính trực tiếp 
theo công thức $\eqref{eq:dt_conv}$ thì cần bao nhiêu phép nhân, bao nhiêu phép cộng? 

Có nhiều cách. Ta có thể đếm số phép nhân và phép cộng cho từng giá trị của $y[n]$, 
rồi cộng tất cả lại. 

Tuy nhiên, ta có thể tính nhanh hơn khi quan sát toàn bộ quá trình tính toán theo định nghĩa. 
Hai dãy xếp hàng cạnh nhau (một dãy đầu vào, và dãy đáp ứng xung sau khi lấy đối xứng). 
Một dãy đứng im, dãy kia dịch chuyển lần lượt từng phần tử một. Mỗi lần dịch chuyển, các cặp đối diện nhau 
sẽ nhân với nhau, sau đó cộng kết quả lại. *Lưu ý*: trong toàn bộ quá trình, mỗi phần tử của dãy này
sẽ chỉ đối diện (gặp) mỗi phần tử của dãy kia đúng một lần duy nhất.

Như vậy, số lần gặp nhau được tính bằng chiều dài của dãy này nhân với chiều dài của dãy kia. Nói cách khác, 
tổng số phép nhân sẽ là $LP$.

Với cùng cách tiếp cận, chúng ta cũng có thể tính được tổng số phép cộng. Dưới đây là code Python để tính phép chập.

```python
import numpy as np

x = np.array([3,-1,2,9,-4,5,7])
h = np.array([-2,0,-3,2,0,-4,2,-1])

L = len(x)
P = len(h)
y = np.zeros(L+P-1)

for i in range(L):
    for j in range(P):
        y[i+j] += x[i]*h[j]

print(y)
```

Ngược lại, từ đoạn code trên ta cũng dễ dàng tính được tổng số phép nhân, và tổng số phép cộng 
(sau khi bỏ đi những lần cộng với không). Một bài toán nho nhỏ, nhưng chỉ cần một chút quan sát vào bản chất, một chút đánh giá ở một góc nhìn khác, chúng ta đã có thể có được lời giải - ít công thức nhất, ít dòng lệnh nhất, đơn giản nhất và ... đẹp nhất! 

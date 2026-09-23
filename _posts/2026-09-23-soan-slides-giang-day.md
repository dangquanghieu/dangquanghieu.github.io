---
layout: post
title: "Soạn slides giảng dạy"
date: 2026-09-23
---

Kỳ này tôi soạn lại slides giảng dạy cho môn Xử lý tín hiệu số. 
Lý do rất đơn giản: slides cũ đã ... quá cũ, hơn 10 năm trước. 
Dùng Latex / Beamer, kết hợp với pstricks cho các loại hình vẽ. 
Nói chung khá là mất công, vậy nên mới lười update :D

Mỗi tuần làm lại một chương. Hôm nay làm tới chương FFT và ứng dụng.
Có phần phân tích phổ tín hiệu thời gian thực. Ngày trước, tất cả chỉ có đúng 1 slide tóm tắt.
Còn lại là demo và chém gió trên Matlab. Bây giờ đưa vào diễn giải tuần tự, từ tốn, từng phần một.
Hì hụi cả buổi, soạn ra 10 slides rồi mà vẫn chưa xong. Vẫn còn chừng 5-7 slides nữa. 
Nếu lười biếng chỉ dùng text, equation, thỉnh thoảng thêm hình vẽ Matlab thì mất chừng một buổi nữa.
Còn nếu kì công vẽ hình minh họa, pstricks các kiểu thì không biết tới khi nào ...

Ví dụ nhé, dưới đây là đoạn code pstricks để vẽ lưu đồ tín hiệu cho thuật toán FFT.

```
\begin{pspicture}(0,-6.5)(10,0)
	\psset{xunit=1,yunit=1}
	\scriptsize
	\multido{\rA=0+-1,\nN=0+1}{8}{\psdot(0,\rA)\psline(0,\rA)(10,\rA) \psdot(1,\rA) \psdot(3,\rA) \psdot(4,\rA) \psdot(6,\rA) \psdot(7,\rA) \psdot(10,\rA) \uput[0](10,\rA){$X(\nN)$}}
	\uput[180](0,0){$x(0)$} \uput[180](0,-1){$x(4)$} \uput[180](0,-2){$x(2)$} \uput[180](0,-3){$x(6)$}
	\uput[180](0,-4){$x(1)$} \uput[180](0,-5){$x(5)$} \uput[180](0,-6){$x(3)$} \uput[180](0,-7){$x(7)$}

	\multido{\rA=0+-1,\rB=-4+-1}{4}{\psline(7,\rA)(10,\rB) }
	\multido{\rA=-4+-1,\rB=0+-1,\rC=-0.3+-1,\nN=0+1}{4}{\psline(7,\rA)(10,\rB) \psline{->}(7,\rA)(9.75,\rA) \uput[-90](9.75,\rA){$-1$} \psline{->}(6,\rA)(6.5,\rA) \uput[90](6.5,\rA){$W_N^{\nN}$} }

	\psline(4,0)(6,-2) \psline(4,-1)(6,-3) \psline(4,-2)(6,0) \psline(4,-3)(6,-1) 
	\psline{->}(4,-2)(5.75,-2) \uput[-90](5.75,-2){$-1$} \psline{->}(4,-3)(5.75,-3) \uput[-90](5.75,-3){$-1$} 
	\psline{->}(3,-2)(3.5,-2) \uput[90](3.5,-2){$W_N^0$} \psline{->}(3,-3)(3.5,-3) \uput[90](3.5,-3){$W_N^2$}  

	\psline(4,-4)(6,-6) \psline(4,-5)(6,-7) \psline(4,-6)(6,-4) \psline(4,-7)(6,-5)
	\psline{->}(4,-6)(5.75,-6) \uput[-90](5.75,-6){$-1$} \psline{->}(4,-7)(5.75,-7) \uput[-90](5.75,-7){$-1$}
	\psline{->}(3,-6)(3.5,-6) \uput[90](3.5,-6){$W_N^0$} \psline{->}(3,-7)(3.5,-7) \uput[90](3.5,-7){$W_N^2$}  

	\multido{\rA=0+-2,\rB=-1+-2}{4}{\psline(1,\rA)(3,\rB)}	
	\multido{\rA=-1+-2,\rB=0+-2}{4}{\psline(1,\rA)(3,\rB) \psline{->}(1,\rA)(2,\rA)\uput[-90](2,\rA){$-1$} \psline{->}(0,\rA)(0.5,\rA)\uput[90](0.5,\rA){$W_N^0$} }	
\end{pspicture}
```

Anyway, việc cần làm nên vẫn cứ phải làm thôi. Hy vọng sau đó tôi có thể tái sử dụng chúng 
cho nhiều năm sau (mà không thấy xấu hổ). Hy vọng sinh viên có thể theo học được, các đồng nghiệp
có thể tham khảo.

À mà đám slides này vẫn được soạn thảo 100% "bằng tay". Không biết AI có thể hỗ trợ được tới đâu nhể? 

P.S: [Link bài giảng](https://www.dropbox.com/scl/fo/y7jkblp6xa8zcyq6nntzh/AN-HDuQl4-esSACCzj6WHC8?rlkey=qkfpolduoiscqb68i542yc2rs&dl=0).
Những files này chắc đang hỗn độn giữa cũ và mới. Khi nào xong thì tôi sẽ dọn dẹp một thể. 

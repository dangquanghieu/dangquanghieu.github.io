"""Favicon nhiều hàm sinc, nền #1D5C63. Mỗi biến thể: danh sách (tâm, biên độ) theo đơn vị T_s,
tùy chọn vẽ đường tổng (tín hiệu khôi phục) nét đậm."""
import numpy as np
from render_mpl import render
YB=0.68
V={ # tên: (các (tâm, biên độ), nửa khoảng hiển thị, vẽ tổng?)
 'B1_lech':   ([(-1,0.55),(0,1.0),(1,0.75)], 2.6, False),          # 3 sinc, biên độ không đối xứng
 'B2_bon':    ([(-1.5,0.55),(-0.5,1.0),(0.5,0.85),(1.5,0.45)], 3.0, False),  # 4 sinc, không có búp "giữa"
 'B3_rong':   ([(-1,0.85),(0,1.0),(1,0.85)], 2.0, False),          # 3 sinc gần bằng nhau, búp rộng
 'B4_tong':   ([(-1,0.55),(0,1.0),(1,0.75)], 2.6, True),           # 3 sinc mờ + đường tổng đậm
}
def curves(name,small):
    cs,half,tong=V[name]; t=np.linspace(-half,half,900); xs=0.5+t/(2*half)*0.84
    scale=0.50/max(a for _,a in cs) if not tong else 0.42
    out=[] if small else [([(0.08,YB),(0.92,YB)],0.022,0.45)]
    if tong:
        if not small:
            for c,a in cs: out.append((list(zip(xs,YB-scale*a*np.sinc(t-c))),0.03,0.45))
        s=sum(a*np.sinc(t-c) for c,a in cs)
        out.append((list(zip(xs,YB-scale*s)),0.075 if small else 0.06,1.0))
        return out
    order=sorted(range(len(cs)),key=lambda i:cs[i][1])   # búp cao vẽ sau cùng
    for i in order:
        c,a=cs[i]; top=(a==max(x[1] for x in cs))
        out.append((list(zip(xs,YB-scale*a*np.sinc(t-c))),(0.07 if small else 0.045),1.0 if top else 0.7))
    return out
def png(name,size): return render(curves(name,size<=24),size)
def svg(name,R=0.20,bg='#1D5C63'):
    s=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">',f'<rect width="100" height="100" rx="{R*100:g}" fill="{bg}"/>']
    for p,w,a in curves(name,False):
        p=p[::8]+[p[-1]] if len(p)>50 else p
        d='M'+' L'.join(f'{x*100:.2f} {y*100:.2f}' for x,y in p)
        s.append(f'<path d="{d}" fill="none" stroke="#fff" stroke-opacity="{a:g}" stroke-width="{w*100:g}" stroke-linecap="round" stroke-linejoin="round"/>')
    s.append('</svg>'); return '\n'.join(s)

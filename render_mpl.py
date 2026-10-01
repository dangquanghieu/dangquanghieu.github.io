"""Vẽ favicon bằng matplotlib (nét khử răng cưa đúng, không bị hạt ở chỗ nối)."""
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from PIL import Image; import io
def render(curves,size,bg='#1D5C63',R=0.20,ss=8):
    S=size*ss; dpi=100; fig=plt.figure(figsize=(S/dpi,S/dpi),dpi=dpi); ax=fig.add_axes([0,0,1,1])
    ax.set_xlim(0,1); ax.set_ylim(1,0); ax.set_axis_off(); fig.patch.set_alpha(0)
    ax.add_patch(FancyBboxPatch((R,R),1-2*R,1-2*R,boxstyle=f'round,pad={R}',fc=bg,ec='none'))
    for p,w,a in curves:
        p=np.asarray(p); ax.plot(p[:,0],p[:,1],color='white',alpha=a,lw=w*S*72/dpi,solid_capstyle='round',solid_joinstyle='round')
    buf=io.BytesIO(); fig.savefig(buf,format='png',dpi=dpi,transparent=True); plt.close(fig)
    return Image.open(buf).convert('RGBA').resize((size,size),Image.LANCZOS)

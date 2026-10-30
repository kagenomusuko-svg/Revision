import numpy as np

def pf_right(W):
    vals, vecs=np.linalg.eig(W)
    k=np.argmax(np.abs(vals))
    v=np.real(vecs[:,k]); v*=np.sign(v.sum()); v=np.abs(v); return v/v.sum(), vals[k]

# MC-01
W1=np.full((2,2),.5); R=np.array([.5,.5]); alpha=np.array([.8,.8]); Delta=R-alpha
assert np.all(W1>0) and np.allclose(W1.sum(axis=1),1) and np.all(Delta<0)
# MC-02
W2=np.array([[.4,.3,.3],[.2,.5,.3],[0,0,0.]])
assert np.allclose(W2.sum(axis=1),[1,1,0]) and not np.allclose(W2@np.ones(3),np.ones(3))
# MC-03
W3=np.array([[.9,.1],[.4,.6]])
rw,_=pf_right(W3); rwt,_=pf_right(W3.T)
assert np.allclose(rw,[.5,.5]) and np.allclose(rwt,[.8,.2])
# MC-04
W4=np.array([[9.,1.],[20.,80.]])
r_raw,_=pf_right(W4); W4n=W4/W4.sum(axis=1,keepdims=True); r_norm,_=pf_right(W4n)
assert not np.allclose(r_raw,r_norm)
# MC-05
p=np.array([.30,.25,.15,.15,.15]); W5=np.tile(p,(5,1)); v,_=pf_right(W5.T)
W5e=W5.copy(); W5e[1]=np.mean(np.delete(W5,1,axis=0),axis=0); ve,_=pf_right(W5e.T)
assert np.allclose(W5,W5e) and np.allclose(v,ve) and v[1]>.0
# MC-06
p6=np.array([.19,.18,.30,.20,.13]); W6=np.tile(p6,(5,1)); v6,_=pf_right(W6.T)
assert np.isclose(p6.sum(),1) and v6[0]>v6[1] and v6[0]<.2
# MC-07 primitive W and no strict one-step TV contraction
W7=np.array([[0.,1.,0.],[.5,0.,.5],[.4,0.,.6]])
assert np.linalg.matrix_power(W7,5).min()>0
def T(v,W):
    z=W@v; return z/np.linalg.norm(z,1)
e1=np.array([1.,0,0]); e2=np.array([0.,1,0])
tv=lambda a,b: np.abs(a-b).sum()/2
assert np.isclose(tv(e1,e2),1) and np.isclose(tv(T(e1,W7),T(e2,W7)),1)
# MC-08 psi range contradiction
psi=lambda x:.21*x**(-.55)
assert psi(.05)>1 and psi(.01)>1
print('MC-01..MC-08: PASS; estos PASS verifican los contraejemplos/cálculos, no la teoría causal.')
print('W vs W.T:',rw,rwt,'; bruto vs normalizado:',r_raw,r_norm)
print('psi(.05), psi(.01):',psi(.05),psi(.01))

from scipy import optimize as opt
import numpy as np


x_0 = np.array([4,-2.5])

#NelderMead

def rosen(x):
    return 100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0

res = opt.minimize(rosen, x_0, method='nelder-mead', options={'xatol': 1e-8, 'disp': True})
print(res)

#CG

#Gradiant
def rosen_der(x):
    xm = x[1:-1]
    xm_m1 = x[:-2]
    xm_p1 = x[2:]
    der = np.zeros_like(x)
    der[1:-1] = 200*(xm-xm_m1**2) - 400*(xm_p1 - xm**2)*xm - 2*(1-xm)
    der[0] = -400*x[0]*(x[1]-x[0]**2) - 2*(1-x[0])
    der[-1] = 200*(x[-1]-x[-2]**2)
    return der

#Hessian
def rosen_hess(x):
    x = np.asarray(x)
    H = np.diag(-400*x[:-1],1) - np.diag(400*x[:-1],-1)
    diagonal = np.zeros_like(x)
    diagonal[0] = 1200*x[0]**2-400*x[1]+2
    diagonal[-1] = 200
    diagonal[1:-1] = 202 + 1200*x[1:-1]**2 - 400*x[2:]
    H = H + np.diag(diagonal)
    return H

res = opt.minimize(rosen, x_0, method='Newton-CG',jac=rosen_der, hess=rosen_hess,options={'xtol': 1e-8, 'disp': True})
print(res)

#BFGS
res = opt.minimize(rosen, x_0, method='BFGS', jac=rosen_der, options={'disp': True})
print(res)
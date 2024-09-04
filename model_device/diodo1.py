# File: model_device/diodo1.py 

import numpy as np 

class Diodo1:
    def __init__:(self, IS, RS, N, TT, CJO, VJ, M, EG, IKF, IR, NR, XTI, KF):
        self.IS = IS 
        self.RS = RS 
        self.N = N 
        self.TT = TT 
        self.CJO = CJO 
        self.VJ = VJ 
        self.M = M 
        self.EG = EG 
        self.IKF = IKF 
        self.IR = IR 
        self.NR = NR 
        self.XTI  = XTI 
        self.KF = KF 
        self.VT = 0.02585 

    # Ecuacion para calcular la corriente a traves del diodo 
    def calcular_

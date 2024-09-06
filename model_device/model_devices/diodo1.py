# Archivo: model_devices/diodo1.py

import numpy as np 

class Diodo1:
    def __init__(self, IS, RS, N, TT, CJO, VJ, M, EG, IKF, ISR, NR, XTI, KF):
        self.IS = IS 
        self.RS = RS 
        self.N = N 
        self.TT = TT 
        self.CJO = CJO 
        self.VJ = VJ 
        self.M = M 
        self.EG = EG 
        self.IKF = IKF 
        self.ISR = IRS 
        self.NR = NR
        self.XTI = XTI 
        self.KF = KF
        self.VT = 0.02585 

    # Ecuacion para calcular la corriente a traves del diodo 
    def calculate_current(self. Vd):
        # Componente exponencial principal (diodo ideal) 
        Id = self.IS * (np.exp((Vd - self.RS * 0) / (self.N * self.VT))-1 ) #Suponiendo que Id = 0 inicialmente 

        # Corriente de recombinacion 
        Irec = self.ISR * (np.exp(Vd /( self.NR * self.VT)) - 1)

        #Corriente total  (sin incluir efectos dinamicos de TT y CJO)
        Itotal = Id + Irec + (Vd/self.RS) 
        return Itotal 


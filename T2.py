#-------------------------------
#Паралельне програмування
#ПКС2СП на мові Python
#MA= min (D)*MX*MR – (D*C)*(MZ*MD)
#Лазарєв Матвій ІО-91
#12.12.21
#-------------------------------
import Operations

class T2:
    def __init__(self,mx, mz):
        self.mx=mx
        self.mz=mz
    def minimal(self, d1, d2, d3):
        min_d2=Operations.min_vector(d1)
        min_d=min(min_d2, d2, d3)
        return min_d
    def computation(self, mx, mr, min_d, mz, md, d,c):
        mq=Operations.multiplication_Matrix(mx,mr)
        me=Operations.scalar_multi_matrix(min_d,mq)
        mt=Operations.multiplication_Matrix(mz,md)
        dc=Operations.scalar_multi(d,c)
        my=Operations.scalar_multi_matrix(dc,mt)
        ma2=Operations.dif_matrix(me,my)
        return ma2
    def sum_ma(self, ma1, m2, m3):
        ma12=Operations.sum_matrix(ma1,m2)
        ma=Operations.sum_matrix(ma12,m3)
        return ma
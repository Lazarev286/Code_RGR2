#-------------------------------
#Паралельне програмування
#ПКС2СП на мові Python
#MA= min (D)*MX*MR – (D*C)*(MZ*MD)
#Лазарєв Матвій ІО-91
#12.12.21
#-------------------------------
import Operations
class T1:
    def __init__(self, c, md):
        self.c=c
        self.md=md
    def minimal(self, d):
        min_d1=Operations.min_vector(d)
        return min_d1
    def computation(self, mx, mr, min_d, mz, md, d,c):
        mq=Operations.multiplication_Matrix(mx,mr)
        me=Operations.scalar_multi_matrix(min_d,mq)
        mt=Operations.multiplication_Matrix(mz,md)
        dc=Operations.scalar_multi(d,c)
        my=Operations.scalar_multi_matrix(dc,mt)
        ma1=Operations.dif_matrix(me,my)
        return ma1
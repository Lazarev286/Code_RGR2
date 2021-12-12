#-------------------------------
#Паралельне програмування
#ПКС2СП на мові Python
#MA= min (D)*MX*MR – (D*C)*(MZ*MD)
#Лазарєв Матвій ІО-91
#12.12.21
#-------------------------------
import Operations
class T3:
    def minimal(self, d1, d2):
        min_d3 = Operations.min_vector(d1)
        min_d34=min(min_d3,d2)
        return min_d34
    def computation(self, mx, mr, min_d, mz, md, d,c):
        mq=Operations.multiplication_Matrix(mx,mr)
        me=Operations.scalar_multi_matrix(min_d,mq)
        mt=Operations.multiplication_Matrix(mz,md)
        dc=Operations.scalar_multi(d,c)
        my=Operations.scalar_multi_matrix(dc,mt)
        ma3=Operations.dif_matrix(me,my)
        return ma3
    def sums(self, matrix1, matrix2):
        matrix34=Operations.sum_matrix(matrix1,matrix2)
        return matrix34


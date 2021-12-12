#-------------------------------
#Паралельне програмування
#ПКС2СП на мові Python
#MA= min (D)*MX*MR – (D*C)*(MZ*MD)
#Лазарєв Матвій ІО-91
#12.12.21
#-------------------------------
import numpy as np

def ones_Matrix(N):
    ones_Matrix = np.ones( (N, N), dtype=np.int32 )
    return ones_Matrix

def rand_Matrix(N):
    Matrix= np.random.randint(0,10,(N,N))
    return Matrix

def ones_Vector(N):
    ones_Vectors = np.ones(N, dtype=np.int32 )
    return ones_Vectors

def rand_Vector(N):
    Vector= np.random.randint(0,10,N)
    return Vector

def multiplication_Matrix(matrix1,matrix2):
    multi_Matrix=matrix1.dot(matrix2)
    return multi_Matrix



def scalar_multi(vector1,vector2):
    multi_vector= sum(p*q for p,q in zip(vector1, vector2))
    return multi_vector

def min_vector(vector):
    minimal=min(vector)
    return minimal


def scalar_multi_matrix(a, matrix):
    multi_scalar_matrix=a*matrix
    return multi_scalar_matrix


def dif_matrix(matrix1,matrix2):
    rez_dif_matrix=matrix1-matrix2
    return rez_dif_matrix

def sum_matrix(matrix1,matrix2):
    rez_sum_matrix=matrix1+matrix2
    return rez_sum_matrix
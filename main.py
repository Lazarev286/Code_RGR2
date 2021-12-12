from mpi4py import MPI
import Operations
import T1, T2, T3, T4
import timeit
#-------------------------------
#Паралельне програмування
#ПКС2СП на мові Python
#MA= min (D)*MX*MR – (D*C)*(MZ*MD)
#Лазарєв Матвій ІО-91
#12.12.21
#-------------------------------
start = timeit.default_timer()
comm=MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
N=2400
if rank == 0:
    print("Task", rank + 1, "start")
    c = Operations.ones_Vector(N)
    md = Operations.ones_Matrix(N)
    t1 = T1.T1(c,md)
    # -----Принимает с Т2---------
    data_mx1 = comm.recv(source=1)
    data_mz1 = comm.recv(source=1)
    data_mr1 = comm.recv(source=1)
    data_d1 = comm.recv(source=1)
    # -----Принимает с Т2---------
    # -----Отправляет в Т2---------
    comm.send(t1.c, dest=1)
    comm.send(t1.md, dest=1)
    # -----Отправляет в Т2---------
    # -----Отправляет min(d) в Т2---------
    min_d1=t1.minimal(data_d1)
    comm.send(min_d1, dest=1)
    # -----Отправляет min(d) в Т2---------
    data_min_d = comm.recv(source=1)
    # ----------------------------------
    ma1 = t1.computation(data_mx1, data_mr1, data_min_d, data_mz1, t1.md, data_d1, t1.c)
    # ---------------------------------
    # -----Отправляет ma1 в Т2---------
    comm.send(ma1, dest=1)

    # -----Отправляет ma1 в Т2---------
    print("Task", rank + 1, "end")

if rank == 1:
    print("Task", rank + 1, "start")
    mx = Operations.ones_Matrix(N)
    mz = Operations.ones_Matrix(N)
    t2 = T2.T2(mx,mz)
    #-----Принимает с Т3---------
    data_mr2 = comm.recv(source=2)
    data_d2 = comm.recv(source=2)
    # -----Принимает с Т3---------
    # -----Отправляет в Т1---------
    comm.send(t2.mx, dest=0)
    comm.send(t2.mz, dest=0)
    comm.send(data_mr2, dest=0)
    comm.send(data_d2, dest=0)
    # -----Отправляет в Т1---------
    # -----Принимает с Т1---------
    data_c2 = comm.recv(source=0)
    data_md2 = comm.recv(source=0)
    # -----Принимает с Т1---------
    # -----Отправляет в Т3---------
    comm.send(t2.mx, dest=2)
    comm.send(t2.mz, dest=2)
    comm.send(data_c2, dest=2)
    comm.send(data_md2, dest=2)
    # -----Отправляет в Т3---------
    # -----Принимает с Т3 d34---------
    data_min_d34 = comm.recv(source=2)
    # -----Принимает с Т3 d34---------
    # -----Принимает с Т1 d1---------
    data_min_d1 = comm.recv(source=0)
    # -----Принимает с Т1 d1---------
    #----- min_d_____
    min_d = t2.minimal(data_d2, data_min_d34,data_min_d1)
    # ----- min_d _____
    #------Отправка min_d--------
    comm.send(min_d, dest=0)
    comm.send(min_d, dest=2)
    comm.send(min_d, dest=3)
    # ------Отправка min_d--------
    #------Приём ma34 ma1---------
    data_ma34=comm.recv(source=2)
    data_ma1 = comm.recv(source=0)
    #------Приём ma34 ma1---------
    ma2 = t2.computation(t2.mx, data_mr2, min_d, t2.mz, data_md2, data_d2, data_c2)
    ma=t2.sum_ma(data_ma1,ma2,data_ma34)
    print("Result Task", rank + 1, "=\n", ma)
    print("Task", rank + 1, "end")
if rank == 2:
    print("Task", rank + 1, "start")
    t3 = T3.T3()
    data_mr3 = comm.recv(source=3)
    data_d3 = comm.recv(source=3)
    comm.send(data_mr3, dest=1)
    comm.send(data_d3, dest=1)
    # -----Принимает с Т2---------
    data_mx3 = comm.recv(source=1)
    data_mz3 = comm.recv(source=1)
    data_c3 = comm.recv(source=1)
    data_md3 = comm.recv(source=1)
    # -----Принимает с Т2---------
    # -----Отправляет в Т4---------
    comm.send(data_mx3, dest=3)
    comm.send(data_mz3, dest=3)
    comm.send(data_c3, dest=3)
    comm.send(data_md3, dest=3)
    # -----Отправляет в Т4---------
    #----Минимум d3,4 и отправка-----
    data_min_d4 = comm.recv(source=3)
    min_d34=t3.minimal(data_d3,data_min_d4)
    comm.send(min_d34, dest=1)
    # ----Минимум d3,4 и отправка-----
    data_min_d = comm.recv(source=1)
    # ----------------------------------
    ma3 = t3.computation(data_mx3, data_mr3, data_min_d, data_mz3, data_md3, data_d3, data_c3)
    # ---------------------------------
    # -----Принимает ma4 с Т4---------
    data_ma4=comm.recv(source=3)
    # -----Принимает ma4 с Т4---------
    #-------Вычисление и отрправка ma34 в Т2
    ma34=t3.sums(ma3,data_ma4)
    comm.send(ma34, dest=1)
    # -------Вычисление и отрправка ma34 в Т2
    print("Task", rank + 1, "end")
if rank == 3:
    print("Task", rank + 1, "start")
    mr = Operations.ones_Matrix(N)
    d = Operations.ones_Vector(N)
    t4 = T4.T4(mr, d)
    # -----Отправляет в Т3---------
    comm.send(t4.mr, dest=2)
    comm.send(t4.d, dest=2)
    # -----Отправляет в Т3---------
    # -----Принимает с Т3---------
    data_mx4 = comm.recv(source=2)
    data_mz4 = comm.recv(source=2)
    data_c4 = comm.recv(source=2)
    data_md4 = comm.recv(source=2)
    # -----Принимает с Т3---------
    min_d4 = t4.minimal(d)
    comm.send(min_d4, dest=2)
    data_min_d = comm.recv(source=1)
    #----------------------------------
    ma4=t4.computation(data_mx4,t4.mr,data_min_d,data_mz4,data_md4,t4.d,data_c4)
    #---------------------------------
    # -----Отправляет ma4 в Т3---------
    comm.send(ma4, dest=2)
    # -----Отправляет ma4 в Т3---------
    print("Task", rank + 1, "end")

stop = timeit.default_timer()
print("The total elapsed time of the program is: ", stop-start)
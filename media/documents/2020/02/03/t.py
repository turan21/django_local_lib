from cvxopt.modeling import variable, op
import time


start = time.time()
x = variable(15, 'x')
c = [4, 1, 2, 4, 5, 6, 4, 5, 9, 5, 3, 1, 6, 5, 9]
z = (
        c[0]*x[0] + c[1]*x[1] + c[2]*x[2] + c[3]*x[3] + c[4]*x[4]
        + c[5]*x[5] + c[6]*x[6] + c[7]*x[7] + c[8]*x[8] + c[9]*x[9]
        + c[10]*x[10] + c[11]*x[11] + c[12]*x[12] + c[13]*x[13] + c[14]*x[14]
)
mass1 = (x[0] + x[1] + x[2] + x[3] + x[4] <= 50)
mass2 = (x[5] + x[6] + x[7] + x[8] + x[9] <= 70)
mass3 = (x[10] + x[11] + x[12] + x[13] + x[14] <= 110)

mass4 = (x[0] + x[5] + x[10] == 50)
mass5 = (x[1] + x[6] + x[11] == 50)
mass6 = (x[2] + x[7] + x[12] == 50)
mass7 = (x[3] + x[8] + x[13] == 50)
mass8 = (x[4] + x[9] + x[14] == 30)

x_non_negative = (x >= 0)
problem = op(z, [mass1, mass2, mass3, mass4, mass5, mass6, mass7, mass8, x_non_negative])
problem.solve(solver='glpk')
print("Результат :")
for i in x.value:
    print(i)
print("Стоимость доставки:")
print(problem.objective.value()[0])
stop = time.time()
print("Время :")
print(stop - start)

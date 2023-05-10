import math

def compute_q_array_EE(A, n, M):
    q = [1] + [0] * (n - 1)
    for i in range(1, n):
        q[i] = (M * A * q[i - 1]) / i
    return q

def compute_p_EE(P_array, n):
    p = [1] + [0] * (n - 1)
    for i in range(1, n):
        p[i] = (A * q[i - 1] + (N - y[i - 1]) * a2 * q[i - 1]) / i
    return p
def compute_q_array_EP(A, n, M):
    q = [1] + [0] * (n-1)
    for i in range(1, n):
        q[i] = (M * A * q[i-1]) / i
    return q

def compute_p_EP(P_array, n):
    p = [1] + [0] * (n-1)
    for i in range(1, n):
        p[i] = (A * q[i-1] + (NU-y[i-1]) * a2U * q[i-1]) / i
    return p
typ=input("Podaj 1 Jesli liczysz Erlang-Engset, ajesli Erlang-Pascal podaj 2 ")
print("Podaj zmienne ")
A =int(input("Zmienna A1 ")) #1
a2 =float(input("Zmienna alfa2 "))#0.5
N = int(input("Zmienna N "))#2
V = int(input("Zmienna V "))#2
u = int(input("Zmienna u "))#1

if typ=="1":
    A2 = N * a2
    q = compute_q_array_EE(int(A), int(N + 1), 2)
    G = 1 / sum(q)
    y = [0, a2 * N * q[0] / q[1], a2 * N * q[1] / q[2]]
    p = compute_p_EE(y, N + 1)
    G2 = 1 / sum(p)
    print("Wyliczone E(2):", math.ceil(G2 * p[2] * 1000) / 1000)

    sum = 0
    for i, element in enumerate(p):
        sum += element * G2 * (N - y[i]) * a2 * u

    B2 = p[2] * G2 * (N - y[2]) * a2 * u / sum

    print("Wyliczone B(2):", math.ceil(B2 * 1000) / 1000)
elif typ=="2":

    NU= N*-1
    a2U=a2*-1
    A2 = N*a2

    q = compute_q_array_EP(int(A), int(N + 1), 2)

    G = 1/sum(q)

    y = [0,a2*N*q[0]/q[1],a2*N*q[1]/q[2]]

    p = compute_p_EP(y, N+1)
    G2 = 1/sum(p)
    print("Wyliczone E(2):", math.ceil(G2 * p[2] * 1000) / 1000)

    sum = 0
    for i, element in enumerate(p):
        sum += element * G2 * (NU - y[i])*a2U*u

    B2 = p[2]*G2 * (NU - y[2])*a2U*u / sum

    print("Wyliczone B(2):", math.ceil(B2 * 1000) / 1000)
p = input("p(pa or N/m^2): ")
v = input("V(m^3): ")
n = input("n(mol): ")
t = input("T(k): ")
R = 8.314 

if p =="" :
    v, n, t = float(v), float(n), float(t)
    p = (n * R * t) / v
    print(f"{p} Pa")
elif v =="":
    p, n, t = float(p), float(n), float(t)
    v = (n * R * t) / p
    print(f"{v} m^3")
elif t =="":
    v, n, p = float(v), float(n), float(p)
    t = (p * v) / (n * R)
    print(f"{t} k")
elif n =="":
    v, p, t = float(v), float(p), float(t)
    n = (p * v) / (R * t)
    print(f"{n} mol")


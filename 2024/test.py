from decimal import Decimal, getcontext

# Configurer la précision à 100 000 décimales
getcontext().prec = 1000  # Précision arbitraire (ajustez selon vos besoins)

# Initialisation
a0 = Decimal(2).sqrt()  # Utilisez Decimal.sqrt() pour calculer la racine carrée

def anp1(an):
    return (Decimal(2) - (Decimal(4) - an * an).sqrt()).sqrt()

pi = open("pi.txt", "r").readlines()

an = a0
for i in range(100):
    an = anp1(an)
    pi_approx = Decimal(2**(i+2)) * an
    print(f"Iteration {i+1}: pi ≈ {pi_approx}")

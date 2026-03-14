import math as m
import datetime as dt

t0=37
t_env=float(input("Rentrer la temperature environnante:"))
t=float(input("Rentrer la temperature corporel de l'individu:"))
M=float(input("Quel est le poids de l'individu:"))
k=(1.2815/(M**0.625))-0.024
coeff={
    (1,1,1):1,
    (1,1,2):0.5,
    (1,2,1):1.1,
    (1,2,2):0.8,
    (1,3,1):1.2,
    (1,3,2):1.2,
    (1,4,1):1.4,
    (1,4,2):1.2,
    (2,1,1):0.75,
    (2,1,2):0.7,
    (2,2,1):0.9,
    (2,2,2):0.7,
    (2,3,1):1.2,
    (2,3,2):0.9,
    (2,4,1):1.4,
    (2,4,2):0.9,
    (3,1,1):0.5,
    (3,2,1):0.7,
    (3,3,1):0.9,
    (3,4,1):1,
    (4,1,1):0.35,
    (4,2,1):0.5,
    (4,3,1):0.8,
    (4,4,1):1
}
print("Dans quel environnement se trouvait l'individu ?")
print("1-Air calme")
print("2-Air en mouvement")
print("3-Eau stagnante")
print("4-Eau courante")
a=float(input("Réponse:"))
print("Dans quel condition se trouvait l'individu:")
print("1-Corps nu")
print("2-Corps peu habillé")
print("3-Corps habillé moderement")
print("4-Corps chaudements habillé")
aa=float(input("Réponse:"))
if aa in range(1,3):
    print("Informations complémentaire:")
    print("1-Vêtements humide et/ou corps mouillé")
    print("2-Vêtements et/ou corps sec")
    aaa=float(input("Réponse:"))
else:
    aaa=1
c=coeff[(a,aa,aaa)]
T=(-m.log((t-t_env)/(t0-t_env))/(k*c))
TT=dt.datetime.now()-dt.timedelta(T)
if c<1:
    print(f"L'individu est dédédé le {TT}h, et son corps refroidi plus rapidemment")
elif c>1:
    print(f"L'individu est dédédé le {TT}h, et son corps refroidi plus lentement")
else:
    print(f"L'individu est dédédé le {TT}h, et sa temperature reste stable")
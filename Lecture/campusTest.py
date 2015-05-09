import gens, transport

bond = gens.Gens("James")
drno = gens.Gens("bowler hat")

print(bond.info())

protagonists = [bond, drno]
pen = gens.Choses("Montblanc")
q_mobile = transport.Vehicle(protagonists)
aston = transport.Car([bond], [drno], "aviation fuel", 5)



print(bond.info())
print(aston.info())
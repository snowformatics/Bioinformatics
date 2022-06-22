
molarity = 0.5
volume = 1

molar_mass = 58.44

weight_mass = float(molar_mass) * float(volume) * float(molarity)
weight_mass = round(weight_mass, 4)

message = "Weight out " + str(weight_mass) + " g " \
          + str('NaCL') + " and dissolve in " + str(volume) + " L water."

print (message)
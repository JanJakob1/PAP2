import matplotlib.pyplot as plt
import numpy as np
def comma_to_float(valstr):
    return float(valstr.decode("utf-8").replace(',', '.'))
# Integrationszeit so gewählt, dass hellste Linie nicht in Sättigung
lamb_gesamt_1, inten_gesamt_1 = np.loadtxt('data/natrium_komplett_1.txt',
                                           skiprows = 17,
                                           converters = {0:comma_to_float, 1:comma_to_float},
                                           comments = '>',
                                           unpack = True)

# Längere Integrationszeit, damit wesentlicher Teil des Spektrums sichtbar
lamb_gesamt_2, inten_gesamt_2 = np.loadtxt('data/natrium_komplett_2.txt',
                                           skiprows = 17,
                                           converters = {0:comma_to_float, 1:comma_to_float},
                                           comments = '>',
                                           unpack = True)

# Integrationszeit für 400 - 540 nm optimiert
lamb_schwach, inten_schwach = np.loadtxt('data/natrium_niedrige_intensitaet.txt',
                                         skiprows = 17,
                                         converters = {0:comma_to_float, 1:comma_to_float},
                                         comments = '>',
                                         unpack = True)
plt.plot(lamb_schwach, inten_schwach, linewidth = 1)
plt.title("Natriumspektrum (kurzwellig)")
plt.xlabel("Wellenlänge [nm]")
plt.ylabel("Intensität [b.E.]")
plt.yscale("log")
plt.ylim((250, 60000))
plt.xlim((300, 540))
plt.show()

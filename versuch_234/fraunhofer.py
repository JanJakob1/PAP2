
# coding: utf-8

# In[12]:


import matplotlib.pyplot as plt
import numpy as np


# SpectraSuite verwendet Kommata als Dezimaltrennzeichen, die durch Punkte ersetzt werden müssen:

# In[13]:


def comma_to_float(valstr):
    return float(valstr.decode("utf-8").replace(',', '.'))


# # Analyse des Sonnenlichts

# Zunächst werden die Daten mit und ohne Fenster geladen.
# Die ersten 17 Zeilen sowie alle Zeilen, die mit '>' beginnen, sind Header und Kommentare und werden deshalb ausgelassen.

# In[14]:


lamb_og, inten_og = np.loadtxt('data/sonne_ohne_glas.txt',
                               skiprows = 17,
                               converters = {0:comma_to_float, 1:comma_to_float},
                               comments = '>',
                               unpack = True)


# In[15]:


lamb_mg, inten_mg = np.loadtxt('data/sonne_durch_glas.txt',
                               skiprows = 17,
                               converters = {0:comma_to_float, 1:comma_to_float},
                               comments = '>',
                               unpack = True)


# Die beiden Intensitätsverteilungen werden nun in ein gemeinsames Diagramm eingezeichnet:

# In[16]:


# ## Absorption von Glas

# Die Absorption von Glas ist gegeben durch
# $$A(\lambda) = 1 - \frac{I_{mG}(\lambda)}{I_{oG}(\lambda)}$$

# In[17]:



# Die Absorption wird nun als Funktion der Wellenlänge dargestellt:

# In[19]:


# ## Fraunhoferlinien

# In[20]:


plt.plot(lamb_og, inten_og, linewidth = 1)
plt.title("Sonnenspektrum")
plt.xlabel("Wellenlänge [nm]")
plt.ylabel("Intensität [b.E.]")
plt.ylim((0, 65000))
plt.xlim((350, 800))
plt.show()


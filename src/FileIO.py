
import pickle

#Salva qualsiasi oggetto in un file
def save_obj(obj, name ):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

#Carica un oggetto salvato in un file
def load_obj(name ):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)

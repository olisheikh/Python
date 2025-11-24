

import pickle_class, pickle

with open('store_obj.data', 'rb') as f:
    for i in range(3):
        s = pickle.load(f)
        s.show()
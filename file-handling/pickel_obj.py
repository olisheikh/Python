
import pickle_class, pickle 

students = [pickle_class.Student(1, 'Rahim', 'CS'), pickle_class.Student(2, 'Karim', 'ME'), pickle_class.Student(3, 'Jamal', 'IPE')]

with open('store_obj.data', 'wb') as f:
    for s in students:
        pickle.dump(s, f)

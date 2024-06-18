import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    calculations={}
    array = np.array(list).reshape(3,3)
    calculations['mean'] = [np.mean(array, axis=0).tolist(), np.mean(array, axis=1).tolist(), np.mean(array)]
    calculations['variance'] = [np.var(array, axis=0).tolist(), np.var(array, axis=1).tolist(), np.var(array)]
    calculations['standard deviation'] = [np.std(array, axis=0).tolist(), np.std(array, axis=1).tolist(), np.std(array)]
    calculations['max'] = [np.max(array, axis=0).tolist(), np.max(array, axis=1).tolist(), np.max(array)]
    calculations['min'] = [np.min(array, axis=0).tolist(), np.min(array, axis=1).tolist(), np.min(array)]
    calculations['sum'] = [np.sum(array, axis=0).tolist(), np.sum(array, axis=1).tolist(), np.sum(array)]
    




    return calculations
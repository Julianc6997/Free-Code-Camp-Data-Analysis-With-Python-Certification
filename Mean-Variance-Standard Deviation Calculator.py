import numpy as np

def calculate(list):  
    if len(list) != 9:
        raise ValueError('List must contain nine numbers.')
    
    list = np.array(list)
    list = list.reshape((3,3))

    results = {}

    results['mean'] = [np.mean(list, axis=0).tolist(), np.mean(list, axis=1).tolist(), np.mean(list).tolist()]
    results['variance'] = [np.var(list, axis=0).tolist(), np.var(list, axis=1).tolist(), np.var(list).tolist()]
    results['standard deviation'] = [np.std(list, axis=0).tolist(), np.std(list, axis=1).tolist(), np.std(list).tolist()]
    results['min'] = [np.min(list, axis=0).tolist(), np.min(list, axis=1).tolist(), np.min(list).tolist()]
    results['max'] = [np.max(list, axis=0).tolist(), np.max(list, axis=1).tolist(), np.max(list).tolist()]
    results['sum'] = [np.sum(list, axis=0).tolist(), np.sum(list, axis=1).tolist(), np.sum(list).tolist()]

    return results


print(calculate([0,1,2,3,4,5,6,7,8]))
import numpy as np 

def combination(array_1, array_2, axis=0):
    array_1 = np.squeeze(array_1)
    array_2 = np.squeeze(array_2)

    array_1_shape = list(array_1.shape)
    array_2_shape = list(array_2.shape)

    array_1_shape.pop(axis)
    array_2_shape.pop(axis)
    
    if array_1_shape == array_2_shape:

        result = np.concatenate([array_1, array_2], axis=axis)
        return result

    else:
        raise ValueError(f"Can not concatenate array_1 array_2 along axis {axis}")

if __name__ == "__main__":
    array_1 = np.zeros(shape=(5,5))
    array_2 = np.zeros(shape=(5,5))

    combination(array_1, array_2, axis=0)
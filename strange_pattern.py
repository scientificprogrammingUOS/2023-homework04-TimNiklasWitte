import numpy as np
#import matplotlib.pyplot as plt


def strange_pattern(shape):

    try:
        n, m = shape
    except:
        raise ValueError("shape must be (n,m)")
    

    pattern = np.zeros(shape=(n,m), dtype=bool)

    pattern[::3, ::3] = True
    pattern[1::3, 2::3] = True
    pattern[2::3, 1::3] = True

    return pattern

   
if __name__ == "__main__":
    # use this for your own testing!

    x = strange_pattern((50,50))

   
    #plt.imshow(x)
    
    #plt.show()

    pattern = np.arange(100)
    pattern = np.reshape(pattern, (10,10))

    print(pattern)
    print("------------")
    print(pattern[::3])
    print(pattern[::3, ::3])

    print("###########")
    print(pattern[::3][::3])

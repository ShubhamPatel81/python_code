import sympy
import scipy
import numpy
import math
import numpy as np

x = np.array(['python', 'PHP', 'java', 'C++'], dtype=np.str)
print("Original Array:")
print(x)
capitalized_case = np.char.capitalize(x)
lowered_case = np.char.lower(x)
uppered_case = np.char.upper(x)
swapcased_case = np.char.swapcase(x)
titlecased_case = np.char.title(x)
print("\nCapitalized: ", capitalized_case)
print("Lowered: ", lowered_case)
print("Uppered: ", uppered_case)
print("Swapcased: ", swapcased_case)
print("Titlecased: ", titlecased_case)

# import scypy and ,math

print(math.pi == numpy.pi)
print(math.pi == scipy.pi)
print(math.pi == sympy.pi)

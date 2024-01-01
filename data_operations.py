# Data Operations in Numpy

# example1
# more than one dimensions
import numpy as np
a = np.array([[1,2],[3,4]])
print(a)

print("\n")

# example2
# minimum dimensions
import numpy as np
a = np.array([1, 2, 3, 4, 5], ndmin = 2)
print (a)

print("\n")

# example3
# dtype parameter
import numpy as np
a = np.array([1, 2, 3], dtype = complex)
print (a)

print("\n")
# Data Operations in Pandas

# Pandas Series Example
#import the pandas library and aliasing as pd
import pandas as pd
import numpy as np
data = np.array(['a','b','c','d'])
s = pd.Series(data)
print (s)

print("\n")

# Pandas DataFrame Example
import pandas as pd
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
print (df)

print("\n")
# Question: Store your four friends name with their marks of any subjects in Pandas DataFrame for practice.
import pandas as pd
data = {'Name':['Ravi','Dinesh','Arun','Ashwani'], 'Marks':[60,70,80,75]}
df = pd.DataFrame(data, index=['Student 1','Student 2','Student 3', 'Student 4'])
print(df)

print("\n")

# Pandas Panel Example
#creating an empty panel
import pandas as pd
import numpy as np

data = {'Item1': pd.DataFrame(np.random.randn(4, 3)),
        'Item2': pd.DataFrame(np.random.randn(4, 2))}

# Create a dictionary of DataFrames instead of using Panel
p = pd.concat(data, axis=1)
print(p)

#  how we can handle missing values
# import the pandas library
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f',
'h'],columns=['one', 'two', 'three'])

df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

print(df)

print("\n")

# Check for missing values
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f','h'], columns=['one', 'two', 'three'])

df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

print(df)
print(df['one'].isnull())


print("\n")

# Cleaning / Filling Missing Data
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(3, 3), index=['a', 'c', 'e'],columns=['one', 'two', 'three'])
df = df.reindex(['a', 'b', 'c'])
print (df)
print("\n")
print ("NaN replaced with '0':")
print (df.fillna(0))


print("\n")

# Fill NA Forward and Backward
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f','h'],columns=['one', 'two', 'three'])
df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

print(df)
print("\n")
print(df.fillna(method='pad'))

print("\n")

# Fill NA Forward and Backward with no future warnings
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f', 'h'], columns=['one', 'two', 'three'])
df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

print("\n")
print("\n")

# Drop Missing Values
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f', 'h'], columns=['one', 'two', 'three'])

df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print("Printing values including missing values \n")
print(df)
print("\n")
print (df.dropna())
print("\n")
print("Printing values including missing values \n")
print(df)
print("\n")
print(df.ffill())


print("\n")
# Replace Missing (or) Generic Values
import pandas as pd
import numpy as np
df = pd.DataFrame({
                    'one':[10,20,30,40,50,2000],
                    'two':[1000,0,30,40,50,60]
                  })
print (df.replace({1000:10, 2000:60}))

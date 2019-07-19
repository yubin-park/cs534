import numpy as np
import pandas as pd
n = 100
x1 = np.random.randn(n)
x2 = np.random.randn(n)
# the formula should be secret
y = x1 + np.log(np.abs(x2) + 1.0) + x1 * x2  
df = pd.DataFrame({"x1": x1, "x2": x2, "y": y})
df.to_csv("hw0_p1.csv", index=False)



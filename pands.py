import pandas as pd
rt matplotlib.pyplot as plt

df = pd.read_csv('/home/t12652/data.csv')


df["Duration"].plot(kind = 'hist')


plt.show()


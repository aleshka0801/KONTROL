import pandas as pd
import matplotlib.pyplot as plt
x = [ 'кемерово','москва','казань','краснодар','севастополь']
y = [550000,13100000,1330000,1150000,547000]

plt.bar(x,y)

plt.title('население городов')
plt.xlabel('города')
plt.ylabel('население')
plt.grid(False)

plt.show()
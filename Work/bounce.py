# bounce.py
#
# Exercise 1.5
import pandas as pd

drop_height = 100
bounce_factor = 3/5
count = 0
bouncing_data = []

while count < 10:
    count += 1
    bouncing_height = drop_height*bounce_factor
    bouncing_data.append('{:.4f}'.format(bouncing_height).rstrip('0').rstrip('.'))
    drop_height = bouncing_height

bouncing_data = pd.DataFrame(bouncing_data)
bouncing_data = round(bouncing_data, 4).astype('float')
bouncing_data.index = range(1, len(bouncing_data) + 1)
print(bouncing_data)
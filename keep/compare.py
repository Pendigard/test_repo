#%%
import pandas as pd

with open('rital_tmp/submission-movie-1.csv') as f:
    l1 = f.readlines()
with open('rital_tmp/submission-movie-2.csv') as f:
    l2 = f.readlines()

n_diff = 0
for i, j in zip(l1, l2):
    if i != j:
        n_diff += 1

print(f'Number of different lines: {n_diff}')
print(f'Percentage of different lines: {n_diff / len(l1) * 100:.2f}%')
# %%

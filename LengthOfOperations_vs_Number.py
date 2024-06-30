import altair as alt
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def collatz(n):
    if n == 1:
        result = [1]
    elif n % 2 == 0:
        result = collatz(n // 2) + [n]
    elif n % 2 == 1:
        result = collatz((3 * n) + 1) + [n]
    return result
#collatz(1589)
runs=5000
seen = {}
sequence_lengths=[]
for i in range(1, runs):
    length = collatz(i)
    sequence_lengths.append(len(length))
    #print(sequence_lengths)
collatz(17)
df=pd.DataFrame(zip(np.arange(1,runs),sequence_lengths), columns=["i","len"])
print(df)
df['is_even']=df['i'].apply(lambda x: 1 if x%2==0 else 0)
domain=['Odd', 'Even']
alt.Chart(df).mark_circle(opacity=0.35).encode(
    x=alt.X('i',scale=alt.Scale(domain=(0, 5000)), axis=alt.Axis(title='N')),
    y=alt.Y('len', axis=alt.Axis(title='Length of Collatz Sequence')),
    color=alt.Color('is_even:N', scale=alt.Scale(scheme="magma"), legend=None)
).properties(
    width=1080,
    height=1080,
    title='Collatz Sequence',
).configure_axis(
    grid=True
).configure_view(
    strokeOpacity=1
)

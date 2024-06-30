import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Collatz sequence function
def collatz(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

# Generate data
max_num = 1000
data = []
for i in range(1, max_num+1):
    sequence = collatz(i)
    data.append({
        'start': i,
        'length': len(sequence),
        'max': max(sequence)
    })

# Convert to Pandas DataFrame
df = pd.DataFrame(data)

# Bar chart using Matplotlib
plt.figure(figsize=(10, 6))
# This bar chart shows the length of the Collatz sequence for each starting number
# X-axis: Starting numbers from 1 to 1000
# Y-axis: Length of the Collatz sequence for each starting number
plt.bar(df['start'], df['length'])
plt.xlabel('Starting Number')
plt.ylabel('Sequence Length')
plt.title('Collatz Conjecture Sequence Lengths')
plt.show()

# Histogram using Seaborn
plt.figure(figsize=(10, 6))
# This histogram shows the distribution of Collatz sequence lengths
# X-axis: Different sequence lengths observed
# Y-axis: Count of starting numbers that result in each sequence length
sns.histplot(data=df, x='length', bins=200)
plt.xlabel('Sequence Length')
plt.ylabel('Count')
plt.title('Histogram of Collatz Conjecture Sequence Lengths')
plt.show()

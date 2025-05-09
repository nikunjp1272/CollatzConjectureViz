# CollatzConjectureViz

## The Collatz Conjecture

The Collatz Conjecture or the Collatz Sequence is a very well-known problem in mathematics.
Here's how it works:

1.  Pick any random number you can think of.
2.  If the number is even, divide it by 2.
3.  If the number is odd, multiply it by 3 and add 1 to it.
4.  Repeat this process until you get to the number '4'.

After reaching the number 4 you'll realize that you're stuck in an endless loop of 4 -> 2 -> 1
Even the largest number that you could think of ends with this loop.
The `collatz.py` file has the basic code of how the problem works and you can plug in various numbers to check out how the function behaves.

## Visualizations

We can see the Sequence lengths of each of the numbers (till 1000) in the Bar Chart below:

<img alt="Starting Number vs Sequence Length" src="https://github.com/nikunjp1272/CollatzConjectureViz/blob/main/images/BarChart.png" style="width:750px; height:500px;">

And the below Histogram shows the frequency of each of the Sequence Lengths:

<img alt="Sequence Length vs the Frequency of the Sequence Lengths" src="https://github.com/nikunjp1272/CollatzConjectureViz/blob/main/images/Histogram.png" style="width:750px; height:500px;">

Below is a scatter plot of all the numbers between 5000 (on X-axis) vs the number of operations they take to reach '1'.

<img alt="Length Of Operations vs Number" src="https://github.com/nikunjp1272/CollatzConjectureViz/blob/main/images/LengthOfOperations_vs_Number.png" style="width:750px; height:500px;">

Another visualization that looks almost like a coral, is another depiction of how the Collatz Sequence progresses.

<img alt="" src="https://github.com/nikunjp1272/CollatzConjectureViz/blob/main/images/RainbowCoral.png" style="width:750px; height:500px;">

The credits for the idea of this visualization go to **Numberphile** on YouTube. However the image is not taken from the video itself.

[Link to the Numberphile video 'UNCRACKABLE? The Collatz Conjecture - Numberphile'](http://www.youtube.com/watch?v=5mFpVDpKX70)

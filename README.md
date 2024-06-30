# CollatzConjectureViz

<h2>The Collatz Conjecture</h2>
The Collatz Conjecture or the Collatz Sequence is a very well-known problem in matehmatics.
Here's how it works:
<ol>
  <li>Pick any random number you can think of.</li>
  <li>If the number is even, divide it by 2.</li>
  <li>If the number is odd, multiply it by 3 and add 1 to it.</li>
  <li>Repeat this process until you get to the number '4'.</li>
</ol>
After reaching the number 4 you'll realize that you're stuck in an endless loop of 4 -> 2 -> 1
Even the largest number that you could think of ends with this loop.
The collatz.py file has the basic code of how the problem works and you can plug in various numbers to check out how the function behaves.

Below is a scatter plot of all the numbers between 5000 (on X-axis) vs the number of operations they take to reach '1'.

<img alt="Length Of Operations vs Number" src="https://github.com/nikunjp1272/CollatzConjectureViz/blob/main/images/LengthOfOperations_vs_Number.png" style="width:750px; height:500px;">

Another visualization that looks almost like a coral, is another depiction of how the Collatz Sequence progresses.

<img alt="" src="https://github.com/nikunjp1272/CollatzConjectureViz/blob/main/images/RainbowCoral.png" style="width:750px; height:500px;">

The credits for the idea of this visualization go to <b>Numberphile</b> on YouTube. However the image is not taken from the video itself.
[Link to the video of Numberphile](https://youtu.be/LqKpkdRRLZw?si=tXq4PwXQx2UhsLI0)

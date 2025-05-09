# 📐 Collatz Conjecture Visualizations

## What is the Collatz Conjecture?

The Collatz Conjecture is a famous unsolved problem in mathematics. It works like this:

1.  Pick any positive integer.
2.  If the number is even, divide it by 2.
3.  If the number is odd, multiply it by 3 and add 1.
4.  Repeat the process with the resulting number.

Eventually, every number tested so far ends in the loop: 4 → 2 → 1 → 4...

## 📊 Visualizations Included

### 🔁 Sequence Length Bar Chart

This bar chart displays the number of steps (sequence length) each starting number (from 1 to 1000) takes to reach 1.

<img alt="Starting Number vs Sequence Length" src="https://github.com/nikunjp1272/CollatzConjectureViz/blob/main/images/BarChart.png" style="width:750px; height:500px;">

### 📉 Histogram of Sequence Lengths

This histogram shows the distribution of how long the sequences are for numbers up to 1000.

<img alt="Histogram of Sequence Lengths" src="https://github.com/nikunjp1272/CollatzConjectureViz/blob/main/images/Histogram.png" style="width:750px; height:500px;">

### 🐢 Turtle Graphics (Spiral View)

This unique visualization uses turtle graphics to draw turning paths based on whether the number is even or odd:

* **Even → Turn Left**
* **Odd → Turn Right**

Each path traces the journey of a number down the Collatz sequence.

<img alt="Turtle Path Visualization" src="https://github.com/nikunjp1272/CollatzConjectureViz/blob/main/images/Spirals.png" style="width:750px; height:500px;">

## 📂 Files

* `collatz.py`: Core logic for generating Collatz sequences.
* `visuals.py`: Code for plotting bar charts and histograms.
* `turtle_viz.py`: Code for spiral turtle graphics.
* `images/`: Contains the output images shown above.

## 🚀 Getting Started

Make sure you have Python 3 installed. Then install the required libraries:

```bash
pip install matplotlib turtle
```
Run the files:
python collatz.py         # For basic sequence testing
python visuals.py         # To generate bar/histogram charts
python turtle_viz.py      # To draw turtle graphics

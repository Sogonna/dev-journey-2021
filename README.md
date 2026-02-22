# dev-journey-2021

**My very first programming attempts – 2021**

These are the small Python scripts I wrote back in 2021 while I was still a microbiology student.  
I got really tired of doing everything manually in Excel — endless copying, calculation mistakes, and hard-to-read lab notebooks. So I decided to teach myself Python basics just to make sense of my experimental data faster and with less errors.

This repository is exactly that starting point for me — the moment I realized that writing code could actually become a real tool for science.  
The code is very simple, not clean, not professional — but that's the point. This is where everything really began for me.

### The projects (all inside the bioinformatics/ folder)

- **growth-curve-analysis.py**  
  My very first one: plots bacterial growth curves (OD600) for control and antibiotic-treated conditions. Just points and two lines, but it was the first time I turned real lab numbers into a visual graph.

- **cfu.py**  
  Compares average bacterial growth (CFU/ml after 24h) in three different culture media (LB, Nutrient Agar, TSA). It calculates mean and standard deviation and draws a bar chart with error bars. I wrote this for a class assignment — my first time using groupby in pandas.

- **log-reduction-disinfectant.py**  
  Calculates log₁₀ reduction after disinfectant exposure at different times. Prints a small table and draws a line plot with the reduction values written on each point.

- **disinfectant-efficacy-comparison.py**  
  A slightly different take on disinfectant effect — shows log reduction + percentage reduction, uses scatter points with a dashed line, and adds two-line annotations on the plot. Still beginner level, but a small step forward from the previous version.

### Technologies 

- Plain Python
- pandas — for organizing data and quick stats
- matplotlib — for making plots (lines, bars, text on points)
- numpy — only for log10 calculations

2021: First steps from microbiology lab notebooks to Python – Simple data analysis &amp; visualization scripts

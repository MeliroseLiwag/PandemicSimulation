# Pandemic Simulation in ARENA
#### Contributors: Shiv Chhabra, Kartikaye Gomber, Adarshkumar Gouda, and Melirose Liwag

# Report
See more details and the full report in the file [`FinalReport.pdf`](/FinalReport.pdf)

# Description
This project explores a small-scale pandemic-like simulation using the ARENA simulation software. The project will explore a hypothetical scenario of a classroom of 31 children, and supposing Tommy to be our patient zero. To mirror real life, each of the 30 children is equally likely to get infected by Tommy and is equally as likely to be susceptible to the flu. To start, we will assume that Tommy comes to school every day whether he is sick or not and will be infectious for 3 days starting on Day 1. With this, we will also assume that Tommy will be the only one infectious on Day 1 and the rest of the 30 children are healthy. Additionally, Tommy has a 0.02 probability of infecting other children on each of the 3 days he is infectious. Any kid infected by Tommy from Day 1 onwards will also be infectious for 3 days starting the day after infection. Furthermore, we will assume that each day and kid in the classroom are all independent and identical with a Bernoulli distribution (Bern(p)). 

# Files
  1. [`Project With immunization`](/Final_CodeAndData/Project%20With%20immunization.doe) and [`Project Without immunization`](/Final_CodeAndData/Project%20Without%20immunization.doe) - ARENA simulation files
     - The simulation itself is set to output into our local machines and our team noticed that the simulation takes around 20+ minutes to run (30-40 minutes at most) through all 100,000 replications so, we do not recommend running our simulation on your own. The simulation files are added to show the flow and process of generating our data
  2. [`Report with Immunization - 100000 reps.csv`] and [`Report 100000 reps.csv`] - CSV files that contain simulation outputs
     - Fairly large and a preview of these files may not be available here on GitHub. The following is a screenshot of how the files should look (Notice that the file with immunization does not have a header, which is taken into account in analyses code files later):
         - Report with Immunization - 100000 reps: ![Output of simulation with immunization](/Images/output_immunization.PNG)
         - Report 100000 reps: ![Output of simulation without immunization](/Images/output.PNG)
  3. [`ExpectedNumberPerDay.py`](/Final_CodeAndData/ExpectedNumberPerDay.py) - Python file
      - This file keeps track of statistical calculations needed for the final report. Analyses include: finding the sample means and confidence intervals for days 1 and 2 as well as finding the average number of infected from all replications.
  4. [`SIR Differential Equation Model.ipynb`](/Final_CodeAndData/SIR%20Differential%20Equation%20Model.ipynb) - Jupyter Notebook
      - This notebook is used to simulate the scenario using the SIR differential method (which is further explained in the [`report`](/FinalReport.pdf)
    
# Methods
  1. Reed-Frost Model
     - The Reed-Frost model was used as a base calculation for this small-scale simulation. Also known as the "Chain Binomial" model, it is widely known to be used in pandemic-like situations such as this project.
  2. Bernoulli Trials
     - Similar to the Reed-Frost model, however, a regular binomial trial is used to calculate the probability of infection per child instead of a chain binomial.
  4. SIR Differential
     - This method separates the situation into three categories: Susceptible, Infectious, and Recovered. Using differential equations, the probability of infection is calculated to include a 'transition rate' and a 'recovery rate'.

The three models were compared in terms of how long each simulation expects the epidemic to end. As shown in the table below, there is no clear interval in how long the epidemic will really last without immunization. Because this project is very small and limited, other significant factors, that may not be considered here, may result in a more significant finding than what our team has so far.

![Model Comparison](/Images/model_compare.PNG)


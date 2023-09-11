ISYE 6644 Summer 2023 - Final Project
Group:123
Members: Shiv Chhabra, Kartikaye Gomber, Adarshkumar Gouda, and Melirose Liwag

**IMPORTANT NOTES**
ARENA Files: Project Without immunization.doe and Project With immunization.doe
notes: 
- Each ARENA model has a module to write to a CSV for us to collect data however, the output
  location has to be updated to your local machine before running the simulation should you
  want to run it and look at the resulting CSV.
- Each ARENA model is set to run 100,000 Replications which can result in the program
  running a little over 20 minutes (30-40 minutes at most).

CSV files: Report 100000 reps.csv and Report with Immunization - 100000 reps.csv
notes:
- Files might take ~5 minutes to open as they are fairly large.
- These files are results produced by the ARENA programs attached and will be used to produce
  analytical results for the following Python files.
- Both files are from scenarios without immunization and with immunization respectively

Python File: ExpectedNumberPerDay.py
notes:
- This python file is used to tabulate the data produced by the ARENA program and get
  the expected values as seen in the final report (Group123FinalReport.pdf)
- This file is also used to caluclate the confidence intervals for both without immunization 
  and with immunization for Day 1 and Day 2

Python Jupyter Notebook: SIR Differential Equation Model.ipynb
notes:
- This notebook is used to simulate the scenario using the SIR Differential method
  as mentioned in the final report (Group123FinalReport.pdf)
- Any results produced by this code is reflected in the final report as well
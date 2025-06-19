import pandas as pd
from fpdf import FPDF
import matplotlib.pyplot as plt

# 1. Load data
df = pd.read_csv("Task 2.csv")

# 2. Analyze data: Average power level per anime
summary = df.groupby("Anime")["Power_Level"].mean().reset_index()
summary = summary.sort_values(by="Power_Level", ascending=False)

# 3. Save chart
plt.figure(figsize=(8, 4))
plt.bar(summary["Anime"], summary["Power_Level"], color='skyblue')
plt.title("Average Power Level by Anime")
plt.ylabel("Power Level")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Task 2.png")
plt.close()

# 4. Generate PDF report
pdf = FPDF()
pdf.add_page()

# Title
pdf.set_font("Arial", 'B', 16)
pdf.cell(0, 10, "Anime Character Power Report", ln=True, align='C')

# Subtitle
pdf.set_font("Arial", '', 12)
pdf.cell(0, 10, "Analyzed by Automated Python Script", ln=True, align='C')
pdf.ln(10)

# Table Header
pdf.set_font("Arial", 'B', 12)
pdf.cell(80, 10, "Anime", border=1)
pdf.cell(40, 10, "Avg Power Level", border=1, ln=True)

# Table Data
pdf.set_font("Arial", '', 12)
for _, row in summary.iterrows():
    pdf.cell(80, 10, row["Anime"], border=1)
    pdf.cell(40, 10, f"{row['Power_Level']:.2f}", border=1, ln=True)

pdf.ln(10)

# Chart
pdf.image("Task 2.png", x=10, w=180)

# Output file
pdf.output("Task 2.pdf")
print("PDF report generated as Task 2")

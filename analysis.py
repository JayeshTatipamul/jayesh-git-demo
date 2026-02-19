import pandas as pd

df = pd.read_csv("data.csv")

print("Average Salary:", df["salary"].mean())

import pandas as pd
import matplotlib.pyplot as plt

file_path = "./IMDB-Movie-Data.csv"
df = pd.read_csv(file_path)

print(df["Genre"])

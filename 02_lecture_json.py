import pandas as pd

donnees = pd.read_json('01_data.json')

print(donnees.to_string())

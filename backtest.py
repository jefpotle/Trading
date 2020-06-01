import pandas as pd
import os

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
df = pd.read_csv(desktop + "\daily_stocks.csv" )

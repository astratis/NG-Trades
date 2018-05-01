from urllib.request import urlopen
import pandas as pd

url = 'https://trades.nationalgrid.co.uk/download-csv'
data = urlopen(url)
my_table = pd.read_table(data, delimiter = ',')
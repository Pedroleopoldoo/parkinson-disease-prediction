# Install dependencies as needed:
# pip install kagglehub[pandas-datasets]
import kagglehub
from kagglehub import KaggleDatasetAdapter

# Set the path to the file you'd like to load
file_path = "Parkinsons-Telemonitoring-ucirvine.csv"

# Load the latest version
df = kagglehub.dataset_load(
  KaggleDatasetAdapter.PANDAS,
  "porinitahoque/parkinsons-telemonitoring",
  file_path,
)

df.to_csv('dataset.csv', index=False)
print("First 5 records:", df.head())
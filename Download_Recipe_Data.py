# Taking data from the web.

# check Python version
# !python -V

import pandas as pd # download library to read data into dataframe
pd.set_option('display.max_columns', None)

# Uncomment if running locally, else download data using the following code cell
# recipes = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0103EN-SkillsNetwork/labs/Module%202/recipes.csv")

import piplite
await piplite.install(['skillsnetwork'])
import skillsnetwork

# Download to current directory with same filename
await skillsnetwork.download_dataset(
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0103EN-SkillsNetwork/labs/Module%202/recipes.csv")
recipes = pd.read_csv("recipes.csv")
print("Data read into dataframe!") # takes about 30 seconds

recipes.head()

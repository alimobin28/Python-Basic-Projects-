# Country Categorical Analysis
# Dataset: Create a Series of countries with frequency counts (like USA, UK, Pakistan, etc.)

# Practice:

# Convert to categorical Series.

# Count frequency of each country.

# Add/remove a country.

# Use .value_counts() and .append()

import pandas as pd

country = ["Aus","USA","Albania","Pakistan","Greenland","USA","Pakistan","India"]

s2 = pd.Series(country,dtype = "category")
print(s2)

print("\n Country Frequency:\n", s2.value_counts())

s2 = s2.cat.add_categories("UAE")
print("\n New Categories after Adding 'UAE':", s2.cat.categories)
#s2 = s2.append(pd.Series(["UAE"],dtype="category")).astype("category")
#s2 = s2.append(pd.Series(["UAE"], dtype="category")).astype("category")
print("\n Country Frequency:\n", s2.value_counts())

s2 = s2.cat.remove_categories("Greenland")
print("\n New Categories after Adding 'Greenland':", s2.cat.categories)

print("\n Country Frequency:\n", s2.value_counts())
'''
this code is used to convert the ersstv5_sst.nc file 
to wide format csv file for checking the data. 
it only converts data from 1910 to 2019.
'''

import xarray as xr

ds = xr.open_dataset("ersstv5_sst.nc")
print(ds)
subset = ds["sst"].sel(time=slice("1910-01-01", "2010-12-31")).squeeze("lev", drop=True)

# Pivot dates into columns and keep (lat, lon) as rows
df_wide = subset.to_dataframe().dropna(subset=["sst"])["sst"].unstack(level="time")

# Format column headers cleanly as YYYY-MM-DD
df_wide.columns = df_wide.columns.strftime("%Y-%m-%d")

df_wide.to_csv("sst_1910_2010_wide.csv")
print(f"Saved {df_wide.shape[0]:,} locations x {df_wide.shape[1]:,} months.")
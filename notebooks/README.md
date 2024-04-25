## EDA analysis

Summary Statistics: Calculate the mean, median, standard deviation, and
other statistical measures for each numeric column to understand data
distribution.
Data Quality Check: Look for missing values, outliers, or incorrect entries
(e.g., negative values where only positive should exist), especially in
columns like GHI, DNI, and DHI.
Time Series Analysis: Analyze how variables like GHI, DNI, DHI, and Tamb
change over time. You can plot these metrics across the 'Timestamp' to
identify patterns or anomalies.
Correlation Analysis: Determine the correlation between different
variables like solar radiation components (GHI, DHI, DNI) and temperature
measures (TModA, TModB) to uncover relationships.
Wind Analysis: Explore wind speed (WS, WSgust, WSstdev) and wind
direction (WD, WDstdev) data to identify any trends or notable wind
events.
Temperature Analysis: Compare module temperatures (TModA, TModB)
with ambient temperature (Tamb) to see how they are related or vary
under different conditions.
Histograms: Create histograms for variables like GHI, DNI, DHI, WS, and
temperatures to visualize the frequency distribution of these variables.
Box Plots: Use box plots to examine the spread and presence of outliers in
the solar radiation and temperature data.
Scatter Plots: Generate scatter plots to explore the relationships between
pairs of variables, such as GHI vs. Tamb, WS vs. WSgust, or any other
potentially interesting pairs.
Data Cleaning: Based on the initial analysis, clean the dataset by handling
anomalies and missing values, especially in columns like Comments which
appear entirely null.
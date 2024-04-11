# Given experimental value for Planck's constant from previous calculations
h_exp = 2.774120272049806e-34  # in J·s

# Tabulated value for Planck's constant
h_tab = 6.63e-34  # in J·s

# Calculate the percent difference between the experimental and tabulated values
percent_diff = abs((h_exp - h_tab) / h_tab) * 100

print(percent_diff)

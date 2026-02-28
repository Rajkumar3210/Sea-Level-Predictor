import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# ----------------------------
# Load Dataset
# ----------------------------
df = pd.read_csv('epa-sea-level-extended-2023.csv')
df = df.dropna()

# ----------------------------
# Linear Regression (All Data)
# ----------------------------
slope, intercept, r, p, std_err = linregress(
    df['Year'],
    df['CSIRO Adjusted Sea Level']
)

# ----------------------------
# Plot Historical Data
# ----------------------------
plt.figure(figsize=(12,6))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'],
            label='Data Points')

years_extended = range(1880, 2051)
sea_level_pred = slope * years_extended + intercept

plt.plot(years_extended, sea_level_pred,
         label='Best Fit Line (All Data)')

plt.title("Sea Level Rise Prediction")
plt.xlabel("Year")
plt.ylabel("Sea Level (inches)")
plt.legend()
plt.grid()

plt.savefig("sea_level_plot.png")
plt.show()

# ----------------------------
# Interactive Prediction Section
# ----------------------------

print("\n--- Sea Level Prediction Tool ---")

while True:
    user_input = input("Enter a future year to predict (or type 'exit'): ")

    if user_input.lower() == 'exit':
        print("Exiting prediction tool...")
        break

    try:
        year = int(user_input)

        if year < 1880:
            print("Year must be 1880 or later.")
            continue

        predicted_value = slope * year + intercept
        print(f"Predicted Sea Level in {year}: "
              f"{round(predicted_value, 2)} inches")

    except ValueError:
        print("Please enter a valid year.")
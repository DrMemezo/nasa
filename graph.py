import pandas as pd
import pathlib
import matplotlib.pyplot as plt

def show_graph_of(country="United States"):
# Read xlsx file
    path = pathlib.Path("filtered_output.xlsx")
    df = pd.read_excel(path, sheet_name="Sheet1")

    # Filter by country name
    country_data = df[df['country'] == country]

    # Drop Nan Values
    country_data = country_data.dropna(subset=['co2'])
    # Plot
    plt.figure(figsize=(10,8))
    plt.plot(country_data['year'], country_data['co2'], marker='o', linestyle='-', linewidth=1)


    plt.title(f"CO2 Emmisions of {country}")
    plt.xlabel('Year')
    plt.ylabel('CO2 Emissions/million tonnes')
    plt.grid(True)

    plt.tight_layout()
    plt.show()

if __name__=="__main__":
    show_graph_of()
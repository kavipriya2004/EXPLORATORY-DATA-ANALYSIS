import pandas as pd
import plotly.express as px

# Load the dataset (Replace 'covid_data.csv' with your actual dataset file)
df = pd.read_csv("covid_data.csv")

# Ensure proper date format
df['date'] = pd.to_datetime(df['date'])

# Aggregated global cases over time
cases_by_date = df.groupby('date')[['new_cases', 'new_deaths', 'new_vaccinations']].sum().reset_index()

# Line Chart: Global COVID-19 Trends
fig_cases = px.line(cases_by_date, x='date', y=['new_cases', 'new_deaths', 'new_vaccinations'],
                    labels={'value': 'Count', 'date': 'Date'},
                    title='Global COVID-19 Cases, Deaths, and Vaccination Trends')
fig_cases.show()

# Bar Chart: Total Vaccinations by Country
vaccination_by_country = df.groupby('location')['total_vaccinations'].max().reset_index()
vaccination_by_country = vaccination_by_country.dropna().sort_values(by='total_vaccinations', ascending=False).head(20)

fig_vaccination = px.bar(vaccination_by_country, x='location', y='total_vaccinations',
                          labels={'total_vaccinations': 'Total Vaccinations', 'location': 'Country'},
                          title='Top 20 Countries by Total Vaccinations',
                          color='total_vaccinations')
fig_vaccination.show()

# Choropleth Map: Total Cases by Country
latest_data = df[df['date'] == df['date'].max()]

fig_map = px.choropleth(latest_data, locations='iso_code', locationmode='ISO-3',
                         color='total_cases', hover_name='location',
                         title='Global COVID-19 Total Cases',
                         color_continuous_scale='Reds')
fig_map.show()

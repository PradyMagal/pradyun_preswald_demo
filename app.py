from preswald import text, plotly, connect, get_df, table, query, slider
import pandas as pd
import plotly.express as px


text("# Welcome to Pradyun's Example Project")
text("This is a simple example of using the `preswald` library to create a web app.")
text("Here, I will be visualizing International Education Costs via plots and tables.")
# Load the CSV
connect() # load in all sources, which by default is the sample_csv
df = get_df('sample_csv')

max_items = slider(
    label="Rows to Display",
    min_val=1,
    max_val=100,
    step=10,
    default=10
)

# Show the data
table(df, limit=max_items)

text("## I will now see what countries have the most expensive Masters programs average")

max_tuition_sql = "SELECT Country, AVG(Tuition_USD) as Avg_Tuition_USD FROM sample_csv WHERE Level = 'Master' GROUP BY Country ORDER BY Avg_Tuition_USD DESC"
max_tution_df = query(max_tuition_sql, "sample_csv")


# Plot filtered Data
fig = px.bar(max_tution_df, x='Country', y='Avg_Tuition_USD', title='Countries with Most exepnsive Masters Program')
plotly(fig)

most_number_sql = "SELECT Country, COUNT(*) as Number_of_Masters_Programs FROM sample_csv WHERE Level = 'Master' GROUP BY Country ORDER BY Number_of_Masters_Programs DESC"
most_number_df = query(most_number_sql, "sample_csv")

text("## Similarly, countries with the most number of masters programs are:")


# Plot filtered Data
fig = px.bar(most_number_df, x='Country', y='Number_of_Masters_Programs', title='Countries with Most Masters Programs')
plotly(fig)

text("## Lastly, lets compare rent with tuition in the US, lets see if there is a correlation")
# Filter the data for the US
us_sql = "SELECT Tuition_USD, Rent_USD FROM sample_csv WHERE Country = 'USA'"
us_df = query(us_sql, "sample_csv")

# # Plot the data
fig = px.scatter(us_df, x='Tuition_USD', y='Rent_USD', title='Tuition vs Rent in the US')
fig.update_traces(marker=dict(size=10, opacity=0.5, line=dict(width=2, color='DarkSlateGrey')),
                  selector=dict(mode='markers+text'))
plotly(fig) 

text("### Thanks for checking out my example project!")
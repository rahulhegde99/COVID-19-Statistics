import scrape
import pandas as pd

total_list, state_list, confirmed_list, recovered_list, death_list = scrape.scrape_now()

#state_stats has the data of each state in a single dataframe
state_stats = pd.DataFrame(list(zip(state_list,confirmed_list,death_list,recovered_list)),
                            columns=['State','Confirmed','Deaths','Recovered'])

#states with highest confirmed cases are ordered first(resets index after sorting)
state_stats = state_stats.sort_values(by='Confirmed', ascending=False).reset_index(drop=True)

#top 10 is choosed
top_state_stats = state_stats.head(10)

#convert the processed dataframe to list to be fed into the graph
state_list = top_state_stats['State'].values.tolist()
confirmed_list = top_state_stats['Confirmed'].values.tolist()
death_list = top_state_stats['Deaths'].values.tolist()
recovered_list = top_state_stats['Recovered'].values.tolist()

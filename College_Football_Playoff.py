#!/usr/bin/env python
# coding: utf-8

# In[5]:


import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as md
import matplotlib.ticker as ticker
import numpy as np
import plotly.express as px
import altair as alt
st.set_page_config(page_title="College Football Playoff", layout="wide",initial_sidebar_state="collapsed")
st.title('College Football Playoff Trophy')

# In[20]:


st.markdown('The College Football Playoff National Championship Trophy is the trophy awarded to the winner of the College Football Playoff (CFP), the postseason tournament in American college football that determines a national champion for the NCAA Division I Football Bowl Subdivision (FBS) [1](https://en.wikipedia.org/wiki/College_Football_Playoff_National_Championship_Trophy).')

st.markdown('College Football Playoff officials commissioned the trophy for the new playoff system, preferring a new award that was unconnected with the previous Bowl Championship Series (BCS) postseason system which was sometimes controversial.')

# In[5]:


st.markdown('The intention of this analysis is to provide information about how the College Footbal Playoff 2022 evolved considering metrics such as:') 
st.write('- Teams')
st.write('- Points')
st.write('- Interceptions')
st.write('- Touchdowns')
st.write('- Turnovers')
st.write('- Passes and rushes')
st.write('- Rushing and passing yards')
st.write('')


# In[10]:

df = pd.read_excel(r'docs\offchain_football_1.xlsx')
df2 = pd.read_excel(r'docs\offchain_footbal_2.xlsx')

# In[22]:

st.subheader('College Football Playoff')
st.write('The first part of this app analyzes the first games between top 4 teams over the current season, which have been Ohio State University, the University of Georgia, Texas Christian University, and the University of Michigan. These 4 teams plays between them to take road to the final match. These period is called as College Football Playoff.')
st.write('In this season, the playoff matches have been Texas - Michigan and Ohio State - Georgia. The metrics to be analyzed from there are:')
st.write('- Points won by each team')
st.write('- Interceptions won by each team')
st.write('- Turnovers by each team')
st.write('- Passes done by each team')
st.write('- Rushes completed by each team')
st.write('- Rushing vs passing yards by each team')
st.write('- Touchdowns per team')
st.write('')

import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Create figure with secondary y-axis
fig1 = make_subplots(specs=[[{"secondary_y": True}]])

fig1.add_trace(go.Bar(x=df['team'],
                y=df['points'],
                name='total points',
                marker_color='rgb(163, 203, 249)'
                , yaxis='y'))

fig1.update_layout(
    title='Team points won',
    xaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)


# Create figure with secondary y-axis
fig2 = make_subplots(specs=[[{"secondary_y": True}]])

fig2.add_trace(go.Line(x=df['team'],
                y=df['interceptions'],
                name='# interceptions',
                marker_color='rgb(163, 203, 249)'
                , yaxis='y'))
fig2.add_trace(go.Line(x=df['team'],
                y=df['turnovers'],
                name='# turnovers',
                marker_color='rgb(11, 78, 154)'
                , yaxis='y2'))

fig2.update_layout(
    title='Interceptions vs Turnovers by team',
    xaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)



st.plotly_chart(fig1, theme="streamlit", use_container_width=True)
st.plotly_chart(fig2, theme="streamlit", use_container_width=True)

col1,col2=st.columns(2)
with col1:
    st.altair_chart(alt.Chart(df)
    .mark_line()
    .encode(x='team:N', y='passes:Q',color='team')
    .properties(title='Completed passes by team'))

col2.altair_chart(alt.Chart(df)
    .mark_line()
    .encode(x='team:N', y='rushes:Q',color='team')
    .properties(title='Completed rushes by team'))


# Create figure with secondary y-axis
fig2 = make_subplots(specs=[[{"secondary_y": True}]])

fig2.add_trace(go.Line(x=df['team'],
                y=df['rushing yards'],
                name='# yards',
                marker_color='rgb(163, 203, 249)'
                , yaxis='y'))
fig2.add_trace(go.Line(x=df['team'],
                y=df['passing yards'],
                name='# yards',
                marker_color='rgb(11, 78, 154)'
                , yaxis='y2'))

fig2.update_layout(
    title='Rushing vs Passing yards by team',
    xaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)
# Set y-axes titles
fig2.update_yaxes(title_text="Rushing yards", secondary_y=False)
fig2.update_yaxes(title_text="Passing yards", secondary_y=True)

st.plotly_chart(fig2, theme="streamlit", use_container_width=True)

fig3 = px.pie(df, values='touchdowns', names='team', title='Distribution of touchdowns by team')

st.plotly_chart(fig3, theme="streamlit", use_container_width=True)


# In[6]:


st.subheader('National Championship Game')
st.write('The second part of this app analyzes the final game between top 2 teams over the current season who passed the previous College Football Playoffs, which have been the University of Georgia and the University of Michigan. These 2 teams played the final match to win the National Championship Game.')
st.write('The metrics to be analyzed from there are:')
st.write('- Points won by each team')
st.write('- Interceptions won by each team')
st.write('- Turnovers by each team')
st.write('- Passes done by each team')
st.write('- Rushes completed by each team')
st.write('- Rushing vs passing yards by each team')
st.write('- Touchdowns per team')
st.write('')

# Create figure with secondary y-axis
fig1 = make_subplots(specs=[[{"secondary_y": True}]])

fig1.add_trace(go.Bar(x=df2['team'],
                y=df2['points'],
                name='total points',
                marker_color='rgb(163, 203, 249)'
                , yaxis='y'))

fig1.update_layout(
    title='Team points won',
    xaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)


# Create figure with secondary y-axis
fig2 = make_subplots(specs=[[{"secondary_y": True}]])

fig2.add_trace(go.Line(x=df2['team'],
                y=df2['interceptions'],
                name='# interceptions',
                marker_color='rgb(163, 203, 249)'
                , yaxis='y'))
fig2.add_trace(go.Line(x=df2['team'],
                y=df2['turnovers'],
                name='# turnovers',
                marker_color='rgb(11, 78, 154)'
                , yaxis='y2'))

fig2.update_layout(
    title='Interceptions vs Turnovers by team',
    xaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)



st.plotly_chart(fig1, theme="streamlit", use_container_width=True)
st.plotly_chart(fig2, theme="streamlit", use_container_width=True)

col1,col2=st.columns(2)
with col1:
    st.altair_chart(alt.Chart(df)
    .mark_line()
    .encode(x='team:N', y='passes:Q',color='team')
    .properties(title='Completed passes by team'))

col2.altair_chart(alt.Chart(df)
    .mark_line()
    .encode(x='team:N', y='rushes:Q',color='team')
    .properties(title='Completed rushes by team'))


# Create figure with secondary y-axis
fig2 = make_subplots(specs=[[{"secondary_y": True}]])

fig2.add_trace(go.Line(x=df2['team'],
                y=df2['rushing yards'],
                name='# yards',
                marker_color='rgb(163, 203, 249)'
                , yaxis='y'))
fig2.add_trace(go.Line(x=df2['team'],
                y=df2['passing yards'],
                name='# yards',
                marker_color='rgb(11, 78, 154)'
                , yaxis='y2'))

fig2.update_layout(
    title='Rushing vs Passing yards by team',
    xaxis_tickfont_size=14,
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15, # gap between bars of adjacent location coordinates.
    bargroupgap=0.1 # gap between bars of the same location coordinate.
)
# Set y-axes titles
fig2.update_yaxes(title_text="Rushing yards", secondary_y=False)
fig2.update_yaxes(title_text="Passing yards", secondary_y=True)

st.plotly_chart(fig2, theme="streamlit", use_container_width=True)

fig3 = px.pie(df, values='touchdowns', names='team', title='Distribution of touchdowns by team')
st.plotly_chart(fig3, theme="streamlit", use_container_width=True)


st.write('')
st.markdown('This app has been done by **_Adrià Parcerisas_**, a PhD Biomedical Engineer related to Machine Learning and Artificial intelligence technical projects for data analysis and research, as well as dive deep on-chain data analysis about cryptocurrency projects. You can find me on [Twitter](https://twitter.com/adriaparcerisas)')
st.write('')
st.markdown('The full sources used to develop this app can be found to the following link: [Github link](https://github.com/adriaparcerisas/College-Football-Playoff)')
st.markdown('_Powered by [Flipside Crypto](https://flipsidecrypto.xyz) and [MetricsDAO](https://metricsdao.notion.site)_')


# In[ ]:


# In[ ]:





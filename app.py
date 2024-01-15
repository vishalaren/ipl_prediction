import streamlit as st
import pickle
import pandas as pd
st.title('IPL WIN PREDICTOR')
teams=['Sunrisers Hyderabad',
 'Mumbai Indians',
 'Royal Challengers Bangalore',
 'Kolkata Knight Riders',
 'Kings XI Punjab',
 'Chennai Super Kings',
 'Rajasthan Royals',
 'Delhi Capitals']
cities=['Hyderabad', 'Mumbai', 'Indore', 'Kolkata', 'Bangalore', 'Delhi',
       'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
       'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Cuttack', 'Ahmedabad', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Ranchi', 'Abu Dhabi', 'Sharjah', 'Pune',
       'Raipur', 'Mohali', 'Bengaluru']
pipe = pickle.load(open("pipe.pkl","rb"))

col1,col2 = st.columns(2)

with col1:
    batting_teams = st.selectbox("select the batting team",sorted(teams))

with col2:
    bowling_teams = st.selectbox("select the bowling team",sorted(teams))

select_cities = st.selectbox("select the host city",sorted(cities))

targets = st.number_input("targets")

col3,col4,col5 = st.columns(3)

with col3:
    score = st.number_input('score')

with col4:
    overs = st.number_input('overs completed')

with col5:
    wickets = st.number_input('wickets')

if st.button('Preditct Proability'):
    runs_left = targets-score
    balls_left = 120 - overs*6
    wickets_left = 10- wickets
    crr = score/overs
    rrr = (runs_left*6)/balls_left
    
    input_df = pd.DataFrame({"batting_team":[batting_teams],"bowling_team":[bowling_teams],"city":[select_cities],
                             "run_left":[runs_left],"wicket_left":[wickets_left],"balls_left":[balls_left],
                            "total_runs_x":[targets],"crr":[crr],"rrr":[rrr]
                             })
    results = pipe.predict_proba(input_df)
    win = results[0][0]
    loss = results[0][1]
    st.text("batting team"+"-"+str(round(win*100))+"%")
    st.text("bolwing team"+"-"+str(round(loss*100))+"%")
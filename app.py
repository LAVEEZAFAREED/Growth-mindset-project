#sreamlit
import streamlit as st

st.set_page_config(page_title= "Growth Mindset Project", page_icon=":star:")
st.title("Growth Mindset Challenge App with Streamlit")

st.header("🚀 Welcome to Your Growth Journey! ")
st.writes("Embrace challenges,learn from mistakes,and unlock your full potentiol.")

#quote section
st.header(":stars: Today's Growth Mindset Quote")
st.write("Success is not final,failure is not fatal:its a courage to continue that counts.")

st.header("What's Your Challenge Today!")
user_input = st.text_input("Describe a challenge you're facing:")

#condition
if user_input:
     st.success(f"💪 You're facing: {user_input}. Keep pushing forward towards your goal!")
else:
     st.warning("Tell us about your challenge to get started!")

#reflecting
st.header("Reflect on your Learning")
reflection = st.text_area("Wriite your reflection here:")

if reflection:
     st.succes("✨Great Insight! Your reflection:{reflection}")
else:
     st.info("Reflecting on past experience help you grow! Start your difficulties")

#acheivements
st.header("Celebrate Your Wins!")
acheivement = st.text_input("Share something you've recently accomplished")

if acheivement:
     st.success("Amazing! You Acheived: {acheivement}")
else:
     st.info("Big or small , every acheivement counts! share one now")

#streamlit
import streamlit as st

st.set_page_config(page_title= "Growth mindset project" , page_icon=":star:")
st.ttitle("Growth Mindset Challenge App With Streamlit")

st.header("🚀 Welcome to Growth Journey !")
st.write("Embrace challenges, learn from mistakes,and unlock your full potential.This AL-powered app helps you build a growth mindset with reflection ,challenges,and acheivements!")

#quote section
st.header("💫Today  's  Growth Mindset Quote")
st.write("Sucess iss not final,failure is not fatal:it is the courage to continue that counts." -winston churchill)

st.header("💡What's Your Challenge Today?")
user_input = st.input("Describr a chalenge you're facing:")


#condition
if user_input:
     st.success(f"💪You're facing: {user_input}. Keep pushing forwaed towards your goal!🚀")
else:
     st.warning("Tell us about your challenge to get started!")

#reflexing
st.header("Reflect on your Learning")
reflection = st.text_area("Write Your reflection here: ")

if reflection:
     st.success(f"✨Great Insight! Your relection: {reflection} ")
else:
     st.info("Reflecting on past experience help you to grow! Share your difficuilties")

#acheivements
st.header("Celebrate Your wins!")
acheivements = st.text_input("Share something you've recentlty accomplished:")

if acheivement:
     st.success(f"🚀 Amazing! You acheived:
#footer
st.write("- - -")
st.write("🚀 Keep beleiving in yourself. Growth is a journey, not a destination! ")
st.writes("**⊝ Created by Laveeza Fareed**")


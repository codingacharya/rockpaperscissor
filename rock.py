import streamlit as st
import random

def get_winner(user_choice, ai_choice):
    if user_choice == ai_choice:
        return "It's a Tie!"
    elif (user_choice == "Rock" and ai_choice == "Scissors") or \
         (user_choice == "Paper" and ai_choice == "Rock") or \
         (user_choice == "Scissors" and ai_choice == "Paper"):
        return "You Win!"
    else:
        return "AI Wins!"

# Initialize session state
if 'wins' not in st.session_state:
    st.session_state.wins = 0
    st.session_state.losses = 0
    st.session_state.ties = 0

st.title("Rock-Paper-Scissors Game ✊📄✂️")

choices = ["Rock", "Paper", "Scissors"]
user_choice = st.radio("Choose your move:", choices, horizontal=True)

if st.button("Play!"):
    ai_choice = random.choice(choices)
    result = get_winner(user_choice, ai_choice)
    
    # Update scores
    if result == "You Win!":
        st.session_state.wins += 1
    elif result == "AI Wins!":
        st.session_state.losses += 1
    else:
        st.session_state.ties += 1
    
    st.subheader(f"AI chose: {ai_choice}")
    st.subheader(result)
    
    st.write("### Scoreboard:")
    st.write(f"✅ Wins: {st.session_state.wins}")
    st.write(f"❌ Losses: {st.session_state.losses}")
    st.write(f"🤝 Ties: {st.session_state.ties}")

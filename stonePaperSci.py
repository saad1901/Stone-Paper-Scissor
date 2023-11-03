import streamlit as st
import random
import time

session_state = st.session_state
if 'user' not in session_state:
    session_state.user = 0
if 'comp' not in session_state:
    session_state.comp = 0

choices = ["Stone", "Paper", "Scissor"]
rc = random.choice(choices)

st.title('Stone-Paper-Scissor Game')
st.text('developed by Mohammad Saad')

a, b, c = st.columns(3)
opt = a.radio('Select', ['Stone', 'Paper', 'Scissor'])
c.text('Computer Selected')
button1 = st.button('Play')

def choice(inp, rc):
    if (rc == "Stone"):
        rc1 = int(0)
    elif (rc == "Paper"):
        rc1 = int(1)
    elif (rc == "Scissor"):
        rc1 = int(2)
    else:
        st.error("Error and exited")
        exit()
    if (inp == "Stone"):
        inp1 = int(0)
    elif (inp == "Paper"):
        inp1 = int(1)
    elif (inp == "Scissor"):
        inp1 = int(2)

    if (m[inp1][rc1] == 0):
        time.sleep(0.3)
        b.subheader("Draw")

    elif (m[inp1][rc1] == 1):
        time.sleep(0.3)
        b.subheader("Win")
        st.balloons()
        session_state.user += 1
    else:
        time.sleep(0.3)
        b.subheader("Lost")
        session_state.comp += 1

m = [
    [0, 1, -1],
    [-1, 0, 1],
    [1, -1, 0]
]

if button1:
    c.subheader(f'{rc}')
    choice(opt, rc)

x, y, z, w = st.columns(4)
button2 = x.button('Reset Score')
if button2:
    session_state.user = 0
    session_state.comp = 0

y.subheader(f'Score: {session_state.user}')
z.subheader(f'{session_state.comp}')

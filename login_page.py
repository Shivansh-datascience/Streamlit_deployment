import streamlit as st


title = st.title("Basic Login Page ")
with title:
    st.text("Building an basic streamlit code for deployment into streamlit cloud")

#adding the user Login credential with username and password

#adding the username functinality
username = str(st.text_input("Enter your USername "))
if not isinstance(username, str):
    st.error("Invalid username")
else:
    if 'username' not in st.session_state:
        st.session_state['username'] = username
        st.write(f"You have entered {st.session_state['username']}")


#adding the password functionality
password = st.text_input("Enter your password")
if 'password' not in st.session_state:
        st.session_state['password'] = password
        st.write(f"You have entered {st.session_state['password']}")
 #storing the password into browser into cookies

#adding the submit button functionality
button = st.button("submit")
if button:
     st.write("Data has been submitted")
else:
     st.write("Incorrect data")             
import streamlit as st
import requests

def joke_generator():
    """"Fetch a random joke from the JokeAPI."""
    try:

        response = requests.get("https://official-joke-api.appspot.com/random_joke") 

        if response.status_code == 200:
            joke_data = response.json()
            return f"{joke_data["setup"]} \n \n {joke_data["punchline"]}"
        else:
            return "failed to fetch joke"
    except:
        return "When did you turnoff your computer last-time? \n \n programmer: maybe it's centuries 😂"

def main():
    st.title("Random Joke Generator")
    st.write("Click the button below to get a random joke!")

    if st.button("Get Joke"):
        joke = joke_generator()
        st.info(joke)
    st.write("This app fetches a random joke from the JokeAPI and displays it here.")
    st.write("_________")

    st.markdown(
        """
        <div style="text-align: center;">
        <p>build with 🧡 by <a href://github.com/vikram-singh9>Vikram</a></p>
        </div>

        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
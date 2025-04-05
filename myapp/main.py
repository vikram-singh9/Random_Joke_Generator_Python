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
    # Customizing the title and intro text for better aesthetics
    st.set_page_config(page_title="Random Joke Generator", page_icon="😂", layout="centered")
    
    st.markdown("""
    <style>
    .title {
        font-family: 'Helvetica', sans-serif;
        font-size: 40px;
        font-weight: 700;
        color: #4CAF50;
        text-align: center;
    }
    .description {
        font-size: 18px;
        color: #333;
        text-align: center;
        margin-bottom: 30px;
    }
    .button {
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        padding: 12px 24px;
        border-radius: 8px;
        border: none;
        transition: background-color 0.3s ease;
    }
    .button:hover {
        background-color: #45a049;
    }
    .footer {
        font-size: 16px;
        text-align: center;
        color: #777;
        margin-top: 40px;
    }
    .footer a {
        color: #4CAF50;
        text-decoration: none;
    }
    .footer a:hover {
        text-decoration: underline;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Title and description
    st.markdown('<div class="title">Random Joke Generator</div>', unsafe_allow_html=True)
    st.markdown('<p class="description">Click the button below to get a random joke!</p>', unsafe_allow_html=True)

    # Button to trigger joke fetch
    if st.button("Get Joke", key="joke_button", help="Click to get a random joke", use_container_width=True):
        joke = joke_generator()
        st.success(joke)

    # Information section
    st.markdown("""
    <p style="text-align: center; font-size: 16px; color: #333;">This app fetches a random joke from the JokeAPI and displays it here.</p>
    """, unsafe_allow_html=True)

    # Footer with link to GitHub
    st.markdown('<div class="footer">Built with 🧡 by <a href="https://github.com/vikram-singh9">Vikram</a></div>', unsafe_allow_html=True)
    
if __name__ == "__main__":
    main()

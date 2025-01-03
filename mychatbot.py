import nltk
import spacy
import streamlit as st
custom_css = """
<style>
body {
    background-color: lightblue;
    color: blue;
    font-family: 'Arial', sans-serif;
}
h1 {
    color: white;
}
.stButton>button {
    background-color:#4682b4;
    color: white;
    border-radius: 10px;
    border: white;
}
.stButton>button:hover {
    background-color: #5a9bd6;
}
</style>
"""

# Inject custom CSS
st.markdown(custom_css, unsafe_allow_html=True)
try:
    import spacy
    nlp = spacy.load("en_core_web_sm")
except ImportError:
    st.error("The spaCy library is not installed. Please install it using 'pip install spacy'.")
except OSError:
    st.error("The spaCy model 'en_core_web_sm' is not downloaded. Please download it using 'python -m spacy download en_core_web_sm'.")

def generate_response(user_input):
    if 'nlp' in globals():
        doc = nlp(user_input)
        if "hello" in user_input.lower():
            return "Hi there! Great to meet you!"
        elif "how are you" in user_input.lower():
            return "I'm just a bot, but I'm here to help you! How can I assist you today?"
        elif "what is your name" in user_input.lower():
            return "I'm your friendly chatbot! What's your name?"
        elif"will you be my friend?" in user_input.lower():
            return "Ofcourse, I am your true firend"
        elif"you are idiot" in user_input.lower():
            return "you are very bad...I am sadt"
        elif doc.ents:
            for ent in doc.ents:
                if ent.label_ == 'GPE':
                    return f"I see you're talking about {ent.text}!"
    return "Tell me more about that!"

def chatbot_ui():
    st.title("I am your cute Chatbot")
    st.image("https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/200e8d139737079.6234b0487404d.gif",width=300)

# Play a local audio file
    st.write("Hi there! How can I help you today?")

    # Get user input
    user_input = st.text_input("You:")

    if st.button("Send"):
        if user_input.lower() in ["exit", "quit"]:
            st.write("Goodbye!")
        else:
            response = generate_response(user_input)
            st.write(f"Chatbot: {response}")
    
if __name__ == "__main__":
    chatbot_ui()


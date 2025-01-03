
import random
import streamlit as st

# Custom CSS to change the background color
custom_css = """
<style>
body {
    background-color: lightblue;
    color: blue;
    font-family: 'Arial', sans-serif;
}
h1 {
    color: lightblue;
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

# List of words
words = ['python', 'hangman', 'challenge', 'programming', 'developer','house','hello','smart','enjoy']

# List of hangman images for each stage
hangman_images = [
    "https://www.oligalma.com/downloads/images/hangman/hangman/2.jpg",
    "https://www.oligalma.com/downloads/images/hangman/hangman/3.jpg",
    "https://www.oligalma.com/downloads/images/hangman/hangman/4.jpg",
    "https://www.oligalma.com/downloads/images/hangman/hangman/5.jpg",
    "https://www.oligalma.com/downloads/images/hangman/hangman/6.jpg",
    "https://www.oligalma.com/downloads/images/hangman/hangman/7.jpg",
    "https://www.oligalma.com/downloads/images/hangman/hangman/8.jpg",
    "https://www.oligalma.com/downloads/images/hangman/hangman/9.jpg",
    "https://www.oligalma.com/downloads/images/hangman/hangman/10.jpg",
    
]

# Function to select a random word
def get_random_word(word_list):
    return random.choice(word_list)

# Function to display the current state of the word
def display_word(word, guessed_letters):
    display = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    return display

# Initialize session state variables
if 'word' not in st.session_state:
    st.session_state.word = get_random_word(words)
    st.session_state.guessed_letters = set()
    st.session_state.incorrect_guesses = 0
    st.session_state.max_incorrect_guesses = 8

# Streamlit app layout
st.title("Hangman Game")
st.write("Welcome to Hangman! Try to guess the word one letter at a time.")
# st.image(hangman_images[st.session_state.incorrect_guesses], width=100)
#st.image("https://www.bing.com/images/create/hangamn-only-6-diifeerent-steps-pictures-with-good/1-6777df650dfa4420ac053be1cba7fcb3?id=L1%2b9%2bU9pxnYH0EFOZQAFog%3d%3d&view=detailv2&idpp=genimg&thId=OIG3.H1bfqYr7YbNXc4Wr02RC&skey=mfFf-5J1EmEgcNPll57RCDYzdE3F27F2Kny7v1f_iuI&FORM=GCRIDP",width=200)
st.image("https://storage.googleapis.com/replit/images/1634525886031_c1df01e211975970acafd2db177ae190.gif",width=200)
# Display the current state of the word
current_display = display_word(st.session_state.word, st.session_state.guessed_letters)
st.write("Word: ", current_display)

# Input for guessing a letter
guess = st.text_input("Guess a letter: ").lower()

if st.button("Submit Guess"):
    if guess in st.session_state.guessed_letters:
        st.write("You already guessed that letter.")
    elif guess in st.session_state.word:
        st.session_state.guessed_letters.add(guess)
        st.write("Good guess!")
    else:
        st.session_state.guessed_letters.add(guess)
        st.session_state.incorrect_guesses += 1
        st.write(f"Incorrect guess. You have {st.session_state.max_incorrect_guesses - st.session_state.incorrect_guesses} guesses left.")

    # Display the updated state of the word
    current_display = display_word(st.session_state.word, st.session_state.guessed_letters)
    st.write("Word: ", current_display)
    st.image(hangman_images[st.session_state.incorrect_guesses], width=100)

    # Check for win/lose conditions
    if '_' not in current_display:
        st.success(f"Congratulations! You guessed the word: {st.session_state.word}")
        
    elif st.session_state.incorrect_guesses >= st.session_state.max_incorrect_guesses:
        st.error(f"Sorry, you ran out of guesses. The word was: {st.session_state.word}")
        
# Reset button to start a new game
if st.button("Start New Game"):
    st.session_state.word = get_random_word(words)
    st.session_state.guessed_letters = set()
    st.session_state.incorrect_guesses = 0
    st.session_state.max_incorrect_guesses = 8
    st.write("New game started!")
    st.image(hangman_images[0], width=100)

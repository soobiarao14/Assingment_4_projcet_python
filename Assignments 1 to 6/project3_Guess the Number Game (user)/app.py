

import streamlit as st
import random

def initialize_game(new_number=True):
    """Initialize or reset the game variables."""
    if new_number or "number" not in st.session_state:
        st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False

def check_guess(guess):
    """Check the user's guess and provide feedback."""
    if st.session_state.game_over:
        return

    st.session_state.attempts += 1

    if guess == 100:
        st.success("🎉 Congratulations! You guessed the correct number!")
        st.session_state.game_over = True
    elif guess < st.session_state.number:
        st.warning("📉 Too Low! Try again.")
    elif guess > st.session_state.number:
        st.warning("📈 Too High! Try again.")
    else:
        st.success(f"🎉 Congratulations! You guessed the number in {st.session_state.attempts} attempts!")
        st.session_state.game_over = True

def main():
    st.title("🎯 User Guess the Number Game")
    
    # Initialize the game state
    if "number" not in st.session_state:
        initialize_game()

    # Display current attempts
    st.write(f"🔢 **Attempts:** {st.session_state.attempts}")

    # User input for guessing
    guess = st.number_input("Enter your guess (1-100):", min_value=1, max_value=100, step=1)

    # Submit button
    if st.button("✅ Submit Guess", disabled=st.session_state.game_over):
        check_guess(guess)

    # Restart buttons
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🔄 Restart Game (New Number)"):
            initialize_game(new_number=True)
            st.rerun()

    # with col2:
    #     if st.button("♻ Restart Anytime (Keep Same Number)"):
    #         initialize_game(new_number=False)
    #         st.rerun()

if __name__ == "__main__":
    main()


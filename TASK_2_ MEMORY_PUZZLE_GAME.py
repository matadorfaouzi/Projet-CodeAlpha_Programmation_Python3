import streamlit as st  
import random  
import time  

# Function to generate pairs of cards  
def generate_cards(num_pairs):  
    cards = list(range(num_pairs)) * 2  # Create pairs  
    random.shuffle(cards)  # Shuffle cards  
    return cards  

# Function to display the game board  
def display_board(cards, flipped_indices, matched_indices):  
    cols = st.columns(4)  # 4 columns for the game area  
    for i in range(len(cards)):  
        if i in matched_indices:  
            cols[i % 4].button(f"{cards[i]}", key=f"card_{i}", disabled=True)  # Show matched cards  
        elif i in flipped_indices:  
            cols[i % 4].button(f"{cards[i]}", key=f"card_{i}", disabled=True)  # Show flipped cards  
        else:  
            cols[i % 4].button("?", key=f"card_{i}")  # Show hidden card  

# Main function to run the game  
def main():  
    st.title("Memory Puzzle Game")  

    if 'cards' not in st.session_state:  
        st.session_state.cards = generate_cards(8)  # Generate 8 pairs (16 cards)  
        st.session_state.flipped_indices = []  # Indices of flipped cards  
        st.session_state.matched_indices = []  # Indices of matched cards  
        st.session_state.time_left = 30  # Set time limit  
        st.session_state.start_time = time.time()  # Record start time  
        st.session_state.game_over = False  # Game state  

    # Check if the game is over  
    if st.session_state.game_over:  
        st.success("Congratulations! You've matched all cards!")  
        if st.button("Play Again"):  
            del st.session_state.cards  
            del st.session_state.flipped_indices  
            del st.session_state.matched_indices  
            del st.session_state.time_left  
            del st.session_state.start_time  
            del st.session_state.game_over  
            st.experimental_rerun()  
    else:  
        # Calculate time left  
        elapsed_time = time.time() - st.session_state.start_time  
        st.session_state.time_left = 30 - int(elapsed_time)  

        if st.session_state.time_left <= 0:  
            st.error("Time's up! Game Over!")  
            st.session_state.game_over = True  

        # Display the game board  
        display_board(st.session_state.cards, st.session_state.flipped_indices, st.session_state.matched_indices)  

        # Handle card clicks  
        for i in range(len(st.session_state.cards)):  
            if st.button("Flip", key=f"flip_{i}"):  
                if i not in st.session_state.flipped_indices and i not in st.session_state.matched_indices:  
                    st.session_state.flipped_indices.append(i)  

                # Check for matches  
                if len(st.session_state.flipped_indices) == 2:  
                    if (st.session_state.cards[st.session_state.flipped_indices[0]] ==  
                            st.session_state.cards[st.session_state.flipped_indices[1]]):  
                        st.session_state.matched_indices.extend(st.session_state.flipped_indices)  
                    time.sleep(1)  # Pause to show the flipped cards  
                    st.session_state.flipped_indices.clear()  # Reset flipped indices  

        # Check if all cards are matched  
        if len(st.session_state.matched_indices) == len(st.session_state.cards):  
            st.session_state.game_over = True  

        # Display time left  
        st.sidebar.write(f"Time left: {st.session_state.time_left} seconds")  

if __name__ == "__main__":  
    main()
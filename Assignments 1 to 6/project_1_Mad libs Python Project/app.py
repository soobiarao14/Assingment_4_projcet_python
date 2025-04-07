

import streamlit as st

# 🎭 Mad Libs Game using Streamlit

def mad_libs_game():
    st.set_page_config(page_title="Mad Libs Game", page_icon="🎭")
    
    # 🎨 Sidebar for input fields
    st.sidebar.title("📝 Fill in the Blanks")
    object1 = st.sidebar.text_input("📌 Enter an object:")
    verb1 = st.sidebar.text_input("🔧 Enter a verb:")
    adjective1 = st.sidebar.text_input("🎨 Enter an adjective:")
    place1 = st.sidebar.text_input("📍 Enter a place:")
    animal1 = st.sidebar.text_input("🐾 Enter an animal:")
    
    # 🏆 Main title
    st.title("🎭 Mad Libs Game")
    st.write("🎉 Create your own funny story by filling in the sidebar!")
    st.write("created by: sobiarao")
    
    # 🎬 Button to generate the story
    if st.sidebar.button("🚀 Generate Story"):
        if object1 and verb1 and adjective1 and place1 and animal1:
            story = f"One day, a {adjective1} {animal1} went to {place1}. It found a {object1} and decided to {verb1} with it. Everyone who saw it laughed and cheered! 😂"
            st.subheader("📖 Your Mad Libs Story:")
            st.write(story)
        else:
            st.warning("⚠️ Please fill in all the fields in the sidebar!")

if __name__ == "__main__":
    mad_libs_game()

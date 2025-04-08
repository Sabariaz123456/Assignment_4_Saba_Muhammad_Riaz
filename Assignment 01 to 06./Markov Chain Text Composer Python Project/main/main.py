import random
import streamlit as st
from streamlit.components.v1 import html

# Function to build the Markov chain from the input text
def build_markov_chain(text, n=1):
    words = text.split()
    markov_chain = {}
    
    for i in range(len(words) - n):
        key = tuple(words[i:i + n])
        next_word = words[i + n]
        if key not in markov_chain:
            markov_chain[key] = []
        markov_chain[key].append(next_word)
        
    return markov_chain

# Function to generate random text using the Markov chain
def generate_text(chain, n=1, max_words=50):
    key = random.choice(list(chain.keys()))
    output_words = list(key)
    
    for _ in range(max_words - n):
        if key not in chain:
            break
        next_word = random.choice(chain[key])
        output_words.append(next_word)
        key = tuple(output_words[-n:])
        
    return ' '.join(output_words)

# Streamlit UI
st.set_page_config(page_title="Markov Chain Text Composer", page_icon="🤖", layout="wide")
st.title("🧠 Markov Chain Text Composer 🤖")
st.markdown("""
    This application generates random text using the **Markov Chain** algorithm.
    You can upload your own text file or manually enter text to generate new, interesting content.
    """, unsafe_allow_html=True)

# Custom styling
html("""
<style>
    .css-1v3fvcr {
        padding: 2rem;
    }
    .css-1v3fvcr h1 {
        color: #4CAF50;
        font-size: 2.5rem;
    }
    .css-1v3fvcr p {
        font-size: 1.1rem;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 1.1rem;
        border-radius: 5px;
        border: none;
        padding: 10px 20px;
        transition: background-color 0.3s;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
</style>
""", height=0)

# File uploader
uploaded_file = st.file_uploader("📂 Upload a text file (txt format)", type=["txt"])

# Input text area for manual text entry
input_text = ""
if uploaded_file is not None:
    input_text = uploaded_file.read().decode("utf-8")
elif st.text_area("📝 Or type your text manually here:", height=200):
    input_text = st.text_area("📝 Or type your text manually here:", height=200)

# If input_text is provided (either file upload or manual input)
if input_text:
    # Show the first 300 characters of the uploaded text
    st.subheader("💬 Your Input Text:")
    st.write(input_text[:300] + "...")
    st.markdown("---")  # Divider for better UI

    # User selects the chain order
    chain_order = st.slider("🔢 Select the Markov Chain order (1 or 2)", 1, 2, 1)

    # User selects the number of words to generate
    num_words = st.slider("🔡 How many words to generate?", 10, 200, 50)

    # Build the Markov chain
    markov_chain = build_markov_chain(input_text, n=chain_order)

    # Generate Text Button
    if st.button("🚀 Generate Text"):
        with st.spinner("Generating text... please wait."):
            generated_text = generate_text(markov_chain, n=chain_order, max_words=num_words)
            st.subheader("🎉 Generated Text:")
            st.write(generated_text)

else:
    st.warning("Please upload a text file or enter some text to generate content!")
    
# Footer
st.markdown("---")
st.markdown("🧑‍💻 **Developed by You** | Powered by **Streamlit & Markov Chains**")




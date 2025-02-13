import streamlit as st
import requests

# Function to fetch AI response from the FastAPI backend
def get_ai_response(user_input):
    api_url = "http://127.0.0.1:3000/get_ans/invoke"

    payload = {
        "messages": [
            {
                "role": 'user',
                "content": user_input
            }
        ]
    }

    try:
        response = requests.post(api_url, json=payload, timeout=10)

        # Handle HTTP errors
        if response.status_code != 200:
            st.error(f"Error {response.status_code}: Unable to fetch response.")
            return None

        # Parse the JSON response
        response_data = response.json()

        # Extract AI response
        return response_data.get("content", "No response received.")

    except requests.exceptions.RequestException as e:
        st.error(f"Request error: {str(e)}")
        return None

# Streamlit UI
st.title("🤖 AI Chatbot")
st.write("Agent:Harry Potter")
st.markdown("Ask your AI assistant anything!")

# User input box
user_query = st.text_area("Enter your query:", height=100)

# Ask button
if st.button("Ask AI"):
    if user_query.strip():
        with st.spinner("Thinking... 🤔"):
            ai_response = get_ai_response(user_query)
            if ai_response:
                st.success("### 🤖 AI's Response")
                st.write(ai_response['messages'][1]['content'])
                
    else:
        st.warning("Please enter a query before asking.")

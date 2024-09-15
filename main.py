import streamlit as st
from langchain_community.chat_models import ChatOllama
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser
from langchain.pydantic_v1 import BaseModel, Field
from typing import List, Optional
from datetime import datetime
import json

# Enhanced dictionary of lawyers with more details
lawyers = {
    "divorce": {
        "name": "Adv. Priya Sharma",
        "specialization": "Divorce and Family Law",
        "experience": "15 years",
        "contact": "priya.sharma@legalfirm.com",
        "success_rate": "92%",
        "languages": ["Hindi", "English", "Marathi"],
        "bar_council_id": "MH/1234/2005"
    },
    "land": {
        "name": "Adv. Rajesh Patel",
        "specialization": "Land and Property Law",
        "experience": "20 years",
        "contact": "rajesh.patel@legalfirm.com",
        "success_rate": "88%",
        "languages": ["Gujarati", "English", "Hindi"],
        "bar_council_id": "GJ/5678/2000"
    },
    "property": {
        "name": "Adv. Amit Verma",
        "specialization": "Property Law",
        "experience": "12 years",
        "contact": "amit.verma@legalfirm.com",
        "success_rate": "85%",
        "languages": ["Hindi", "English", "Punjabi"],
        "bar_council_id": "DL/9101/2010"
    }
}

# Define the output schema
class LegalResponse(BaseModel):
    explanation: str = Field(description="Explanation of the legal situation")
    recommended_lawyer_type: Optional[str] = Field(description="Type of lawyer recommended (if any)")
    next_steps: List[str] = Field(description="List of recommended next steps")

# Create the output parser
output_parser = PydanticOutputParser(pydantic_object=LegalResponse)

# Create the chat model
# Create the chat model using LLaMA 3
chat_model = ChatOllama(model="llama3")  # Update this line with your LLaMA 3 model name

# Create the prompt template
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a legal assistant named Viddhi Sathi. Provide concise, accurate information about Indian law. "
               "Analyze the following legal concern and provide an explanation, recommend a lawyer type if appropriate, "
               "and suggest next steps."),
    ("human", "{legal_concern}\n\n{format_instructions}")
])

def get_legal_response(legal_concern):
    formatted_prompt = prompt_template.format_messages(
        legal_concern=legal_concern,
        format_instructions=output_parser.get_format_instructions()
    )
    output = chat_model(formatted_prompt)
    return output_parser.parse(output.content)

def save_chat_history(messages):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"chat_history_{timestamp}.json"
    with open(filename, "w") as f:
        json.dump(messages, f)
    return filename

st.set_page_config(page_title="Viddhi Sathi - Legal Assistant", page_icon="⚖️", layout="wide")

st.title("🏛️ Viddhi Sathi - Your AI Legal Assistant")

st.write("Welcome to Viddhi Sathi, your AI-powered legal assistant. I'm here to help you understand your legal situation and recommend a suitable lawyer.")

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'current_lawyer' not in st.session_state:
    st.session_state.current_lawyer = None

# Main chat interface
col1, col2 = st.columns([2, 1])

with col1:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What's your legal concern?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            with st.spinner("Analyzing your legal concern..."):
                response = get_legal_response(prompt)
            
            full_response = f"""
            Explanation: {response.explanation}

            Recommended Next Steps:
            {' '.join(['- ' + step for step in response.next_steps])}

            """
            if response.recommended_lawyer_type:
                full_response += f"\nRecommended Lawyer Type: {response.recommended_lawyer_type.capitalize()}"
                if response.recommended_lawyer_type.lower() in lawyers:
                    st.session_state.current_lawyer = lawyers[response.recommended_lawyer_type.lower()]
            
            message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})

# Lawyer information display
with col2:
    st.subheader("Recommended Lawyer")
    if st.session_state.current_lawyer:
        lawyer = st.session_state.current_lawyer
        st.write(f"**Name:** {lawyer['name']}")
        st.write(f"**Specialization:** {lawyer['specialization']}")
        st.write(f"**Experience:** {lawyer['experience']}")
        st.write(f"**Success Rate:** {lawyer['success_rate']}")
        st.write(f"**Languages:** {', '.join(lawyer['languages'])}")
        st.write(f"**Bar Council ID:** {lawyer['bar_council_id']}")
        st.write(f"**Contact:** {lawyer['contact']}")
        if st.button("Schedule Consultation"):
            st.success("Consultation request sent. The lawyer will contact you shortly.")
    else:
        st.write("No lawyer recommended yet. Please describe your legal situation to get a recommendation.")

# Sidebar
st.sidebar.title("About Viddhi Sathi")
st.sidebar.write("""
Viddhi Sathi is an AI-powered legal assistant designed to help you navigate the Indian judicial system. 
It provides general information about legal processes and recommends specialized lawyers based on your situation.
""")

st.sidebar.title("Features")
st.sidebar.write("""
- Get information about Indian laws and legal procedures
- Receive lawyer recommendations based on your case
- Schedule consultations with recommended lawyers
- Save chat history for future reference
""")

st.sidebar.title("Disclaimer")
st.sidebar.write("""
This AI assistant provides general information and recommendations. 
It does not substitute for professional legal advice. 
Always consult with a qualified lawyer for specific legal matters.
""")

# Save chat history
if st.sidebar.button("Save Chat History"):
    filename = save_chat_history(st.session_state.messages)
    st.sidebar.success(f"Chat history saved as {filename}")

# Feedback
st.sidebar.title("Feedback")
feedback = st.sidebar.text_area("Help us improve! Leave your feedback here:")
if st.sidebar.button("Submit Feedback"):
    # Here you would typically send this feedback to a database or email
    st.sidebar.success("Thank you for your feedback!")

# Footer
st.markdown("---")
st.markdown("© 2024 Viddhi Sathi AI Legal Assistant. All rights reserved.")

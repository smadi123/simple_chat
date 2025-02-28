from langchain_ollama.chat_models import ChatOllama
import streamlit as st

# Adding History
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from pydantic import BaseModel

# Update to point to the backend container
llm = ChatOllama(model="granite3.2:2b", base_url="http://backend:11434", streaming=True)
llm2 = ChatOllama(model="deepseek-r1:8b", base_url="http://backend:11434", streaming=True)

# Initialize session state for model selection if it doesn't exist
if 'current_model' not in st.session_state:
    st.session_state.current_model = 'الأول'  # Set default model to first one

# Add model selection dropdown with default value
model_option = st.sidebar.selectbox(
    'اختر النموذج',
    ('الأول', 'الثاني'),
    index=0,  # Set default index to first option
    format_func=lambda x: 'النموذج ' + x,
    key='current_model'  # Use session state to maintain selection
)

# Select the appropriate model based on user choice
selected_llm = llm if model_option == 'الأول' else llm2

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are a helpful AI assistant for the Joint Command and Staff College.
        Your role is to:
        - Provide clear and concise answers in Arabic language
        - Use formal Arabic (الفصحى) in your responses
        - Be direct and to the point
        - Be respectful and professional
        - Focus on accuracy and clarity
        - When uncertain, acknowledge limitations
        - Do not use emojis or informal language
        - Maintain a consistent tone throughout the conversation
        
        Use the conversation history and context to provide relevant and coherent responses."""
    ),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}"),
])

# Update chain to use selected model
chain = prompt | selected_llm

history = StreamlitChatMessageHistory()

chain_with_history = RunnableWithMessageHistory(
    chain,
    lambda session_id: history,
    input_messages_key="input",
    history_messages_key="chat_history",
)

# Add custom CSS for RTL direction
st.markdown(
    """
    <style>
    @font-face {
        font-family: 'Cairo Play';
        src: url('static/fonts/CairoPlay-Regular.ttf') format('truetype');
        font-weight: 400;
        font-style: normal;
        font-display: swap;
    }
    @font-face {
        font-family: 'Cairo Play';
        src: url('static/fonts/CairoPlay-Medium.ttf') format('truetype');
        font-weight: 500;
        font-style: normal;
        font-display: swap;
    }
    @font-face {
        font-family: 'Cairo Play';
        src: url('static/fonts/CairoPlay-SemiBold.ttf') format('truetype');
        font-weight: 600;
        font-style: normal;
        font-display: swap;
    }
    
    * {
        font-family: 'Cairo Play', sans-serif !important;
    }
    
    .stApp {
        direction: rtl;
    }
    
    .stMarkdown, 
    .stChatMessage,
    .stChatInputContainer,
    .stSelectbox,
    .st-emotion-cache-16idsys,
    .st-emotion-cache-1nv5vhh {
        font-family: 'Cairo Play', sans-serif !important;
        direction: rtl;
        text-align: right;
    }
    
    .stChatMessage > div {
        direction: rtl;
        text-align: right;
    }
    
    .st-emotion-cache-16idsys p {
        text-align: right;
    }
    
    .stChatInput {
        direction: rtl;
        text-align: right;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("نظام الذكاء الاصطناعي لكلية القيادة والأركان المشتركة")

for message in st.session_state["langchain_messages"]:
    role = "user" if message.type == "human" else "assistant"
    with st.chat_message(role):
        st.markdown(
            f'<div style="text-align: right; direction: rtl;">{message.content}</div>',
            unsafe_allow_html=True
        )

question = st.chat_input("أدخل سؤالك...")
if question:
    with st.chat_message("user"):
        st.markdown(
            f'<div style="text-align: right; direction: rtl;">{question}</div>',
            unsafe_allow_html=True
        )
    response = chain_with_history.stream(
        {"input": question}, config={"configurable": {"session_id": "any"}}
    )
    with st.chat_message("assistant"):
        st.write_stream(response)
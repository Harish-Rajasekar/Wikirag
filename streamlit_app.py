import streamlit as st

from src.rag_pipeline import RAGPipeline


# =====================================================
# Page Configuration
# =====================================================

st.set_page_config(
    page_title="WikiRAG",
    page_icon="📚",
    layout="wide"
)

# =====================================================
# Session State Initialization
# =====================================================

if "loaded" not in st.session_state:
    st.session_state.loaded = False

if "topic" not in st.session_state:
    st.session_state.topic = ""

if "rag" not in st.session_state:
    st.session_state.rag = RAGPipeline()

if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# =====================================================
# Sidebar
# =====================================================

with st.sidebar:

    st.title("⚙️ Settings")

    st.markdown("### 🤖 Model")
    st.info("Llama 3.3 70B (Groq)")

    st.markdown("### 📄 Knowledge Base")
    st.info("Wikipedia")

    st.divider()

    if st.button("🔄 Reset Session", use_container_width=True):

        st.session_state.loaded = False
        st.session_state.topic = ""
        st.session_state.messages = []
        st.session_state.rag = RAGPipeline()

        st.rerun()

    st.divider()

    st.markdown("### ℹ️ About")

    st.write(
        """
        WikiRAG is a Retrieval-Augmented
        Generation chatbot built using:

        - LangChain
        - ChromaDB
        - Sentence Transformers
        - Groq Llama 3.3
        - Streamlit
        """
    )

# =====================================================
# Main Page
# =====================================================

st.title("📚 WikiRAG Assistant")
st.write("Ask questions about any Wikipedia article.")

st.divider()

# =====================================================
# Topic Loader
# =====================================================

st.subheader("Wikipedia Topic")

col1, col2 = st.columns([4, 1])

with col1:

    topic = st.text_input(
        "",
        placeholder="Example: Lewis Hamilton"
    )

with col2:

    load_button = st.button(
        "📥 Load",
        use_container_width=True
    )

if load_button:

    if topic.strip() == "":

        st.warning("Please enter a Wikipedia topic.")

    else:

        with st.spinner("📚 Fetching Wikipedia article..."):

            try:

                st.session_state.rag.load_topic(topic)
                st.session_state.chat_history = []
                st.session_state.loaded = True
                st.session_state.topic = topic

                # Clear previous conversation
                st.session_state.messages = []

                st.success(f"Loaded '{topic}' successfully!")

            except Exception as e:

                st.error(str(e))

if st.session_state.loaded:

    st.success("✅ Article Loaded")

    st.caption(f"Current Topic: **{st.session_state.topic}**")

st.divider()

# =====================================================
# Chat History
# =====================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# =====================================================
# Chat Input
# =====================================================

prompt = st.chat_input(
    "Ask anything about the loaded article...",
    disabled=not st.session_state.loaded
)

if prompt:

    # -------------------------
    # Show User Message
    # -------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):

        st.markdown(prompt)

    # -------------------------
    # Generate Answer
    # -------------------------

    with st.spinner("🤖 Thinking..."):

        try:

            recent_history = st.session_state.chat_history[-5:]

            answer = st.session_state.rag.ask(
                prompt,
                recent_history
            )
            st.session_state.chat_history.append(
                {
                    "user": prompt,
                    "assistant": answer
                }
            )
        except Exception as e:

            answer = f"❌ {str(e)}"

    # -------------------------
    # Show Assistant Message
    # -------------------------

    with st.chat_message("assistant"):

        st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

st.divider()

st.caption(
    "Built with ❤️ using Streamlit, LangChain, ChromaDB and Groq."
)
import streamlit as st
from utils.pdf_parser import extract_text
from graph.workflow import build_graph

st.set_page_config(page_title="AI Research Analyzer", layout="wide")

st.title("📄 AI Research Paper Analyzer")
st.markdown("Upload a research paper and get structured insights using AI agents.")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:
    with st.spinner("📥 Extracting text from PDF..."):
        text, first_page = extract_text(uploaded_file)

    st.success("✅ Text extracted successfully!")

    if st.button("🚀 Analyze Paper"):
        graph = build_graph()

        progress = st.progress(0)
        status = st.empty()

        with st.spinner("🤖 Running AI Agents..."):

            status.text("📌 Extracting Metadata...")
            progress.progress(20)

            result = graph.invoke({
                "paper_text": text,
                "first_page": first_page
            })

            progress.progress(100)
            status.text("✅ Analysis Complete!")

        st.markdown("---")

        # 📌 METADATA
        st.header("📌 Paper Metadata")
        metadata = result.get("metadata", {})

        col1, col2 = st.columns(2)

        with col1:
            st.write(f"**Title:** {metadata.get('title', 'N/A')}")
            st.write(f"**Authors:** {metadata.get('authors', 'N/A')}")

        with col2:
            st.write(f"**Year:** {metadata.get('year', 'N/A')}")
            st.write(f"**Venue:** {metadata.get('venue', 'N/A')}")

        st.markdown("---")

        # 📊 ANALYSIS
        st.header("📊 Research Analysis")
        st.json(result.get("analysis"))

        st.markdown("---")

        # 📝 SUMMARY
        st.header("📝 Executive Summary")
        st.write(result.get("summary"))

        st.markdown("---")

        # 📚 CITATIONS
        st.header("📚 Citations & References")
        st.write(result.get("citations"))

        st.markdown("---")

        # 💡 INSIGHTS
        st.header("💡 Key Insights")
        st.write(result.get("insights"))
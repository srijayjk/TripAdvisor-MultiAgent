import streamlit as st
import tempfile
import requests
from src.builder import build_agents, build_tasks, render_yaml_template
from crewai import Crew
from langchain_community.llms import Ollama
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Trip Planner", layout="wide")
st.title("🌍 AI-Powered Trip Planner")

# Sidebar input
with st.sidebar:
    st.header("✈️ Trip Settings")
    country = st.text_input("Destination Country", "Japan")
    days = st.slider("Number of Days", 1, 30, 5)
    budget = st.selectbox("Budget", ["Budget", "Mid-range", "Luxury"])
    
    # Interactive location picker
    st.subheader("📍 Select on Map")
    m = folium.Map(location=[35.6895, 139.6917], zoom_start=4)
    map_data = st_folium(m, width=300, height=200)
    coords = map_data.get("last_clicked", {"lat": 35.6895, "lng": 139.6917})
    
    plan_button = st.button("🧠 Generate Plan")

if plan_button:
    with st.spinner("Running travel agents..."):
        from langchain_community.chat_models import ChatLiteLLM

        llm = ChatLiteLLM(
                model="ollama/llama3.2:3b",  # use your actual model path
                temperature=0.7
            )

        context = {"destination": country, "days": days, "budget": budget}
        config = render_yaml_template("config/agents_config.yaml", context)

        agents = build_agents(config, llm)
        tasks = build_tasks(config, agents)
        crew = Crew(agents=list(agents.values()), tasks=tasks, verbose=True)

        try:
            result = crew.kickoff()
            st.success("Trip plan ready!")
        except Exception as e:
            st.error(f"Error during planning: {e}")
            st.stop()

        st.session_state["trip_plan"] = result

        # Show images (Unsplash-like)
        st.image(
            f"https://source.unsplash.com/800x400/?{country},travel",
            caption=f"{country} Highlights",
            use_column_width=True,
        )

        st.subheader("🗓️ Daily Itinerary")
        days_text = days_text = result.output.split("Day ")
        if len(days_text) > 1:
            tabs = st.tabs([f"Day {i}" for i in range(1, len(days_text))])
            for i, tab in enumerate(tabs):
                with tab:
                    tab.markdown(f"**Day {i+1}**\n\n{days_text[i+1]}")
        else:
            st.markdown(result)

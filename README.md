# 🌍 TripAdvisor Multi-Agent Travel Planner
An AI-powered multi-agent application built using CrewAI, LangGraph, and Streamlit, enabling intelligent, personalized travel planning based on your budget, destination, and duration.



## ✨ Features
- 🧠 Multi-Agent Architecture: Specialized agents collaborate (Planner, Budgeter, Researcher, etc.)
- 🧳 Dynamic Travel Planning: Generates detailed itineraries based on user input
- 🗺️ Interactive Map Support: Visualizes destinations using folium
- 🧭 Daily Itinerary View: Tabs for each day, powered by intelligent day-splitting
- 🖼️ Place Images Integration: Pulls from Unsplash or Pixabay (optional)
- 📄 PDF Export: Save the trip plan as a printable document

## 📁 Folder Structure

bash 
```
TripAdvisor-MultiAgent/
├── config/
│   └── agents_config.yaml        # Agent/task definitions (templated)
├── src/
│   └── builder.py                # Builds agents/tasks from config
├── streamlite_app.py            # Streamlit frontend
├── main.py                      # CLI/main runner
└── README.md
```

## 🚀 Setup Instructions
1. Clone and create environment:

bash 
```
git clone https://github.com/your-username/TripAdvisor-MultiAgent.git
cd TripAdvisor-MultiAgent
conda create -n llm_env python=3.10
conda activate llm_env

```
2. Install dependencies:

bash 
```
pip install -r requirements.txt
```

bash
```
Make sure you have Ollama and LLaMA 3.2B running:
```

3. Run the app:

bash
```
streamlit run streamlite_app.py

```


## 📦 Dependencies
- CrewAI
- LangGraph
- Streamlit
- folium, streamlit-folium
- jinja2, PyYAML
- pdfkit (optional for PDF export)
- Ollama + LLaMA 3.2b


## 🤝 Contributions
Feel free to fork and contribute! Open an issue or PR with ideas for tools, destinations, or agent upgrades.

## 💡 Credits
Developed by Srijay Kolvekar, built with love for travel and open-source AI.


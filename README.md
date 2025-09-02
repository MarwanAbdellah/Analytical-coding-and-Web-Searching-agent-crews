# Analytical Coding and Web Searching Agent Crews

This repository implements an **Analytical Coding and Web Searching multi-agent system** using **CrewAI**. It is designed to perform **data analysis, coding tasks, and web-based information retrieval** through specialized agents.

---

``` Features ```
- **Multi-Agent Architecture** powered by [CrewAI](https://docs.crewai.com/)
- **Analytical Agent** for data analysis and insights
- **Coding Agent** for code generation and debugging
- **Web Searching Agent** for fetching relevant information from the internet
- **LLM Integration** for natural language understanding and generation
- **Extensible Tools** for file and directory reading, API usage, and more

---

``` Tech Stack ```
- **Python 3.10+**
- **CrewAI Framework**
- **Gemini API** (or any LLM supported by CrewAI)
- **WSL 2 / Docker (optional)** for containerized execution

---

``` Project Structure ```
```
analytical_coding_crew/
├── src/
│   ├── data/                   # Data files (e.g., stock prices)
│   ├── agents/                 # Agent definitions
│   ├── tasks/                  # Task configurations
│   └── main.py                 # Entry point
├── configs/                    # YAML configs for agents and tasks
├── README.md                   # Project documentation
└── requirements.txt            # Python dependencies
```

---

``` Installation ```

### 1. Clone the repository
```
git clone https://github.com/MarwanAbdellah/Analytical-coding-and-Web-Searching-agent-crews.git
cd Analytical-coding-and-Web-Searching-agent-crews
```

### 2. Create a virtual environment
```
python -m venv venv
source venv/bin/activate    # On Linux/Mac
venv\Scripts\activate       # On Windows
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

---

``` Environment Variables ```
Create a `.env` file in the root directory and set:
```
MODEL=gemini-pro
GEMINI_API_KEY=your_api_key_here
```

---

``` How to Run ```
Run the main crew process:
```
python -m analytical_coding_crew.src.main
```

---

``` Agents Overview ```
- **Analytical Agent**: Performs data analysis and generates reports.
- **Coding Agent**: Handles code writing, debugging, and optimization.
- **Web Searching Agent**: Fetches and processes information from online sources.

---

``` Tools Included ```
- **DirectoryReadTool** – Reads files from specified directories.
- **FileReadTool** – Reads individual files.
- **Custom Web Search** – For fetching real-time data.

---

``` Example Data ```
Sample stock prices in CSV format are included under:
```
analytical_coding_crew/src/data/Stock_prices/
```

---

``` Future Enhancements ```
- Add more specialized agents (e.g., visualization agent)
- Integrate with external APIs for financial and analytical data
- Support for real-time collaboration

---

``` License ```
This project is licensed under the MIT License.

---

``` Author ```
**Marwan Abdellah**  
[GitHub Profile](https://github.com/MarwanAbdellah)

---

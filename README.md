# ⚖️ Vidhi Saathi - AI Legal Assistant

Welcome to **Vidhi Saathi**, an AI-powered legal assistant designed to help users navigate the Indian judicial system. Vidhi Saathi provides general legal information, recommends specialized lawyers based on the case, and offers next steps for various legal concerns.

## 🚀 Features

- **Legal Analysis**: Analyzes legal concerns and provides a clear explanation.
- **Lawyer Recommendation**: Suggests specialized lawyers based on the type of legal issue.
- **Next Steps**: Provides actionable next steps to resolve the legal issue.
- **Consultation**: Easily schedule a consultation with recommended lawyers.
- **Multilingual Support**: Lawyer details include languages spoken, ensuring clear communication.
- **Save Chat History**: Save your chat history to revisit later.

## 🛠️ Tech Stack

- **Streamlit**: Used to build the interactive web app.
- **LangChain**: Provides the AI model connection and prompt handling.
- **Ollama**: Powers the LLaMA 3 model for generating legal responses.
- **Python**: Core programming language.
- **Pydantic**: For handling and validating AI model output.

## 📦 Installation

To get this project running locally, follow the steps below.

### Prerequisites

1. **Python 3.10+**
2. **Streamlit** and other required Python packages (listed in `requirements.txt`)
3. **Ollama** CLI for LLaMA 3 model

### Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/viddhi-sathi-legal-assistant.git
   cd viddhi-sathi-legal-assistant
2.Create a virtual environment and install dependencies:
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
  pip install -r requirements.txt
```
2.Install Ollama and ensure LLaMA 3 model is ready:
```bash
ollama pull llama-3
```


3.Run the Streamlit app:

```bash
streamlit run main.py
```
4.Open your browser and visit http://localhost:8501 to use the app.

## 🔧 How It Works

1. **Legal Concern Input**: Users type their legal concern into the chat interface.
2. **AI-Powered Response**: The app sends the input to the LLaMA 3 model via Ollama, which processes the input and provides:
   - A legal explanation
   - A recommendation for the type of lawyer
   - Next steps to take
3. **Lawyer Recommendation**: Based on the legal concern, a specialized lawyer from a predefined list is recommended.
4. **Consultation**: Users can schedule a consultation directly through the app.
# Example Lawyer Profile
```json
{
    "name": "Adv. Priya Sharma",
    "specialization": "Divorce and Family Law",
    "experience": "15 years",
    "success_rate": "92%",
    "languages": ["Hindi", "English", "Marathi"],
    "contact": "priya.sharma@legalfirm.com"
}
```
# ⚙️ Configuration
To modify the predefined list of lawyers or customize the system's logic, you can edit the dictionary inside main.py. Example:

```python
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
    ...
}
```
# 💡 Future Enhancements
Expand Lawyer Database: Add more categories and lawyer details.
Case Document Analysis: Allow users to upload documents for deeper analysis.
Chatbot: Enhance the chatbot for a more conversational user experience.

# 📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

# Talent Scout | Smart Hiring Assistant 🤖 
 

An AI-powered conversational chatbot that acts as a virtual recruiter, built using **Streamlit**, **LangChain**, and **Groq LLMs**. The bot conducts an interactive interview to collect and validate structured candidate information.






## 🚀 Features

- 💬 ChatGPT-style interface using `st.chat_input()` and `st.chat_message()`
- 📄 Collects candidate details:
  - Full Name
  - Email Address
  - Phone Number
  - Location
  - Tech Stack (languages, frameworks, tools)
- 🔁 Maintains memory using `RunnableWithMessageHistory`
- 🧠 Extracts structured data from natural responses
- 🧹 Handles empty LLM responses and reruns gracefully
- 🔄 Reset chat session with a single click

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit  
- **LLM Backend:** Groq (`mixtral-8x7b-32768`) via `langchain_groq`  
- **Memory:** LangChain + Streamlit session state  
- **Language:** Python 3.11+  
- **Prompting:** LangChain's `ChatPromptTemplate` + `MessagesPlaceholder`

---

## 📦 Installation

1. **Clone the repo:**
   ```bash
   git clone https://github.com/your-username/talent-assistant-chatbot.git
   cd talent-assistant-chatbot


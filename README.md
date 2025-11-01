🧠 Smart Data Extraction Bot

An AI-powered tool to extract and summarize website content with ease.
Built using Python, Streamlit, and Hugging Face Transformers, this app intelligently scrapes text from any webpage and generates concise or professional summaries using advanced AI models.

🌟 Overview

Smart Data Extraction Bot allows you to:

🔍 Extract meaningful content from any public webpage (blogs, news, research pages, etc.)

🧠 Automatically summarize extracted text using AI

🎨 Choose summary tone — Professional or Concise

💾 Export your results as PDF or Word (.docx) files

⚙️ Works seamlessly on static and JavaScript-rendered sites

🧩 Key Features
Feature	Description
Smart Web Scraper	Uses requests-html for JavaScript-rendered pages and BeautifulSoup4 for static ones.
AI Summarization	Integrates Hugging Face models for automatic summarization.
Dynamic Model Switching	Automatically selects model based on summary tone.
Streamlit UI	User-friendly interface for input, preview, and downloads.
PDF & DOCX Export	Easily save summaries as shareable documents.
Error Handling	Graceful fallbacks for failed requests and long text.
🧠 Technologies Used
Category	Tools / Libraries
Language	Python 3.9+
Framework	Streamlit
Web Automation	requests-html, BeautifulSoup4
AI/NLP	Hugging Face Transformers via huggingface_hub
Environment Handling	python-dotenv
Document Generation	reportlab (PDF), python-docx (DOCX)
Data Handling	Pandas
HTML Parsing	lxml, lxml_html_clean
📦 Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/<your-username>/smart-data-extraction-bot.git
cd smart-data-extraction-bot

2️⃣ Create and Activate a Virtual Environment
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate   # On Mac/Linux

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure Environment Variables

Create a file named .env in your project root and add your Hugging Face API Token:

HF_API_TOKEN=your_huggingface_access_token_here


Get a free API token here → https://huggingface.co/settings/tokens

5️⃣ Run the App
streamlit run app.py

6️⃣ Open in Browser

Streamlit will open automatically at:

http://localhost:8501

⚙️ Folder Structure
smart-data-extraction-bot/
│
├── app.py                 # Streamlit web interface
├── scraper.py             # Scraping and summarization logic
├── .env                   # Hugging Face API key
├── requirements.txt       # All dependencies
└── README.md              # Project documentation

📘 How It Works

Enter a URL → Paste any public webpage (news, research, article).

Extraction → The scraper retrieves and cleans all meaningful paragraph text.

Summarization → The AI model generates a clear and concise summary.

Download → You can export the summarized text as PDF or DOCX.

🧩 Summary Styles
Style	Model Used	Description
Professional	facebook/bart-large-xsum	Produces well-structured, formal summaries ideal for reports or documentation.
Concise	facebook/bart-large-cnn	Short, fact-based summaries perfect for quick overviews or briefs.
🧾 Export Options

Once the summary is generated, users can download it as:

📄 PDF file – Ready for printing or sharing

📝 Word (.docx) file – Editable and easy to reuse

🧠 Example Output

Input: Wikipedia: Artificial Intelligence

Professional Summary:

Artificial intelligence (AI) is a field of computer science concerned with creating systems capable of performing tasks that normally require human intelligence. It encompasses reasoning, learning, perception, and problem-solving.

Concise Summary:

AI enables machines to perform human-like cognitive functions such as learning and reasoning, forming the basis of modern automation and decision systems.

🧰 Requirements
streamlit
requests
requests-html
beautifulsoup4
huggingface_hub
python-dotenv
pandas
lxml
lxml_html_clean
reportlab
python-docx

🌐 Deployment Options

You can deploy this app easily on:

Streamlit Cloud → https://share.streamlit.io

Hugging Face Spaces → (supports Streamlit apps)

Vercel / Render → Python-based deployment supported

💡 Future Enhancements

🧠 Add multi-language summarization

🔗 Allow batch URL processing

📊 Add analytics dashboard for processed summaries

🌍 Integrate citation sources and keywords

👩‍💻 Author

VARI NAGA PUJITHA

💡 Passionate about AI, automation, and data-driven applications.

🪶 License

This project is released under the MIT License — feel free to use, modify, and share with proper credit.

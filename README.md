# Patient Sentiment and Adverse Effect Analysis

## Project Overview

I developed this project to analyze patient reviews and predict potential adverse effects of medications using advanced Machine Learning and Natural Language Processing (NLP) techniques. The system scrapes real-world patient reviews from platforms like Reddit and Drugs.com, analyzes their sentiment using BERT, and provides actionable insights such as side effect warnings and diet recommendations.

This web application serves as a comprehensive health companion, helping users understand their medications better and managing their health through AI-driven insights.

## Features

-   **Drug Analysis**: Enter a drug name to get a detailed report on its sentiment (positive/negative/neutral), common side effects, and a summarized review of patient experiences.
-   **Sentiment Analysis**: Utilizes `BERT` (Bidirectional Encoder Representations from Transformers) model to accurately gauge patient sentiment from unstructured text reviews.
-   **Adverse Effect Detection**: Scrapes and processes data to identify reported side effects that might not be prominently listed.
-   **Diet Recommendation**: Provides personalized diet plans based on the medication, side effects, and patient age.
-   **Prescription Analysis**: Upload a prescription image to analyze and digitize the information.
-   **Disease Prediction**: An AI-powered symptom checker to predict potential conditions based on user inputs.
-   **Virtual Doctor**: An interactive AI assistant to answer health-related queries.
-   **Authentication**: Secure login and registration/signup system using MongoDB.

## Technologies Used

-   **Backend**: Python, Flask
-   **Database**: MongoDB (Atlas)
-   **Machine Learning / AI**:
    -   PyTorch
    -   Transformers (Hugging Face BERT)
    -   Groq API (Llama3-8b for text generation)
    -   Scikit-learn / Pandas / NumPy
-   **Web Scraping**: BeautifulSoup, PRAW (Reddit API)
-   **Frontend**: HTML5, CSS3, JavaScript, Mockup UI designs
-   **Visualization**: AmCharts for interactive data visualization (Pie charts, Funnel charts).

## How It Works

1.  **Data Collection**: The app fetches live data from social platforms and medical forums.
2.  **Processing**: Threaded processes clean and tokenize the text.
3.  **Analysis**:
    -   Sentiment is classified using the pre-trained BERT model.
    -   Side effects are extracted or generated using Large Language Models (LLMs).
4.  **Presentation**: Results are displayed on a user-friendly dashboard with interactive charts and text-to-speech capabilities.

## Setup and Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/LuminarySam30/Patient-Sentiment-and-Adverse-Effect-Analysis.git
    cd Patient-Sentiment-and-Adverse-Effect-Analysis
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the application**:
    ```bash
    flask run
    ```
    Access the app at `http://localhost:5000` (or the port specified in the console).

## Key Files

-   `webapp.py`: Main Flask application entry point.
-   `GenAI.py`: Inteface for LLM interactions (Groq).
-   `SentimentAnalysis.py`: Core logic for BERT-based sentiment classification.
-   `ReviewExtraction.py` & `SideEffectThread.py`: Scrapers for data gathering.

---
*Developed by Samuel Jeromiah*

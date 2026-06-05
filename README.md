# PROJECT-AI-Based-Fake-News-Probability-Scoring-System
# Description 
#### The AI Based Fake News Probability Scoring System is a Python-based application designed to detect and classify news articles as REAL or FAKE using Machine Learning and Natural Language Processing techniques.
#### The project demonstrates the use of probabilistic scoring, dataset training, text preprocessing, MongoDB database integration, graphical visualization, and a user-friendly Tkinter GUI design.
#### This system is suitable for educational purposes, research projects, and media platforms where automated fake news detection and analysis are required.
# REPOSITORY STRUCTURE
  ```
 
 fake-news-probability-scoring-system/
│
├── assets/
│   ├── screenshots/
│   │   ├── home.png
│   │   ├── graph.png
│   │   └── dataset_loaded.png
│   └── logo.png
│
├── dataset/
│   └── news_dataset.csv
│
├── docs/
│   ├── project_report.pdf
│   └── presentation.pptx
│
├── src/
│   ├── main.py
│   ├── database.py
│   ├── predictor.py
│   ├── preprocessing.py
│   ├── visualization.py
│   └── utils.py
│
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
   ```
  
# Getting Started

## Prerequisites

Make sure the following are installed on your system:

* Python 3.x
* MongoDB
* Required Python Libraries:

  * tkinter
  * pandas
  * matplotlib
  * pymongo
  * openpyxl

## Installation

1. Clone the repository:

```bash
git clone <your-github-repo-link>
 

2. Navigate to the project folder:

```bash
cd fake-news-probability-scoring-system
```

3. Install required dependencies:

```bash
pip install pandas matplotlib pymongo openpyxl
```

4. Start MongoDB server on your system.

5. Run the project:

```bash
python main.py
```

## Usage

* Load the dataset file (.csv or .xlsx)
* Enter news text in the input box
* Click on **Analyze News**
* View prediction results and probability score
* Use Graph and Data buttons for visualization and stored records


📊 AI Content Impact Analysis
This project performs an end-to-end analysis of the Global AI Content Impact Dataset, evaluating how artificial intelligence is affecting industries, countries, jobs, and consumer trust. It includes data cleaning, exploratory data analysis, feature engineering, dimensionality reduction, and strategic visualization to derive actionable insights.

🧠 Overview
The objective of this project is to:

Explore trends in AI adoption, economic impact, job displacement, and consumer trust

Identify key factors contributing to successful AI integration

Analyze outliers and anomalies in the dataset

Provide strategic recommendations for policymakers, businesses, and developers

Deliver actionable visualizations for decision-making
📂 Project Structure
AI-Impact-Analysis/
│
├── ai_impact_analysis.ipynb   # Main Jupyter Notebook with code
├── data/
│   └── Global_AI_Content_Impact_Dataset.csv  # Raw dataset
├── outputs/
│   ├── cleaned_data.csv       # Cleaned version of the dataset
│   └── plots/                 # Directory for saved visualizations
├── README.md                  # This file
└── requirements.txt           # Python dependencies
🧾 Features
Data Cleaning & Preprocessing

Removes duplicates and null values

Converts data types

Encodes categorical variables

Exploratory Data Analysis (EDA)

Distribution plots

Correlation heatmaps

Industry-wise and country-wise trends

Outlier & Anomaly Detection

Z-score and IQR-based filtering

Visualization of anomalies

Feature Engineering

Aggregated metrics: Total_Impact_Score, Growth_Metric, etc.

Ranking of industries and countries

Dimensionality Reduction

PCA to identify dominant latent factors

Variance explained by principal components

Visualizations

Bar charts, pie charts, heatmaps, scatter plots, etc.

Top AI tools, job loss impact, adoption vs. trust graphs

Strategic Insights

Data-driven suggestions for policy and business leaders

📈 Key Metrics Defined
Total_Impact_Score: Weighted average of impact, adoption, and trust

Growth_Metric: Sum of Revenue_Impact and Productivity_Impact

AI_Tradeoff_Index: Ratio of growth vs. job loss

Anomaly_Flag: Marks statistically significant outliers
📊 Visual Output Samples
Top 10 AI Tools by impact score

AI Adoption vs Consumer Trust scatter plots

Industry Job Loss & Revenue Growth heatmaps

PCA Component Biplots showing feature influence

All plots are saved in /outputs/plots/ during execution.

📁 Dataset Description
Column	Description
Industry	Sector using AI
Country	Country name
AI_Tool	Name of AI application/tool
Adoption_Rate	% adoption in the industry
Revenue_Impact	AI’s effect on revenue
Productivity_Impact	% productivity increase
Job_Loss	% jobs lost to automation
Consumer_Trust	Trust index (0–100)
Regulatory_Index	Governance score (0–1)
Innovation_Score	R&D and AI innovation measure
Data_Privacy_Concern	Privacy concern level
Economic_Impact	Composite score of financial metrics

🧠 Insights Summary
High AI adoption industries tend to show greater productivity and revenue, but also higher job displacement

Consumer trust is positively correlated with regulatory strength and transparency

Retail and Manufacturing face the largest job disruption

Balanced AI adoption exists in countries with strong innovation and governance frameworks

💡 Strategic Recommendations
Invest in reskilling programs for job-affected sectors

Promote AI explainability and transparency to improve consumer trust

Enforce strong regulatory frameworks for ethical AI

Use custom AI adoption plans for each industry
📌 Dependencies
Add this in requirements.txt:
pandas
numpy
matplotlib
seaborn
scikit-learn
plotly

Install with:
pip install -r requirements.txt


import os
import requests
from dotenv import load_dotenv

class NewsScraperAgent:
    def __init__(self):
        self.api_key = os.getenv("NEWS_API_KEY")
        self.base_url = "https://newsapi.org/v2/everything"
        self.query = "Indian stock market"
    
    def get_top_20_companies(self):
        """
        This method will scrape news related to Indian stock market
        and suggest top 20 companies whose stock might be worth considering.
        """
        if not self.api_key:
            print("Error: NEWS_API_KEY is not set in the environment.")
            return None
        
        try:
            response = requests.get(self.base_url, params={
                'q': self.query,
                'apiKey': self.api_key,
                'pageSize': 100,
                'sortBy': 'relevancy'
            })
            if response.status_code == 200:
                news_data = response.json()
                articles = news_data.get("articles", [])
                
                # Extract company names from the news articles (this can be customized)
                companies = self.extract_companies_from_articles(articles)
                
                # Get top 20 companies
                top_20_companies = companies[:20]
                return top_20_companies
            else:
                print(f"Error: Failed to fetch news, status code: {response.status_code}")
                return None
        except Exception as e:
            print(f"Error while fetching news: {str(e)}")
            return None

    def extract_companies_from_articles(self, articles):
        """
        Placeholder function to extract company names from news articles.
        You can implement an NLP technique here to extract company names or use any relevant approach.
        """
        companies = []
        for article in articles:
            title = article.get("title", "")
            if "company" in title.lower():  # Simple keyword matching (replace with more sophisticated logic)
                companies.append(title.split()[0])  # Assuming the company name is the first word (can be changed)
        
        return companies

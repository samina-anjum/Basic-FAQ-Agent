```python
class FAQAgent:
    def __init__(self):
        self.name = "GrokFAQ"
        self.context = "You are a helpful FAQ bot created by xAI."
        self.faq_db = {
            "what is your name?": f"My name is {self.name}, a helpful FAQ bot created by xAI!",
            "what can you do?": "I can answer frequently asked questions about myself and my capabilities. Try asking about my purpose or features!",
            "who created you?": "I was created by xAI, a company working on building artificial intelligence to accelerate human scientific discovery.",
            "what is your purpose?": "My purpose is to assist users by providing accurate and helpful answers to common questions, making information easily accessible!",
            "how can you help me?": "I can help by answering your questions about my features, creators, or purpose. Just ask me anything from my FAQ list!"
        }
    
    def process_query(self, query):
        query = query.lower().strip()
        return self.faq_db.get(query, "Sorry, I don't have an answer for that. Try asking something like 'What is your name?' or 'What can you do?'")

# Test the FAQ agent
def test_faq_agent():
    agent = FAQAgent()
    test_queries = [
        "What is your name?",
        "What can you do?",
        "Who created you?",
        "What is your purpose?",
        "What's the weather like?"
    ]
    
    print("FAQ Agent Interactions:")
    print("-" * 30)
    for query in test_queries:
        print(f"Query: {query}")
        print(f"Response: {agent.process_query(query)}")
        print("-" * 30)

if __name__ == "__main__":
    test_faq_agent()
```
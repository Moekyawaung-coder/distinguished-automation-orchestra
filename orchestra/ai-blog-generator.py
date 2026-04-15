import ollama

def generate_senior_blog(topic: str) -> str:
    response = ollama.chat(model='llama3.2', messages=[{
        'role': 'user',
        'content': f"""You are a Distinguished Android Engineer named Moe Kyaw Aung.
        Write a 1200-word senior-to-distinguished level technical blog post about {topic}.
        Include real code examples, trade-off analysis, metrics, and senior insights.
        Use professional yet approachable tone."""
    }])
    return response['message']['content']

# Auto-generates new articles every week
if __name__ == "__main__":
    new_post = generate_senior_blog("Advanced Hybrid AI Routing at Global Scale")
    with open("distinguished-android-scale/blog/hybrid-ai-routing-2025.md", "w") as f:
        f.write(new_post
  )

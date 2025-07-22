# generator.py
# Author: Qawser Qayoom
# Description: AI-based Marketing Content Generator

import openai

# Set your API key here
openai.api_key = "YOUR_OPENAI_API_KEY"

def generate_marketing_post(product, occasion):
    prompt = f"""Create a high-conversion marketing post for the following:
    Product: {product}
    Occasion: {occasion}
    
    Format:
    1. Headline
    2. Caption with emojis
    3. 3 Hashtags
    4. Call-to-action
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=300
    )

    return response['choices'][0]['message']['content']

# Example usage
if __name__ == "__main__":
    product = input("Enter product name: ")
    occasion = input("Enter occasion: ")
    output = generate_marketing_post(product, occasion)
    print("\nGenerated Marketing Post:\n")
    print(output)

# src/load_model.py
from transformers import AutoModelForCausalLM, AutoTokenizer

# Specify the model name
model_name = 'scb10x/typhoon-7b'

# Load the model
model = AutoModelForCausalLM.from_pretrained(model_name)

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Print a success message
print("Model and tokenizer loaded successfully.")

def chat_with_model(prompt, max_length=50):
    # Encode the input prompt
    inputs = tokenizer(prompt, return_tensors='pt')

    # Generate a response
    outputs = model.generate(inputs['input_ids'], max_length=max_length, num_return_sequences=1)

    # Decode the generated tokens back to text
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

# Example usage
if __name__ == "__main__":
    while True:
        prompt = input("You: ")
        if prompt.lower() in ["exit", "quit"]:
            break
        response = chat_with_model(prompt)
        print(f"Model: {response}")
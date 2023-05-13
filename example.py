"""Example of using GPT model to build a simple ChatBot"""
import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel


# Load the GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')


def generate_response(user_input, model, tokenizer):
    """Define a function to generate responses"""
    # Tokenize the user input
    input_ids = tokenizer.encode(user_input, return_tensors='pt')
    # Generate a response from the model
    output = model.generate(input_ids=input_ids, max_length=1000, do_sample=True)
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response


while True:
"""Set up a loop to receive user input and generate responses"""
    user_input = input('You: ')
    response = generate_response(user_input, model, tokenizer)
    print('Bot:', response)

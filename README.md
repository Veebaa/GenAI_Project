# Generative AI Project
Building my first Generative AI tool. 

## What the AI will do:
Text Generation: To generate meaningful responses and maintain a conversation.
Code Generation: To generate or analyze code based on user input.
Conversational Flow: To handle dialogue contextually over multiple turns.

### Base Model:
Text Generation:
GPT-4o-mini: OpenAI's advanced language model, is used for text generation tasks.
Code Generation:
OpenAI Codex: Specialized in generating anf analyzing code.

### Development Environment:
Programming Language: Python (3.9+)
IDE: PyCharm
Framework: Flask

## Collect Training Data
Text Generation:
- Open datasets like Common Crawl, BooksCorpus, or Wikipedia.
- Focus on conversational datasets, e.g., Persona-Chat, ConvAI2.
Code Generation:
Datasets like The Stack (Hugging Face), CodeSearchNet, or GitHub repositories.

## Fine-Tune the Model
### Steps:
#### 1. Preprocessing:
- Tokenize text/code using Hugging Face Tokenizers.
- Use appropriate tokenization for code (e.g., preserving indentation).

#### 2. Fine-Tuning:
- Use a sequence-to-sequence approach for dialogue flow.
- For code, fine-tune on language-specific datasets using similar methods.

## Add Conversational Flow
To maintain context in conversations:
- Use a rolling buffer of dialogue history.
- Pass previous user inputs and AI responses as part of the input.

## Evaluate the Model
Text: Use metrics like BLEU, ROUGE, or perplexity.
Code: Check functionality by executing generated code snippets.

## Build and Test a Frontend
Use Flask to create a web-based interface for user interaction.

## Optimize for Utility
- Add tools like syntax highlighting for code output.
- Train the model to explain its decisions for research purposes.
- Ensure intuitive and responsive user experience in the frontend.
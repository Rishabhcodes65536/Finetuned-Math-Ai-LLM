# Finetuned-Math-Ai-LLM
This repository contains code for fine-tuning our favourite SOT i.e.Meta LLaMA-3 8B model using LoRA (Low-Rank Adaptation) on Google Colab. The setup includes mounting Google Drive to save checkpoints and ensuring efficient training using 4-bit quantization and half-precision floating-point operations.

## Features

- **Model**: Fine-tune [`unsloth/llama-3-8b-Instruct-bnb-4bit`](https://huggingface.co/unsloth/llama-3-8b-Instruct-bnb-4bit) model.
- **LoRA Configuration**: Customizable LoRA parameters for efficient adaptation.
- **Training**: Saves checkpoints directly to Google Drive, allowing resumption of training without losing progress due to Colab limits.
- **Inference**: Code to generate responses from the fine-tuned model.


##Setup
```bash
git clone https://github.com/Rishabhcodes65536/Finetuned-Math-Ai-LLM.git
```

##Usage

###Training
1.Open the Colab notebook and run the cells to mount Google Drive.
2.Run the training script.
3.Checkpoints will be periodically saved to your Google Drive.

###Inference
1.Load the best model checkpoint from Google Drive.
2.Use the provided inference script to generate responses.

##Acknowledgements
This repository is inspired by the work of [Unsloth peft for Meta Llama-3-8b](https://github.com/unslothai/unsloth)
[Hugging Face](https://huggingface.co) for fetching base model as well as storing the fine-tuned model
[Google Colab](https://colab.research.google.com) for Your Free Computing Units for Training as well as Inference


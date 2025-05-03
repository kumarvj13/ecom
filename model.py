from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch

model_name = "google/flan-t5-base"

# Load model and tokenizer with weights
tokenizer = T5Tokenizer.from_pretrained("t5-small", legacy=False)
model = T5ForConditionalGeneration.from_pretrained("t5-small")
# tokenizer = T5Tokenizer.from_pretrained(model_name)
# model = T5ForConditionalGeneration.from_pretrained(model_name)  # DO NOT pass device_map or low_cpu_mem_usage here

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)

def generate_insight(prompt: str) -> str:
    try:
        input_ids = tokenizer.encode(prompt, return_tensors="pt", truncation=True, max_length=2512).to(device)
        with torch.no_grad():
            outputs = model.generate(input_ids, max_length=1300, num_beams=4, early_stopping=True)
        return tokenizer.decode(outputs[0], skip_special_tokens=True)
    except Exception as e:
        return f"Error generating insight: {str(e)}"

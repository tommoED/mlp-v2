import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, 
 
torch.random.manual_seed(0)

model_path = "microsoft/Phi-4-mini-instruct"

model = AutoModelForCausalLM.from_pretrained(
    model_path,
    device_map="auto",
    torch_dtype="auto",
    trust_remote_code=True,
)
tokenizer = AutoTokenizer.from_pretrained(model_path)


from peft import get_peft_model, LoraConfig, TaskType

peft_config = LoraConfig(
    task_type=TaskType.CAUSAL_LM,
    r=32,
    lora_alpha=64,
    lora_dropout=0.1,
    bias="none",
    target_modules=["q_proj", "v_proj"],
)

model = get_peft_model(model, peft_config)


print(model.device)

def tokenize_example(example):
    instruction = example["instruction"]
    response = example["response"]

    # Concatenate the instruction and response, using a separator.
    text = instruction + "\n" + response

    output = tokenizer(text, truncation=True, max_length=max_length, padding="max_length")
    labels = output["input_ids"].copy()

    # Obtain the tokenized instruction length (without special tokens if needed)
    instruction_token_len = len(tokenizer(instruction, add_special_tokens=False)["input_ids"])
    
    # Mask the instruction tokens so loss is computed only on the response
    labels[:instruction_token_len] = [-100] * instruction_token_len

    output["labels"] = labels
    return output


from datasets import load_dataset
from transformers import AutoTokenizer

# Load the dataset from the JSONL file
dataset = load_dataset("json", data_files={"train": "..\\data\\finetuning_dataset-v4.jsonl"})

# Apply tokenization
tokenized_dataset = dataset.map(tokenize_example)

# Split into train and validation
split_dataset = tokenized_dataset.train_test_split(test_size=0.1)

train_dataset, validation_dataset = split_dataset["train"], split_dataset["test"]






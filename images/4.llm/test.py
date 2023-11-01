import torch
import transformers
import accelerate
import datasets
import evaluate
import peft

print("Cuda devices")
for i in range(torch.cuda.device_count()):
    print(f"[{i}]: {torch.cuda.get_device_name(i)}")

print("Versions")
print("cuda:", torch.version.cuda)
print("torch:", torch.__version__)
print("transformers:", transformers.__version__)
print("datasets:", datasets.__version__)
print("peft:", peft.__version__)


import torch
import lightning

print("Cuda devices")
for i in range(torch.cuda.device_count()):
    print(f"[{i}]: {torch.cuda.get_device_name(i)}")

print("Versions")
print("cuda:", torch.version.cuda)
print("torch:", torch.__version__)
print("lightning:", lightning.__version__)


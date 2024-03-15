import torch

if not torch.backends.mps.is_available():
    if not torch.backends.mps.is_built():
        print("MPS недоступен, поскольку текущая установка PyTorch не была «построена с включенным MPS.")
    else:
        print("MPS недоступен, поскольку на этом компьютере нет устройства с поддержкой MPS.")

else:
    print("Все ok")
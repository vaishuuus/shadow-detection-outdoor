## Threshold Tuning Summary

### Experiment 1 — V threshold range
- V=80: mean IoU = 0.1998
- V=100: mean IoU = 0.3800
- V=120: mean IoU = 0.4535

### Experiment 2 — Fine tuning around V=120
- V=105: mean IoU = 0.4116
- V=110: mean IoU = 0.4318
- V=115: mean IoU = 0.4452
- V=120: mean IoU = 0.4535
- V=125: mean IoU = 0.4610
- V=130: mean IoU = 0.4629
- V=135: mean IoU = 0.4624

### Experiment 3 — S lower threshold
- S_lower=0: mean IoU = 0.4053
- S_lower=15: mean IoU = 0.5108
- S_lower=30: mean IoU = 0.3134
- S_lower=45: mean IoU = 0.1239

### Experiment 4 — LAB vs HSV
- Best HSV (V=130): 0.4629
- Best LAB (L=120): 0.4983

### Final choice: HSV V≤130  S≥15

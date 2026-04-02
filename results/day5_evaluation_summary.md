## Evaluation Results — ISTD Test Set

**Method:** HSV colour space  | V ≤ 130  | S ≥ 15

**Dataset:** ISTD  | 540 test images

| Metric | Mean | Median | Std |
|--------|------|--------|-----|
| IoU (↑) | 0.6733 | 0.7944 | 0.3046 |
| F1 (↑)  | 0.7572 | 0.8855 | 0.2647 |
| BER (↓) | 11.62 | 5.87 | 12.46 |

| Images with IoU > 0.5 | 383 / 540 |
| Images with IoU > 0.7 | 308 / 540 |

### Comparison with grayscale baseline

| Method | IoU | F1 | BER |
|--------|-----|----|-----|
| Grayscale threshold | 0.4911 | 0.5974 | 22.61 |
| HSV (ours) | 0.6733 | 0.7572 | 11.62 |

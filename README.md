# link_khovanov
solve khovanov for link for both directions of each component.

## Install

```bash
pip install link-khovanov
```

## Usage

```python
import link_khovanov

pd_code = [[10, 1, 11, 2], [12, 3, 13, 4], [14, 19, 15, 20], [18, 7, 19, 8], [16, 5, 17, 6], [4, 15, 5, 16], [6, 17, 7, 18], [20, 13, 9, 14], [2, 9, 3, 10], [8, 11, 1, 12]]

for idx, line in enumerate(link_khovanov.link_khovanov(pd_code)):
    print(f"{idx:02d}", line, "\n")
```

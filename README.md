
# Rami's Matplotlib Utilities

Those are a bunch of opinionated `matplotlib` plotting utilities tailored for my own needs.

## Installation

```sh
pip install git+https://github.com/Rami-Sabbagh/mpl-utils.git@1.0.0
```

## Styles Usage

```py
import matplotlib.pyplot as plt
plt.style.use('mpl_utils.styles.default')
```

**Available styles:** `default` only.

## Development

- Install Poetry and Python 3.12+
- Clone repository locally.
- Install dependencies: `poetry install`.
- Start a shell with the `venv` activated: `poetry shell`.

## Testing

Simply run `pytest` at the root of the repo, with the `venv` activated.
Or using `poetry run pytest`.


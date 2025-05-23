# Codex Example

This repository demonstrates a simple system for selecting an AI model based on
a quality-to-price ratio. The `ai_selector.py` module defines an `AIModel`
class and a helper function `select_best_model` that chooses the most cost-
effective model for a given task.

## Usage

Run `ai_selector.py` directly to see an example of selecting a model:

```bash
python ai_selector.py
```

## Testing

Tests are located in the `tests/` directory and can be run with `pytest`:

```bash
pytest -q
```


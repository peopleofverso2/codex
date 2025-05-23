from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class AIModel:
    """Represents an AI model with a quality score and cost."""
    name: str
    quality_score: float  # Higher is better
    cost_per_query: float  # Example: USD per request
    tasks: List[str] = field(default_factory=list)

def select_best_model(models: List[AIModel], task: str) -> Optional[AIModel]:
    """Select the best model for a given task based on quality/cost ratio.

    Args:
        models: Available models.
        task: Task for which a model is needed.

    Returns:
        The model with the highest quality to cost ratio that supports the task,
        or None if no model supports the task.
    """
    best_model = None
    best_ratio = float('-inf')
    for model in models:
        if task in model.tasks and model.cost_per_query > 0:
            ratio = model.quality_score / model.cost_per_query
            if ratio > best_ratio:
                best_ratio = ratio
                best_model = model
    return best_model

if __name__ == "__main__":
    available_models = [
        AIModel(name="ModelA", quality_score=85.0, cost_per_query=0.02, tasks=["text", "image"]),
        AIModel(name="ModelB", quality_score=92.0, cost_per_query=0.05, tasks=["text"]),
        AIModel(name="ModelC", quality_score=70.0, cost_per_query=0.01, tasks=["image"]),
    ]

    task_name = "text"
    best = select_best_model(available_models, task_name)
    if best:
        print(f"Best model for {task_name}: {best.name}")
    else:
        print(f"No model supports the task: {task_name}")


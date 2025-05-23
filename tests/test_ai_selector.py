import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pytest
from ai_selector import AIModel, select_best_model

def test_select_best_model_basic():
    models = [
        AIModel(name='A', quality_score=80, cost_per_query=0.05, tasks=['text']),
        AIModel(name='B', quality_score=90, cost_per_query=0.10, tasks=['text', 'image'])
    ]
    best = select_best_model(models, 'text')
    assert best.name == 'A'


def test_no_model_for_task():
    models = [AIModel(name='A', quality_score=80, cost_per_query=0.05, tasks=['text'])]
    assert select_best_model(models, 'image') is None


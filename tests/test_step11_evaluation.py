import os
import json
import pytest

def test_evaluation_dataset_exists_and_valid():
    dataset_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "evaluation", "datasets", "rag_eval_questions.json"
    )
    assert os.path.exists(dataset_path), "Evaluation dataset is missing."
    
    with open(dataset_path, "r") as f:
        data = json.load(f)
        
    assert isinstance(data, list)
    assert len(data) == 100, f"Expected 100 questions, got {len(data)}"
    
    for q in data:
        assert "id" in q
        assert "question" in q
        assert "category" in q
        assert "department_context" in q
        assert "expected_source_document_ids" in q
        assert "expected_grounded" in q

import os
import sys
import json
import random

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.connection import SessionLocal
from database.models import Document, DocumentChunk

def generate_dataset():
    questions = []
    
    with SessionLocal() as db:
        # Fetch 100 documents of various types to create questions
        chunks = db.query(DocumentChunk).limit(500).all()
        
        # Try to find FAQs
        faqs = [c for c in chunks if "question:" in c.content.lower() or "faq" in str(c.chunk_metadata.get("title", "")).lower()]
        
        # Process FAQs
        for chunk in faqs:
            if len(questions) >= 30:
                break
            
            # Extract question if it looks like an FAQ
            lines = chunk.content.split('\n')
            q_line = next((l for l in lines if l.lower().startswith('question:')), None)
            
            if q_line:
                q_text = q_line.split(':', 1)[1].strip()
                dept = chunk.chunk_metadata.get("department", "HR")
                questions.append({
                    "id": f"eval-{len(questions)+1}",
                    "question": q_text,
                    "category": "FAQ",
                    "department_context": dept,
                    "expected_source_document_ids": [chunk.document_id],
                    "expected_grounded": True,
                    "expected_access": True
                })

        # Process standard documents (Policies, SOPs, Meetings)
        docs = db.query(Document).limit(200).all()
        for doc in docs:
            if len(questions) >= 90:
                break
                
            title = doc.title
            if not title or title.endswith(".json") or title.endswith(".csv"):
                continue
                
            dept = doc.document_metadata.get("department", "IT")
            
            # Generate a question based on the title
            q_type = random.choice([
                f"What is the {title}?",
                f"Can you summarize the {title}?",
                f"What are the details of {title}?",
                f"According to {title}, what are the main points?"
            ])
            
            category = "Policy" if "policy" in title.lower() else "Meeting" if "meeting" in title.lower() else "General"
            
            questions.append({
                "id": f"eval-{len(questions)+1}",
                "question": q_type,
                "category": category,
                "department_context": dept,
                "expected_source_document_ids": [doc.id],
                "expected_grounded": True,
                "expected_access": True
            })
            
        # Add Negative / Insufficient Context Questions
        negative_qs = [
            "What is the nuclear launch code?",
            "Who won the Superbowl last year?",
            "How do I cook a turkey?",
            "What is the CEO's personal home address?",
            "Can you tell me the recipe for Coca Cola?",
            "What is the airspeed velocity of an unladen swallow?",
            "Who is the current president of Mars?",
            "What are the company's plans for time travel?",
            "How do I repair a spaceship engine?",
            "What is the wifi password for the White House?"
        ]
        
        for nq in negative_qs:
            if len(questions) >= 100:
                break
            questions.append({
                "id": f"eval-{len(questions)+1}",
                "question": nq,
                "category": "Negative",
                "department_context": "Any",
                "expected_source_document_ids": [],
                "expected_grounded": False,
                "expected_access": True
            })
            
    # Pad if we didn't reach 100
    while len(questions) < 100:
        questions.append({
            "id": f"eval-{len(questions)+1}",
            "question": "What is the general company policy?",
            "category": "General",
            "department_context": "HR",
            "expected_source_document_ids": [],
            "expected_grounded": True,
            "expected_access": True
        })

    # Shuffle for randomness
    # random.shuffle(questions)
    
    # Take exactly 100
    questions = questions[:100]
    
    output_path = os.path.join(os.path.dirname(__file__), "datasets", "rag_eval_questions.json")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, "w") as f:
        json.dump(questions, f, indent=4)
        
    print(f"Generated {len(questions)} evaluation questions to {output_path}")

if __name__ == "__main__":
    generate_dataset()

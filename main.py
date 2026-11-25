from fastapi import FastAPI

app = FastAPI()

notes = [
    {
        "id": 1,
        "term": "variable",
        "definition": "A name that stores a value.",
        "js_equivalent": "let / const",
        "tags": ["python", "basics"],
        "learned": True,
    },
    {
        "id": 2,
        "term": "list",
        "definition": "An ordered and mutable collection of items.",
        "js_equivalent": "Array",
        "tags": ["python", "data-structures"],
        "learned": True,
    },
    {
        "id": 3,
        "term": "dictionary",
        "definition": "A collection of key-value pairs.",
        "js_equivalent": "Object",
        "tags": ["python", "data-structures"],
        "learned": False,
    },
    {
        "id": 4,
        "term": "function",
        "definition": "A reusable block of code that performs a specific task.",
        "js_equivalent": "Function",
        "tags": ["python", "functions"],
        "learned": False,
    },
]

@app.get("/")
def root():
    return {
        "message": "Robin's API is running!",
        "status": "success"
    }

@app.get("/terms")
def get_terms(tag: str | None = None):
    result = []

    for note in notes:
        if tag and tag not in note["tags"]:
            continue

        result.append(note)

    return result


@app.get("/terms/{term_id}")
def get_term(term_id: int):
    for note in notes:
        if note["id"] == term_id:
            return note
    return {"message": "Term Not Found"}

# Extract specific keys from dictionaries
students = [
    {"name": "Ravi", "score": 85},
    {"name": "Meena", "score": 92},
    {"name": "Amit", "score": 78}
]

top_students = list(filter(lambda x: x["score"] > 80, students))
print(top_students)
# [{'name': 'Ravi', 'score': 85}, {'name': 'Meena', 'score': 92}]

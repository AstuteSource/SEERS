import json

def calculate_average_mutation_score_from_file(file_path):
    with open(file_path, 'r') as json_file:
        json_data = json.load(json_file)

    total_mutation_score = 0
    total_mutants = 0

    for item in json_data:
        mutation_score = item.get("mutation_score", 0)
        if mutation_score > 0:
            total_mutation_score += mutation_score
            total_mutants += 1
    if total_mutants == 0:
        return 0

    average_mutation_score = total_mutation_score / total_mutants
    return average_mutation_score

# Example usage:
json_file_path = "/home/student/juniorsem/SEERS/scripts/analyzer/JaclynMutScore.json"
average_score = calculate_average_mutation_score_from_file(json_file_path)
print("Predicted Mutation Score:", (average_score))

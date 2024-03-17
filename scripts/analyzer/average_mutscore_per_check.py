import json
from collections import defaultdict

def calculate_average_mutation_scores_from_file(file_path):
    with open(file_path, 'r') as json_file:
        json_data = json.load(json_file)

    mutation_scores_by_check = defaultdict(list)

    for item in json_data:
        check_id = item.get("pattern", {}).get("check_id")
        mutation_score = item.get("mutation_score", 0)
        if mutation_score > 0 and check_id:
            mutation_scores_by_check[check_id].append(mutation_score)

    average_scores = {}
    for check_id, scores in mutation_scores_by_check.items():
        if scores:
            average_scores[check_id] = sum(scores) / len(scores)
        else:
            average_scores[check_id] = 0

    return average_scores

# Example usage:
json_file_path = "/home/student/juniorsem/SEERS/scripts/analyzer/JaclynMutScore.json"
average_scores = calculate_average_mutation_scores_from_file(json_file_path)
print("Average Mutation Scores:")
for check_id, score in average_scores.items():
    print(check_id, ":", score)

def group_answers(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    grouped_answers = []
    current_group = []

    for line in lines:
        if line.strip():  # Check if the line is not empty
            current_group.append(line.strip()[line.strip().index(".") + 1:])
        else:
            if current_group:
                grouped_answers.append(current_group)
                current_group = []
    if current_group:
        grouped_answers.append(current_group)

    return grouped_answers

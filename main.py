from group_answers import group_answers
from txt_to_list import txt_to_list

option_map = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3
}


def main():
    questions = txt_to_list('questions.txt')
    answers = group_answers('answers.txt')
    correct_options = [int(option) for option in txt_to_list('correct_options.txt')]
    incorrect_questions = []

    print("Write your answer in 'a', 'b', 'c', 'd'\n")
    for index, question in enumerate(questions):
        print(question)
        for option in answers[index]:
            print("\t" + option)
        input_option = input("Choose the correct answer: ")
        if option_map[input_option.lower()] == correct_options[index]:
            print("\n\tBingo! Your choice is correct.\n")
        else:
            incorrect_questions.append(index)
            print("\n\tOops! Your choice is incorrect.")
            print("\tThe correct answer is:")
            print('\t' + answers[index][correct_options[index]] + '\n')


if __name__ == "__main__":
    main()

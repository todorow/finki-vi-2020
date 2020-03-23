
def read_from_system_in():
    data = {}
    input_data = input().split(",")
    while not input_data.__contains__("end"):
        full_name = input_data[0] + " " + input_data[1]
        index = input_data[2]
        score = [int(input_data[4]), int(input_data[5]), int(input_data[6])]
        subject = {input_data[3]: score}
        if index in data:
            if full_name in data[index]:
                current_subjects = data[index][full_name]
                data[index][full_name] = current_subjects + [subject]
            else:
                data[index] = {full_name: [subject]}
        else:
            data[index] = {full_name: [subject]}
        input_data = input().split(",")
    return data


def calculate_grade(score):
    total_score = sum(score, 0)
    if total_score in range(0, 51, 1):
        return "5"
    elif total_score in range(51, 61, 1):
        return "6"
    elif total_score in range(61, 71, 1):
        return "7"
    elif total_score in range(71, 81, 1):
        return "8"
    elif total_score in range(81, 91, 1):
        return "9"
    elif total_score in range(91, 101, 1):
        return "10"


if __name__ == "__main__":
    students = read_from_system_in()
    for key in students.keys():
        student_name = [name for name in students[key].keys()][0]
        print("Student: " + student_name )
        for subject in students[key][student_name]:
            subject_name = [ name  for name in subject.keys() ][0]
            grade = calculate_grade(subject[subject_name])
            print("    " + subject_name + ": " + grade)
        print("")

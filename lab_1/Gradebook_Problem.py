"""Gradebook Problem 1 (0 / 4)
Дефинирајте речник students во кој ќе се чуваат информации за предметите кои ги полагале студентите.
Од стандарден влез се читаат информации за име, презиме, број на индекс, предмет, поени од теоретски дел,
 поени од практичен дел и поени од лабораториски вежби. Може да се вчитаат информации за неограничен број студенти.
  Вчитувањето информации завршува кога ќе се прочита клучниот збор end.
  Пополнете го речникот students со вчитаните информации.

Потоа, за секој од студентите да се испечати името и презимето, и оцената за секој од предметите кои ги има полагано.

Оцената се пресметува на следниот начин:

[0, 50] - 5

(50, 60] - 6

(60, 70] - 7

(70, 80] - 8

(80, 90] - 9

(90, 100] - 10

Sample input:
Alice,Doe,141414,Artificial Intelligence,40,40,5
Alice,Doe,141414,Machine Learning,30,40,10
Lewis,Smith,141415,Robotics,40,30,10
Lewis,Smith,141415,Bioinformatics,40,30,10
George,Williams,123456,Artificial Intelligence,20,40,9
James,Brown,123457,Artificial Intelligence,25,30,3
William,Williams,123458,Artificial Intelligence,10,45,8
Elle,Brown,123459,Artificial Intelligence,45,10,7
end

Sample output:
Student: Alice Doe
    Artificial Intelligence: 9
    Machine Learning: 8

Student: Lewis Smith
    Robotics: 8
    Bioinformatics: 8

Student: George Williams
    Artificial Intelligence: 7

Student: James Brown
    Artificial Intelligence: 6

Student: William Williams
    Artificial Intelligence: 7

Student: Elle Brown
    Artificial Intelligence: 7
"""


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

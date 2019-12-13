if __name__ == '__main__':
    python_students = []
    for _ in range(int(input())):
        python_students.append([input(), float(input())])

    second_lowest = sorted(
        list(set([marks for name, marks in python_students])))[1]
    print('\n'.join([a for a, b in sorted(
        python_students) if b == second_lowest]))

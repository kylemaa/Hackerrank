import operator
nested_dictionary = {'username1': {'INFO': 1, 'ERROR': 2},
                     'username2': {'INFO': 101, 'ERROR': 102},
                     'username3': {'INFO': 1001, 'ERROR': 1002}}


def generate_user_report(dictionary, report_file):
    with open(report_file, "w+") as f:
        f.write(["key", "value", "Contribution"])
        for k in sorted(dictionary.items(), key=operator.itemgetter(0)):
            f.write(str(k)+':'+str(dictionary[k]) + '\n')
        f.close()


generate_user_report(
    nested_dictionary, '/Users/KKyle/Hackerrank/Python-Proficiency/nested_dictionary.csv')

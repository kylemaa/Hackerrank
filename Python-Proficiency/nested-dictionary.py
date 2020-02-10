import operator

nested_dictionary = {'abby': {'INFO': 1, 'ERROR': 2},
                     'kyle': {'INFO': 101, 'ERROR': 102},
                     'ben': {'INFO': 1001, 'ERROR': 1002}}
normal_dictionary = {'error_name1': 30, 'error_name2': 44, 'error_name3': 0}


def generate_user_report(dictionary, report_file):
    with open(report_file, "w+") as f:
        f.write("Username"+', '+"INFO"+', '+"ERROR" + '\n')
        for k in sorted(dictionary.items(), key=operator.itemgetter(0)):
            f.write(
                str(k[0])+', '+str(k[1]['INFO'])+', '+str(k[1]['ERROR']) + '\n')
        f.close()


def generate_error_report(dictionary, report_file):
    with open(report_file, "w+") as f:
        f.write("Error"+', ' + "Count" + '\n')
        for k in sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True):
            f.write(str(k[0])+', '+str(k[1])+'\n')
        f.close()


generate_user_report(
    nested_dictionary, '/Users/KKyle/Hackerrank/Python-Proficiency/nested_dictionary.csv')

generate_error_report(
    normal_dictionary, '/Users/KKyle/Hackerrank/Python-Proficiency/nested_error_dictionary.csv')

import re


def check_web_address(text):
    pattern = "^[a-zA-Z_+.-]*\.[a-zA-Z]*$"
    result = re.search(pattern, text)
    return result != None


# print(check_web_address("gmail.com"))  # True
# print(check_web_address("www@google"))  # False
# print(check_web_address("www.Coursera.org"))  # True
# print(check_web_address("web-address.com/homepage"))  # False
# print(check_web_address("My_Favorite-Blog.US"))  # True


def check_time(text):
    pattern = "[1]?[0-9]:[0-5][0-9] ?[amAM|pmPM]"
    result = re.search(pattern, text)
    return result != None


# print(check_time("12:45pm"))  # True
# print(check_time("9:59 AM"))  # True
# print(check_time("6:60am"))  # False
# print(check_time("five o'clock"))  # False


def extract_pid(log_line):
    regex = r"\[(\d+)\]: (\b[A-Z]*\b)"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1], result[2])


# 12345 (ERROR)
# print(extract_pid(
#     "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"))
# print(extract_pid("99 elephants in a [cage]"))  # None
# print(extract_pid(
#     "A string that also has numbers [34567] but no uppercase message"))  # None
# # 67890 (RUNNING)
# print(extract_pid(
#     "July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup"))

def convert_phone_number(phone):
    result = re.sub(r"(\d{3})(-\d{3})(-\b\d{4}\b)", r"(\1)\2\3", phone)
    return result


# My number is (212) 345-9999.
print(convert_phone_number("My number is 212-345-9999."))
# Please call (888) 555-1234
print(convert_phone_number("Please call 888-555-1234"))
print(convert_phone_number("123-123-12345"))  # 123-123-12345
# Phone number of Buckingham Palace is +44 303 123 7300
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300"))

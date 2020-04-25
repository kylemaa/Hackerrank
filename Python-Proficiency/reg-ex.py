import csv
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
# print(convert_phone_number("My number is 212-345-9999."))
# # Please call (888) 555-1234
# print(convert_phone_number("Please call 888-555-1234"))
# print(convert_phone_number("123-123-12345"))  # 123-123-12345
# # Phone number of Buckingham Palace is +44 303 123 7300
# print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300"))

def transform_record(record):
    new_record = re.sub(r"(\d+)-(\d+)?(\d+)?", r"+1-\1-\2\3", record)
    return new_record


# print(transform_record("Sabrina Green,802-867-5309,System Administrator"))
# # Sabrina Green,+1-802-867-5309,System Administrator

# print(transform_record("Eli Jones,684-3481127,IT specialist"))
# # Eli Jones,+1-684-3481127,IT specialist

# print(transform_record("Melody Daniels,846-687-7436,Programmer"))
# # Melody Daniels,+1-846-687-7436,Programmer

# print(transform_record("Charlie Rivera,698-746-3357,Web Developer"))
# # Charlie Rivera,+1-698-746-3357,Web Developer

def multi_vowel_words(text):
    pattern = "\w*[aeiou]{3}\w*"
    result = re.findall(pattern, text)
    return result


# print(multi_vowel_words("Life is beautiful"))
# # ['beautiful']

# print(multi_vowel_words("Obviously, the queen is courageous and gracious."))
# # ['Obviously', 'queen', 'courageous', 'gracious']

# print(multi_vowel_words(
#     "The rambunctious children had to sit quietly and await their delicious dinner."))
# # ['rambunctious', 'quietly', 'delicious']

# print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)"))
# # ['queue']

# print(multi_vowel_words("Hello world!"))
# # []

"""Lab for REGEX """
#!/usr/bin/env python3


def contains_domain(address, domain):
    """Returns True if the email address contains the given,domain,in the domain position, false if not."""
    domain = r'[\w\.-]+@'+domain+'$'
    if re.match(domain, address):
        return True
    return False


def replace_domain(address, old_domain, new_domain):
    """Replaces the old domain with the new domain in the received address."""
    old_domain_pattern = r'' + old_domain + '$'
    address = re.sub(old_domain_pattern, new_domain, address)
    return address


def main():
    """Processes the list of emails, replacing any instances of the old domain with the new domain."""
    old_domain, new_domain = 'abc.edu', 'xyz.edu'
    csv_file_location = '<csv_file_location>'
    report_file = '<path_to_home_directory>' + '/updated_user_emails.csv'
    user_email_list = []
    old_domain_email_list = []
    new_domain_email_list = []

    with open(csv_file_location, 'r') as f:
        user_data_list = list(csv.reader(f))
        user_email_list = [data[1].strip() for data in user_data_list[1:]]

        for email_address in user_email_list:
            if contains_domain(email_address, old_domain):
                old_domain_email_list.append(email_address)
                replaced_email = replace_domain(
                    email_address, old_domain, new_domain)
                new_domain_email_list.append(replaced_email)

        email_key = ' ' + 'Email Address'
        email_index = user_data_list[0].index(email_key)

        for user in user_data_list[1:]:
            for old_domain, new_domain in zip(old_domain_email_list, new_domain_email_list):
                if user[email_index] == ' ' + old_domain:
                    user[email_index] = ' ' + new_domain
    f.close()

    with open(report_file, 'w+') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(user_data_list)
        output_file.close()


# main()

def show_time_of_pid(line):
    pattern = r"(\w{3}) (\d \d+:\d+:\d+).*\[(\d+)\]"
    result = re.search(pattern, line)
    return "{} {} pid:{}".format(result[1], result[2], result[3])


# # Jul 6 14:01:23 pid:29440
# print(show_time_of_pid(
#     "Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)"))

# # Jul 6 14:02:08 pid:29187
# print(show_time_of_pid(
#     "Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)"))

# # Jul 6 14:02:09 pid:29187
# print(show_time_of_pid(
#     "Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)"))

# # Jul 6 14:03:01 pid:29440
# print(show_time_of_pid(
#     "Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)"))

# # Jul 6 14:03:40 pid:29807
# print(show_time_of_pid(
#     "Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\""))

# # Jul 6 14:04:01 pid:29440
# print(show_time_of_pid(
#     "Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)"))

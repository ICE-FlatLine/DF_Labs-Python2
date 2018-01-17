import os

folder_path = "/Users/slavataras/Downloads/Software/Music/Arctic Monkeys - Favorite Worst Nightmare - Universal"
my_folder = os.listdir(folder_path)


def convert_bytes(num):  # this function will convert byte values to KB, MB, GB or TB using metric (SI) system

    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1000:
            return "%3.1f %s" % (num, x)
        num /= 1000.0


def longest_el(a_list):
    longest_element_length = 0
    for element in a_list:
        if len(element) > longest_element_length:
            longest_element_length = len(element)
    # padding = " " * (longest_element_length + 5)
    return longest_element_length


for item_name in my_folder:
    item_full_path = folder_path + "/" + item_name
    item_size = os.stat(item_full_path).st_size
    print "%s %s" % (item_name, convert_bytes(item_size))


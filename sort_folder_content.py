import os

folder_path = "/Users/slavataras/Downloads/Software/Music/Arctic Monkeys - Favorite Worst Nightmare - Universal"
my_folder = os.listdir(folder_path)


# this function will convert byte values to KB, MB, GB or TB using metric (SI) system

def convert_bytes(num):

    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1000:
            return "%3.1f %s" % (num, x)  # displays up to 3 digits before decimal separator and one decimal digit after
        num /= 1000.0


# this function will return the longest element in the given list for the eventual calculation of desired padding value
# in "list_folder" function

def longest_element(a_list):
    longest_element_length = 0
    for element in a_list:
        if len(element) > longest_element_length:
            longest_element_length = len(element)
    return longest_element_length


# this function will print items in the given list (folder) and their respective sizes (in readable format) in the form
# of a table, where a padding value between columns is calculated based on the longest item name in the given list

def list_folder(a_folder):
    padding = longest_element(a_folder) + 10
    for item_name in a_folder:
        item_full_path = os.path.join(folder_path, item_name)
        item_size = os.stat(item_full_path).st_size
        print item_name.ljust(padding),
        print convert_bytes(item_size)


list_folder(my_folder)






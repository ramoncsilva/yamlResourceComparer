import yaml
import re
import argparse


def flatten_yaml(data, parent_key='', sep='.'):
    items = []
    if isinstance(data, list):
        for i, item in enumerate(data):
            new_key = f"{parent_key}{sep}{item}" if parent_key else item
            if isinstance(item, dict):
                items.extend(flatten_yaml(item, parent_key, sep=sep))
            else:
                items.append(new_key)
    elif isinstance(data, dict):
        for k, v in data.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, (dict, list)):
                items.extend(flatten_yaml(v, new_key, sep=sep))
            else:
                if not isinstance(v, (dict, list)):
                    new_key = f"{new_key}{sep}{v}"
                items.append(new_key)
    return items


def find_by_attribute(items=[], attribute_name=""):
    filtered_items = []
    for item in items:
        if attribute_name in item:
            filtered_items.append(item)
    return filtered_items


def remove_before_word(text="", word=""):
    # Regex para encontrar tudo antes da palavra especificada
    pattern = rf'.*?(?={word})'
    # Substitui tudo antes da palavra por uma string vazia
    result = re.sub(pattern, '', text)
    return result


def clear_list_words_before_sufix(items=[], sufix=""):
    cleared_items = []
    for item in items:
        cleared_items.append(remove_before_word(item, sufix))
    return cleared_items


def compare_two_yaml_file_attributes(
        first_file_path="",
        second_file_path="",
        first_file_filter_attribute="",
        second_file_filter_attribute="",
        first_file_clear_attribute_path=False,
        second_file_clear_attribute_path=False
):
    first_output_list = []
    second_output_list = []

    with open(first_file_path, 'r') as first_file:
        first_yaml_data = yaml.safe_load(first_file)

    with open(second_file_path, 'r') as second_file:
        second_yaml_data = yaml.safe_load(second_file)

    first_flattened_data = flatten_yaml(first_yaml_data)
    second_flattened_data = flatten_yaml(second_yaml_data)

    if first_file_filter_attribute is not "":
        first_output_list = find_by_attribute(first_flattened_data, first_file_filter_attribute)
        if first_file_clear_attribute_path:
            first_output_list = clear_list_words_before_sufix(first_output_list, first_file_filter_attribute)

    if second_file_filter_attribute is not "":
        second_output_list = find_by_attribute(second_flattened_data, second_file_filter_attribute)
        if second_file_clear_attribute_path:
            second_output_list = clear_list_words_before_sufix(second_output_list, second_file_filter_attribute)

    return first_output_list, second_output_list


def find_different_attributes(first_list, second_list):
    present_on_first_list_not_in_second = first_list.copy()
    present_on_second_list_not_in_first = second_list.copy()

    for look_attribute in first_list:
        for target_attribute in second_list:
            if look_attribute in target_attribute:
                present_on_first_list_not_in_second.remove(look_attribute)

    for look_attribute in second_list:
        for target_attribute in first_list:
            if look_attribute in target_attribute:
                present_on_second_list_not_in_first.remove(look_attribute)

    return present_on_first_list_not_in_second, present_on_second_list_not_in_first


parser = argparse.ArgumentParser()
parser.add_argument("fyp", help="first yaml file path")
parser.add_argument("syp", help="second yaml file path")
parser.add_argument("--fre", required=True, help="first file root element")
parser.add_argument("--sre", required=True, help="second file root element")
parser.add_argument("--fcrsf", help="clear root sufixes on first file", action="store_true")
parser.add_argument("--scrsf", help="clear root sufixes on second file", action="store_true")
parser.add_argument("-d","--diff", help="clear root sufixes on second file", action="store_true")
args = parser.parse_args()

diff_first, diff_second = compare_two_yaml_file_attributes(
    args.fyp,
    args.syp,
    args.fre,
    args.sre,
    args.fcrsf,
    args.scrsf
)

diff_first, diff_second = find_different_attributes(diff_first, diff_second)
print("+++ FIRST FILE +++")
for item in diff_first:
    print(f"{item}")
print("+++ FIRST FILE +++")
print("==== ======== ====")
print("+++ SECOND FILE ++")
for item in diff_second:
    print(f"{item}")
print("+++ SECOND FILE ++")

from pprint import pprint

from SourceCode import SourceCode
from SourceCodeFiles import SourceCodeFiles


def reduce_to_60():
    with open("out.txt", "r", encoding="utf-8", errors="ignore") as f1:
        lines = f1.readlines()
    with open("out2.txt", "w", encoding="utf-8", errors="ignore") as f2:
        f2.writelines(lines[:50*30])
        f2.writelines(lines[-50*30:-1])


def main():
    source_code_files = SourceCodeFiles("code")
    output_list = []
    for file_path in source_code_files.file_path_list:
        source_code = SourceCode(source_code_files.root, file_path)
        output_list.append(source_code.get_content())
    with open("out.txt", "w", encoding="utf-8", errors="ignore") as f:
        f.writelines(output_list)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    reduce_to_60()

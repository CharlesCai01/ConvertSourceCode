from SourceCode import SourceCode


def main():
    source_code = SourceCode(r"D:\MyWork\PycharmProjects\ConvertSourceCode\code",
                             r"D:\MyWork\PycharmProjects\ConvertSourceCode\code\User.js")
    print(source_code.get_content())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

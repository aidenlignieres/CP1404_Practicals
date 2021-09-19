"""Running simple client side code program"""


from programming_language import ProgrammingLanguage


def main():
    """Storing starting variables and then testing if they are dynamically typed programs"""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    language = [ruby, python, visual_basic]
    print("The Dynamically typed languages are:")
    for language in language:
        if language.is_dynamic():
            print(language.name)


main()

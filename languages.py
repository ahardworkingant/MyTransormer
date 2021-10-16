from programming_language import ProgrammingLanguage
def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    # print(python.__str__())
    # print(visual_basic.is_dynamic())
    object = [ruby,python,visual_basic]
    return object
def test_is_dynamic(object):
    print("The dynamically typed languages are:")
    for i in object:
        if i.is_dynamic():
            print(f"format({i.Name:5})")
test_is_dynamic(main())
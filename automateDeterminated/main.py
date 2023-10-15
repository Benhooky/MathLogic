from automation import FiniteAutomaton


def main():
    automaton = FiniteAutomaton()
    input_string = input("Write the string: ")
    result = automaton.process_string(input_string)
    if result:
        print("String is accepted.")
    else:
        print("String is not accepted.")


if __name__ == '__main__':
    main()

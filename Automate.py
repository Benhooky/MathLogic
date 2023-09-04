class FiniteAutomaton:
    def __init__(self):
        self.states = {'S', 'Q', 'G'}
        self.transitions = {
            'S': {'Q'},
            'Q': {'Q', 'G'},
            'G': {'Q', 'S'}
        }
        self.current_state = 'S'
    
    def process_input(self, input_text):
        for char in input_text:
            if char.isdigit():
                if self.current_state == 'S':
                    self.current_state = 'Q'
                elif self.current_state == 'Q':
                    pass  # Stay in Q
                elif self.current_state == 'G':
                    self.current_state = 'Q'
                else:
                    return "Не соответствует"
            elif char in (',', ' '):
                if self.current_state in ('Q', 'G'):
                    self.current_state = 'G'
                else:
                    return "Не соответствует"
            else:
                return "Символы не из алфавита"
        
        if self.current_state == 'Q':
            return "Строка соответствует"
        else:
            return "Не соответствует"

# Пример использования
input_text = input("Введите текст: ")
automaton = FiniteAutomaton()
result = automaton.process_input(input_text)
print(result)

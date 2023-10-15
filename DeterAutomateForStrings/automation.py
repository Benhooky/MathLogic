from colorama import Fore, Style


class State:
    """
    Represents a state in a finite automaton.

    Attributes:
        name (str): A unique name for the state.
        transitions (dict): Dictionary of transitions to other states.
        is_final (bool): Indicates if the state is final.
        default_next (State): Default state to transition if no matching symbol is found.

    Methods:
        add_transition(symbol, state): Add a transition for a symbol.
        set_default_next(state): Set the default state for transitions.
        next_state(symbol): Get the next state for a symbol.
    """

    def __init__(self, name, is_final=False):
        self.name = name
        self.transitions = {}
        self.is_final = is_final
        self.default_next = None

    def add_transition(self, symbol, state):
        """Add a transition for a given symbol to another state."""
        self.transitions[symbol] = state

    def set_default_next(self, state):
        """Set the default state to transition to if no matching symbol is found."""
        self.default_next = state

    def next_state(self, symbol):
        """Get the next state for a symbol or the default state if not found."""
        return self.transitions.get(symbol, self.default_next)


class FiniteAutomaton:
    """
    Represents a deterministic finite automaton (DFA).

    Attributes:
        start_state (State): The initial state.
        current_state (State): The current state during processing.

    Methods:
        reset(): Reset the current state to the start state.
        transition(symbol): Perform a transition based on a symbol.
        process_string(input_string): Process an input string.
    """

    def __init__(self):
        self.start_state = State(1)
        state2 = State(2)
        state3 = State(3)
        state4 = State(4)
        state5 = State(5, True)
        state6 = State(6, True)
        error_state = State("error")

        self.start_state.set_default_next(self.start_state)
        state2.set_default_next(error_state)
        state3.set_default_next(error_state)
        state4.set_default_next(error_state)
        state5.set_default_next(state6)
        state6.set_default_next(state6)
        error_state.set_default_next(error_state)

        self.add_transition(self.start_state, "123456789", state2)
        self.add_transition(state2, "0123456789", state3)
        self.add_transition(state3, "0123456789", state4)
        self.add_transition(state4, "0123456789", state5)
        self.add_transition(state5, "0123456789", state5)
        self.add_transition(state6, "123456789", state2)

        self.current_state = self.start_state

    def add_transition(self, state, symbols, next_state):
        for symbol in symbols:
            state.add_transition(symbol, next_state)

    def reset(self):
        """Reset the current state to the start state."""
        self.current_state = self.start_state

    def transition(self, symbol):
        """Perform a transition based on the given symbol."""
        next_state = self.current_state.next_state(symbol)
        position = len(self.current_string) + 1
        if next_state.name == "error":
            error_message = f"False because of position {position}: {self.current_string}{self.color_symbol(symbol)}"
            print(error_message)
            return False
        self.current_string += symbol
        self.current_state = next_state
        return True

    def color_symbol(self, symbol):
        return f"{Fore.RED}{symbol}{Style.RESET_ALL}"

    def process_string(self, input_string):
        """Process an input string and determine if it's accepted by the DFA."""
        self.reset()
        self.current_string = ""
        for symbol in input_string:
            if not self.transition(symbol):
                return False

        return self.current_state.is_final

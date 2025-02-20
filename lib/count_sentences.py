#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        self._value = ""
        self.set_value(value)

    def get_value(self):
        return self._value

    def set_value(self, value):
        if not isinstance(value, str):
            print("The value must be a string.")
        else:
            self._value = value

    value = property(get_value, set_value)
    def is_sentence(self):
        if len(self.value) > 0 and self.value[-1] == ".":
            return True
        return False

    def is_question(self):
        if len(self.value) > 0 and self.value[-1] == "?":
            return True
        return False

    def is_exclamation(self):
        if len(self.value) > 0 and self.value[-1] == "!":
            return True
        return False

    def count_sentences(self):
        count = 0
        i = 0
        while i < len(self.value):
            if self.value[i] in ".!?":
                count += 1
                while i + 1 < len(self.value) and self.value[i + 1] in ".!?":
                    i += 1
            i += 1
        return count
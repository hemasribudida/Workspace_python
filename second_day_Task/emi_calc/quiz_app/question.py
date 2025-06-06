class Question:
    def __init__(self, number, text, options, answer_index):
        self.number = number
        self.text = text
        self.options = options
        self.answer_index = answer_index

    def display(self):
        print(f"\nQ{self.number}. {self.text}")
        for i, option in enumerate(self.options, 1):
            print(f"{i}. {option}")
        while True:
            try:
                user_input = int(input("Your answer (1-4): "))
                if user_input in [1, 2, 3, 4]:
                    return user_input == self.answer_index
                else:
                    print("Please enter a valid option (1-4).")
            except ValueError:
                print("Please enter a number (1-4).")

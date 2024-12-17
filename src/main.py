class RockPaperScissors():

    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']

    def get_user_choice(self):
        user_choice = input(f"Please enter your choice from {self.choices}")
        if user_choice.lower() in self.choices:
            return user_choice.lower()
        print("please enter a valid choice")
        return self.get_user_choice()
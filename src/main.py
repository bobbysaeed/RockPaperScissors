class RockPaperScissors():

    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']

    def get_user_choice(self):
        user_choice = input(f"Please enter your choice from {self.choices}")
        if user_choice.lower() in self.choices:
            return user_choice.lower()
        print("please enter a valid choice")
        return self.get_user_choice()

    def get_pc_choice(self):
        return random.choice(self.choices)

    def get_the_winner(self, user_choice, pc_choice):
        winning_Conditions = [('rock', 'scissors'), ('paper', 'rock'), ('scissors', 'paper')]

        if user_choice == pc_choice:
            print("it's a tie!")
        for winning_Condition in winning_Conditions:

            if winning_Condition[1] == pc_choice and winning_Condition[0] == user_choice:
                print("You Have Won! CONGRATS...")

        print("Oops! You just lost to a Computer")
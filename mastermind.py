import random as ran
import sys

class MasterMind:

    def __init__ (self):
        """Initialize the game, and create game resources."""

        self.answer = [0, 0, 0, 0]
        self.guess = [0, 0, 0, 0]
        self.attempted_guesses = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.life = 0
        self.running = True

    def run_game(self):
        self._starting_output()
        while self.running:
            if self.guess == self.answer:
                self.running = False
            elif self.life > 6:
                self._lose_state()
            else:
                self._take_input()
        sys.exit()

    def _lose_state(self):
        print("You have used all your guesses. Better luck next time!\n\n")
        self.life = 0
        self._starting_output()

    def _take_input(self):
        print("Guess is incorrect. You guessed the following digits correctly: ")
        prompt = input()
        self._check_input(prompt)

    def _starting_output(self):
        # Generate Initial Answer
        self._generate_answer()
        print("Welcome to Mastermind. Press (Q) to quit or a 4 digit number to start guessing. ")
        prompt = input()
        self._check_input(prompt)

    def _check_input(self, prompt):
        if prompt == 'Q' or prompt == 'q':
            self.running = False
        else:
            for i in range(len(prompt)):
                self.guess[i] = int(prompt[i])
            self.attempted_guesses[self.life] = self.guess
            self.life += 1

    def _generate_answer(self):
        for i in range(len(self.answer)):
            self.answer[i] = ran.randint(0, 9)

if __name__ == '__main__':
    mm = MasterMind()
    mm.run_game()
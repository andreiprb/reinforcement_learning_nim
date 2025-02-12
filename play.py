from nim.Nim import *

import random


if __name__ == '__main__':
    ai_player = train()
    human_player = random.randint(0, 1)

    game = Nim()

    while True:
        print()
        print("Piles:")
        for i, pile in enumerate(game.piles):
            print(f"Pile {i}: {pile}")
        print()

        available_actions = NimLogic.available_actions(game.piles)


        def get_int(prompt):
            while True:
                user_input = input(prompt)
                try:
                    return int(user_input)
                except ValueError:
                    continue

        if game.player == human_player:
            print("Your Turn")
            while True:
                pile = get_int("Choose Pile: ")
                count = get_int("Choose Count: ")
                if (pile, count) in available_actions:
                    break
                print("Invalid move, try again.")

        else:
            print("AI's Turn")
            pile, count = ai_player.choose_action(game.piles, epsilon=False)
            print(f"AI chose to take {count} from pile {pile}.")

        game.move((pile, count))

        if game.winner is not None:
            print()
            print("GAME OVER")
            winner = "Human" if game.winner == human_player else "AI"
            print(f"Winner is {winner}")

            break

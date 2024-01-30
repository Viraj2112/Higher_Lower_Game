from random import randint
from replit import clear
from game_data import data
from art import logo, vs


def random_number():
  return randint(0, len(data) - 1)


def compare(user_choice, num1, num2):
  '''it takes the user choice a or b, and evaluates who has more followers.'''
  if user_choice == 'a':  # user chose a
    if data[num1]['follower_count'] > data[num2]['follower_count']:
      return True
    else:
      return False
  else:  # user chose b
    if data[num2]['follower_count'] > data[num1]['follower_count']:
      return True
    else:
      return False


def higher_lower_game():
  end_of_game = False
  score = 0
  print(logo)  # Logo of the game

  while end_of_game == False:
    if score == 0:
      num1 = random_number()
      while True:
        num2 = random_number()
        if num2 != num1:
          break  # Generating random integers for a and b
    else:
      num1 = num2
      num2 = random_number()

    name_a, description_a, location_a = data[num1]['name'], data[num1][
      'description'], data[num1]['country']
    name_b, description_b, location_b = data[num2]['name'], data[num2][
      'description'], data[num2]['country']
    # Stored the name description and location in seperate variables for both a and b.

    print(f"Compare A: {name_a}, {description_a}, from {location_a}")  #  A
    print(vs)  # VS symbol
    print(f"Against B: {name_b}, {description_b}, from {location_b}")  #  B
    choice = input("Who has more followers? 'A' or 'B': ").lower(
    )  # Ask for user choice A or B.

    comparison = compare(choice, num1, num2)
    if comparison == False:  #if user is wrong
      end_of_game = True
    else:
      score += 1
      clear()
      print(logo)  # logo
      print(f"You are right. The correct score is: {score}")

  clear()
  print(logo)  # Logo
  print(f"Sorry that's wrong. Final score = {score}")


while input(
    "Do you want to play Higher Lower Game: 'Y' or 'N': ").lower() == 'y':
  clear()
  higher_lower_game()

print("Thankyou for Playing.")

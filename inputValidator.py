class Validator:
  @staticmethod
  def get_integer(prompt, min, max):
    while True:
      try:
        inputString = input(prompt)  # Get user input
        inputInt = int(inputString)  # Convert to int
        if min <= inputInt <= max:  # Verify range
          return inputInt  # Return valid input
        else:
          print(f"Please enter a value between {min} and {max}.")
      except ValueError:
        print("Invalid input. Please enter a valid integer.")
  @staticmethod
  def get_float(prompt, min, max):

    # loop until correct input received
    while True:
      try:
        inputString = input(prompt)      # get user input
        inputFloat = float(inputString)  # try to convert to float

        if (inputFloat >= min) and (inputFloat <= max):  # verify range
          return inputFloat          # success!
      except:
         continue                    # try again
         
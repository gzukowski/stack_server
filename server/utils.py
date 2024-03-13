import random

GROWTH = {"dec": 1, "inc": -1}


# DEPRECATED 2 BYTE PUSH  "AX": 2
REGISTER = {"EAX": 4, }
EAX = 4  # bytes
#AX = 2  # bytes
MINIMUM_ADDRESS = 0x0fffff05
MAXIMUM_ADDRESS = 0x0ffffffa
MINIMUM_VALUE = 0x10000000
MAXIMUM_VALUE = 0x1fffffff


def generate_new_task():
      register = random.choice(list(REGISTER.keys()))
      stack_pointer : int =  random.randint(MINIMUM_ADDRESS,MAXIMUM_ADDRESS)
      growth = random.choice(list(GROWTH.keys()))
      cells = [
            hex(stack_pointer - (3*GROWTH[growth]))[2:],
            hex(stack_pointer - (2*GROWTH[growth]))[2:],
            hex(stack_pointer - (1*GROWTH[growth]))[2:],
            hex(stack_pointer)[2:],
            hex(stack_pointer + (1*GROWTH[growth]))[2:],
            hex(stack_pointer + (2*GROWTH[growth]))[2:],
            hex(stack_pointer + (3*GROWTH[growth]))[2:]
      ]
      answer : str = str(hex(random.randint(MINIMUM_VALUE,MAXIMUM_VALUE)))[2:]
      splitted_answer = [answer[i:i+2] for i in range(0, len(answer), 2)]

      answer = splitted_answer

      hex_integers = [random.randint(0, 255) for _ in range(3)]
      hex_strings = [hex(num)[2:].zfill(2) for num in hex_integers]

      values = []

      if GROWTH[growth] == -1:
            values =  answer  + hex_strings
      else:
            values =  hex_strings + answer[::-1]

    

      return {
            "cells" : cells,
            "esp" : stack_pointer,
            "answer" : answer,
            "values" : values,
            "register" : register
            }

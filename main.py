import argparse
import random

def natural_number(value):
  ivalue = int(value)
  if ivalue < 0:
    raise argparse.ArgumentTypeError("%s is an invalid positive int value" % value)
    return ivalue

parser = argparse.ArgumentParser()
parser.add_argument('green', type=natural_number)
parser.add_argument('red', type=natural_number)
parser.add_argument('yellow', type=natural_number)

dice = {
    'yellow' : {
      1: 1,
      2: 1,
      3: 2,
      4: 100,
      5: 101,
      6: 102
    },
    'red' : {
      1: 1,
      2: 2,
      3: 2,
      4: 2,
      5: 3,
      6: 103
    },
    'green' : {
      1: 1,
      2: 1,
      3: 100,
      4: 100,
      5: 101,
      6: 101
    },
    'blue' : {
      1: 0,
      2: 1,
      3: 2,
      4: 2,
      5: 101,
      6: 102
    }
}

rollvalues = {
  'blue' : [],
  'red' : [],
  'green' : [],
  'yellow' : [],
}

def roll(name):
  die = dice[name]
  value = die[random.choice(list(die))]
  rollvalues[name] = value
  return value

print(roll('blue'))

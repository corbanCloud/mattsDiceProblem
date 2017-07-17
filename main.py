import argparse
import sys
import random
import pprint

# Define our natural_number filter to format user input
# We don't want to try and roll a dice -1 or 1/2 times
def natural_number(value):
  ivalue = int(value)
  if ivalue < 0:
    raise argparse.ArgumentTypeError("%s is an invalid natural number" % value)

  return ivalue

# @Matt ignore this for now. TL;DR takes the --green=1 on the command line
# and turns it into a variable we can use and ensures it it a natural
# number by running it through the function above
parser = argparse.ArgumentParser(description='Description of your program')
parser.add_argument('-g','--green', help='Description for foo argument', required=True, type=natural_number)
parser.add_argument('-r','--red', help='Description for bar argument', required=True, type=natural_number)
parser.add_argument('-y','--yellow', help='Description for bar argument', required=True, type=natural_number)
parser.add_argument('-s','--samplesize', help='Description for bar argument', required=True, type=natural_number)
args = vars(parser.parse_args())
#sssssshhhhhh just let this happen for now
args['blue'] = 1
# Pretty printer we will use so we can see the dictionary better
pp = pprint.PrettyPrinter(indent=4)

# Our "dice"
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

# Our dictionary for storing roll values
sample = []
# surgesize : frequency
surges = {}
# name should be a key form the dice dictionary
def roll(name, store):
  # get the die
  die = dice[name]
  # pick a random face, and get that value
  value = die[random.choice(list(die))]
  # add that to the roll history
  store[name].append(value)
  return value

for i in range(args['samplesize']):
    simulation = {
     'blue' : [],
     'green' : [],
     'yellow' : [],
     'red' : []
    }
    # for each one of our die
    for dieName in simulation:
        # roll it how ever many times the CLI args indicated
        for x in range(args[dieName]):
          roll(dieName, simulation)

    sample.append(simulation)
    for dieName, outcomes in simulation.items():
        surgesize = sum(i > 99 for i in outcomes)
        if surgesize in surges:
            surges[surgesize] += 1
        else:
            surges[surgesize] = 1

print("--- Sample Data Generated  ---")
pp.pprint(sample)
print("--- Surge Occurences ---")
print("(Quantity of Surges in a set vs Total Occurences Of That Quantity)")
pp.pprint(surges)

#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  # specify the items that are going to be combined(rock,paper,scissors)
  #create a list to hold the possible combinations
  #list should have lists inside it for combinations
  #match every item with the others and loop back
  #n represents the number of plays per round
  #if recursive, find a base case to terminate, a recursive case and a progress made at each invocation of the recursive funtion

  #options
  options = ['rock', 'paper', 'scissors']
  possibilities =[]

  for i in options:
    pass



  return possibilities


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
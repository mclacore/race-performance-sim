def main():
  print("Welcome to the running app")
  grade_splits(session())
  print("Goodbye")


def session():
  session = {}
  session['distance'] = int(input("Add distance\n"))
  session['time'] = input("Add time taken\n")
  session['splits'] = []
  split = '0'
  
  for i in range(1, session['distance'] + 1):
    split = input(f"Add split for mile {i}\n")
    session['splits'].append(split)
  
  return session


def grade_splits(session):
  splits = session['splits']
  counter = 0

  if len(splits) <= 1:
      return f"Not enough splits, can't grade."

  for i in range(len(splits) - 1):
    if i <= 2:
      if splits[i + 1] <= splits[i]:
        counter += 1
      else:
        counter -= 1
    elif i >= 3 and i <= 6:
      if splits[i + 1] <= splits[i]:
        counter += 2
      else:
        counter -= 2
    else:
      if splits[i + 1] <= splits[i]:
        counter += 3
      else:
        counter -= 3

  grade = counter / len(splits) * 100
  if grade < 0:
    return f"You slowed down a bit, could use improvement. Grade: {grade}"
  elif grade == 0:
      return f"Good job, you maintained your pace. Grade: {grade}"
  else:
    return f"Great job, you killed it! Grade: {grade}"


# if mile #2 is <= mile #1, then add 1 to counter, else subtract 1 from counter.
# if mile #5 is <= mile #4, then add 2 to counter, else subtract 2 from counter.
# if mile #8 is <= mile #7, then add 3 to counter, else subtract 3 from counter.

# negatives are bad, positives are good. the more negative, the worse the run grade
# the better the run, the more positive the grade
# how to calculate grade from overall counter value compared to distance
# grade = counter / distance * 100
# dummy data = 5 miles, 60 minutes, splits = [10, 12, 14, 11, 13]
#                                             0   -1  -3   1   -3 final grade -3
# -3 / 5 = -0.6
# 3 / 5 = 0.6
#
# dummy data = 5 miles, 30 minutes, splits = [5, 6, 7, 6, 6]
#                                            0  -1 -3 -1  1 final grade 1
# -1 / 5 = -0.2
# 1 / 5 = 0.2
# 
# dummy data = 5 miles, 90 minutes, splits = [15, 16, 18, 19, 22]
#                                             0   -1  -3  -5  -7 final grade -7
# -7 / 5 = -1.4
# 7 / 5 = 1.4

# dummy data = 12 miles, 150 minutes, splits = [10, 12, 14, 11, 13, 15, 12, 14, 16, 13, 15, 17]
#                                               0   -1  -3   1  -1  -3   0  -3  -6  -3  -6  -9 final grade -9
# -9 / 12 = -0.75
# 9 / 12 = 0.75



def miles_to_km(distance):
  return float(distance * 1.6)


def km_to_miles(distance):
  return float(distance * 0.621371)
  
main()

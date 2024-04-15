# race-performance-sim
Race day predictor based on training run data using Python.

High level design:
- Collect running data, for starters - distance + time ran + splits (time per mile)
- Grade the splits. 0 value for first split, then increasing + or - value the more splits there are
- Store race day distance
- Calculate simulated race day performance using split grade curve average applied to race day distance


1. Collect running data
   
Input 1 training session:  distance + time
```python
def session(distance, time, splits):
  distance = input("Add distance")
  time = input("Add time taken")
  splits = []
  for i in range(0, distance):
    split = split[i]
    split = input(f"Add split for {i} mile")
    splits.append(split[i])
  session = {distance, time, splits[i]}
  return session
  # need to store this into a database as an entry

def time_convert(time):
  # need to convert time into a standard metric based on input hours/minutes

def distance_conversion(distance):
  # need to convert miles to KM based on input of mileage
```

2. grade the splits
```python
def grade_splits(splits):
  counter = 0
  # this method grades values given
  # index and split given by grade_split
  for i in range(0, len(splits)):
    split = split[i]
    if i <= 2:
      if split[i + 1] <= split[i]:
        counter += 1
      else:
        counter -= 1
    if i >= 3 and i <=6:
      if split[i + 1] <= split[i]:
        counter += 2
      else:
        counter -= 2
    if i >= 7:
      if split[i + 1] <= split[i]:
        counter += 3
      else:
        counter -= 3

  return counter


def process_splits(splits, counter):
  graded_splits = []
  final_grade = 0
  """
    here i need to take the splits and index them into a tuple {index, split_time, grade}
    then, i need to assign a +/- value based on the split index, which compares itself to the previous split
    then calculate and return the grade total
  """
  for index, split in enumerate(splits):
    # index, time, run grade_splits(splits)
    # calculate and return grade total
    graded_splits.append(index, split, counter)
    for grade[2] in graded_splits:
      final_grade += grade[2]

    return final_grade
```

3. store race day distance

```python
def race(distance):
  return race_distance = input("enter race distance")
```

4. calculate race day performance
```python
def split_average(sessions):
  for session in sessions:
    # add up and average all the splits
  return split_average

def distance_average(sessions):
  for session in sessions:
    # add up and then average all the distances
  return distance_average


def simulator(race_distance, final_grade, distance_average, split_average):
  # so if i have the full race distance, i.e. 10 miles
  # and i have the grade. i need to do a few things
  ### compare distance average for training to race distance
  ### assign percentage 
  ### take final grade score and multiply by percentage = race_diff
  ### use split average as starting split, then add race_diff exponentially to each split needed to
    # complete race distance



class Race():
  def simulator():

  def race():

class Training(Race):
  def session():

class Splits(Training):
  def grade_splits():

  def process_splits():

  def split_average():

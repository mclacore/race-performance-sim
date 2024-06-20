def main():
  print("Welcome to the running app")
  session = session()
  grade_splits(session)
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
  
  print(session)
  return session


def grade_splits(session):
  splits = session['splits']
  counter = 0
  for i in range(0, len(splits)):
    split = splits[i]
    if i <= 2:
      if split[i + 1] <= split[1]:
        counter += 1
      else:
        counter -= 1
    elif i >= 3 and i <= 6:
      if split[i + 1] <= split[1]:
        counter += 2
      else:
        counter -= 2
    else:
      if split[i + 1] <= split[1]:
        counter += 3
      else:
        counter -= 3
  return counter


def miles_to_km(distance):
  return float(distance * 1.6)


def km_to_miles(distance):
  return float(distance * 0.621371)
  
main()

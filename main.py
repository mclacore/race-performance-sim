def main():
  session = {}
  session['distance'] = int(input("Add distance\n"))
  session['time'] = input("Add time taken\n")
  session['splits'] = []
  split = '0'
  
  for i in range(1, session['distance'] + 1):
    split = input(f"Add split for mile {i}\n")
    session['splits'].append(split)
  
  return session


def miles_to_km(distance):
  return float(distance * 1.6)


def km_to_miles(distance):
  return float(distance * 0.621371)
  
main()
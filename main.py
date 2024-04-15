def session():
  session = {}
  session['distance'] = int(input("Add distance\n"))
  session['time'] = input("Add time taken\n")
  session['splits'] = []
  split = "0"
  for i in range(0, session['distance']):
    split = split[i]
    split = input(f"Add split for {i} mile\n")
    session['splits'].append(split)
  print(f"distance is {session['distance']} and time is {session['time']}")
  print(session)
  
  
session()
def session():
  session = {}
  session['distance'] = int(input("Add distance\n"))
  session['time'] = input("Add time taken\n")
  session['splits'] = []
  split = '0'
  
  for i in range(1, session['distance'] + 1):
    split = input(f"Add split for mile {i}\n")
    session['splits'].append(split)
  
  print(f"distance is {session['distance']} and time is {session['time']}")
  print(session)
  
  
session()
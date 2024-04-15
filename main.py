def session():
  distance = int(input("Add distance\n"))
  time = input("Add time taken\n")
  splits = []
  split = "0"
  for i in range(0, distance):
    split = split[i]
    split = input(f"Add split for {i} mile\n")
    splits.append(split)
  print(f"distance is {distance} and time is {time}")
  print(splits)
  
session()
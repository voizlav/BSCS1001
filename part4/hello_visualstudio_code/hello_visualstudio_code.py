while True:
  get_editor = input("Editor: ").lower()
  if get_editor in ["word", "notepad"]:
    print("awful")
  elif get_editor == "visual studio code":
    print("an excellent choice!")
    break
  else:
    print("not good")
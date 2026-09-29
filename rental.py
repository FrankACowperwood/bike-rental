from bicycle import bicycles
def rent_bicycle(bicycle_id):
    found = False
    for bicycle in bicycles:
     if bicycle["id"] == bicycle_id:
      found = True
      if bicycle["status"] == "available":
            bicycle["status"] = "rented"
            print("Велосипед успешно арендован")

      elif bicycle["status"] == "rented":
            print("Велосипед недоступен")
    if found == False:
     print("Велосипеда нет")
def show_available_bicycles():
   print("Доступные велосипеды:")
for bicycle in bicycles:
    if bicycle["status"] == "available":
        print(
            bicycle["id"],
            bicycle["brand"],
            bicycle["type"],
            bicycle["price"]
        )
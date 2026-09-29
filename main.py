from rental import rent_bicycle, show_available_bicycles
show_available_bicycles()
bicycle_id = int(input("Введите ID велосипеда для аренды: "))
rent_bicycle(bicycle_id)

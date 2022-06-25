# WRITE YOUR FUNCTIONS HERE
from os import remove


def get_pet_shop_name(name):
    return name["name"]

def get_total_cash(sum):
    return sum["admin"]["total_cash"]

def add_or_remove_cash(cash, num):
    cash["admin"]["total_cash"] += num

def get_pets_sold(sold):
    return sold["admin"]["pets_sold"]

def increase_pets_sold(sold, amount):
    sold["admin"]["pets_sold"] += amount

def get_stock_count(count):
    return len(count["pets"])

def get_pets_by_breed(pet_shop, breed):
    count = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            count.append(pet["breed"])
    return count
    
def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet

def remove_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            pet_shop["pets"].remove(pet)

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)
    
def get_customer_cash(cash):
    return cash["cash"]

def remove_customer_cash(customer, amount):
    customer["cash"] -= amount

def get_customer_pet_count(pet_count):
    return len(pet_count["pets"])

def add_pet_to_customer(customer, new_pet):
    if customer["pets"] == []:
        customer["pets"].append(new_pet)







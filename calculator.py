def main():
    num_civ_factories = int(input("How many civilian factories do you need? "))
    factory_output = int(input("Do you want to have factory output 1, 2 or none of them? (1/2/0): "))
    use_psa = input("Do you want to use the Public Service Act (y/n)? ")
    multiplier = 1
    if factory_output == 1:
        multiplier *= 1.2
    elif factory_output == 2:
        multiplier *= 1.25
    num_electronics_factories = (num_civ_factories * 3 + 15) // 16
    num_motor_factories = (num_civ_factories * 2.5 + 5) // 6
    num_fertilizer_factories = (num_civ_factories * 2.5 + 11) // 12
    num_steel_factories = (num_motor_factories + 2) // 3
    total_cost = (num_civ_factories + num_electronics_factories + num_motor_factories + num_fertilizer_factories + num_steel_factories) * 25000000
    print("You need to build:")
    print("- {} electronics factories".format(num_electronics_factories))
    print("- {} motor factories".format(num_motor_factories))
    print("- {} fertilizer factories".format(num_fertilizer_factories))
    print("- {} steel factories".format(num_steel_factories))
    print("This will require:")
    print("- {} copper".format(num_electronics_factories * 2))
    print("- {} gold".format(num_electronics_factories * 2))
    print("- {} iron".format(num_steel_factories * 4))
    print("- {:.1f} titanium".format(num_steel_factories * 0.2))
    print("- {} photosphate".format(num_fertilizer_factories * 3.5))
    print("The total cost will be: ${:,.0f}".format(total_cost))
    print("The civilian factories will need:")
    print("- {} electronics".format(num_civ_factories * 3))
    print("- {:.1f} motor parts".format(num_civ_factories * 2.5))
    print("- {:.1f} fertilizer".format(num_civ_factories * 2.5))
    if use_psa == "y":
        multiplier *= 1.2
    consumer_goods = num_civ_factories * 40 * multiplier
    print("The total number of consumer goods produced will be: {:,.0f}".format(consumer_goods))

main()

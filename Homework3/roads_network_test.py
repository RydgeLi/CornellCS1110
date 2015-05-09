import roads_network
###################################
#  function to perform a travel   #
###################################
def Travel(roads, my_car):
    print('\n##################### A car is about to travel #####################')
    my_car.show_info()
    # find a path for the car before it goes
    roads.search(my_car.get_dep(), my_car.get_des(), [])
    journey = roads.get_search_journey()
    # show the path or nothing
    if len(journey) == 0:
        print('##################### there is no way you can get to there! #####################')
    else:
        print('##################### found a path for you: #####################')
        for item in journey:
            print(item.get_name())
        ############################# begin to travel #############################
        
        print('##################### ready to go! #####################\n')
        while not my_car.get_pos() == my_car.get_des().get_name():
            if my_car.isInTown():  # When car is in town, choose next road
                print('right now, the car is in', my_car.get_pos(), 'Town')
                for i in range(len(journey)):
                    if journey[i].get_name() == my_car.get_pos():
                        my_car.set_pos(journey[i].get_name() + journey[i + 1].get_name())
                my_car.set_status(False)
            else:  # when car is on road, just go to the other side of the road
                print('right now, the car is on', my_car.get_pos(), 'Road')
                my_car.set_pos(my_car.get_pos()[1])
                my_car.set_status(True)
        print('arrived! now the car is in', my_car.get_des().get_name(), 'Town')
    roads.clear_search_journey()
    
                            ######################
                            # test starts here   #
                            ######################
###################### define some towns: A(0), B(1), C(2), D(3), E(4), F(5), G(6), H(7), I(8), J(9) #############################
town_list = []
for i in range(65, 75):
    town_list.append(roads_network.Town(chr(i), []))
    
print(' ##################### Here is the list of towns: #####################')
for item in town_list:
    print(item.get_name())
    
##################### build up the road network #############################
road_system = roads_network.Network(town_list[0])
for i in range(1, 3):
    road_system.build(town_list[0], town_list[i])  # A-B A-C
for i in range(1, 8):
    road_system.build(town_list[i], town_list[i + 2])  # B-D C-E D-F E-G F-H G-I H-J
road_system.build(town_list[2], town_list[5])  # C-F
road_system.build(town_list[8], town_list[0])  # I-A

print('##################### Here is the road network: #####################')
road_system.show_network(road_system.root)

################### define two cars for test #############################
my_car1 = roads_network.Car('yl2489', 'Rydge', town_list[0], town_list[4])  # from A to E
my_car2 = roads_network.Car('2489', 'Yujie', town_list[2], town_list[7])  # from C to H
Travel(road_system, my_car1)
Travel(road_system, my_car2)

class Town:
    def __init__(self, name, next_town):
        self.name = name
        self.next_town = next_town
        
    def get_next_town(self):
        return self.next
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
     
class Network:
    def __init__(self, root):
        self.root = root
        self.road_list = []
        self.size = 0
        self.search_journey = []
    
    def build(self, town, new_town):
        town.next_town.append(new_town)
        new_town.next_town.append(town)
        self.road_list.append(town.get_name() + '<->' + new_town.get_name())
        self.size = self.size + 1
        
    def show_network(self, town, visited=[]):
        for road in self.road_list:
            print(road)
    
    # search the whole network to find a path.
    def search(self, dep, des, visited):
        if dep not in visited:
            visited.append(dep)
            self.search_journey.append(dep)
            if dep == des:
                return True
            if len(dep.next_town) > 0:
                for next_stop in dep.next_town:
                    if self.search(next_stop, des, visited):
                        return True
                self.search_journey.pop()
    
    def get_search_journey(self):
        return self.search_journey
    
    def clear_search_journey(self):
        self.search_journey.clear()
    
class Car:
    def __init__(self, number, driver, dep, des):
        self.number = number
        self.driver = driver
        self.dep = dep
        self.des = des
        self.pos = dep.get_name()
        self.in_town = True
    def show_info(self):
        print('            the No. of the car is', self.number, ', driver is', self.driver)
        print('            from', self.dep.get_name(), 'to', self.des.get_name())
    def isInTown(self):
        return self.in_town
    
    def set_status(self, flag):
        self.in_town = flag
    
    def get_dep(self):
        return self.dep
        
    def get_des(self):
        return self.des
    
    def get_pos(self):
        return self.pos
     
    def set_pos(self, pos):
        self.pos = pos


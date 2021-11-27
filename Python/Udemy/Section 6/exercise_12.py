# inheritance of list on a class we made.
class SuperList(list):
    def __len__(self):
        return 1000
    
super_list_1 = SuperList()
print(len(super_list_1))
super_list_1.append(5)
print(super_list_1[0])
print(issubclass(SuperList, list))
print(issubclass(SuperList, object))

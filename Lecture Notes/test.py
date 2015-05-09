def change(attr):
    attr.clear();
    attr = [];

test = [1, 1];
change(test);
print(test)
# print(test)

def show_tree(root):
    if root.left:
        show_tree(root.left);
    print(root);
    if root.right:
        show_tree(root.right);
        
class private:
    def __init__(self):
        self.one = 1
        self._two = 2
        self.__three = 3  # private
        
    def get_hidden(self):
        return self.__three

funny = private()

print(funny.one)
print(funny._two)
print(funny.get_hidden())

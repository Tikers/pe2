from inspect import stack


class Stack:
    def __init__(self):
        self.__stack_list = []
        # print("Hi!")

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

    def print_stack(self):
        print(self.__stack_list)


class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val

    def get_sum(self):
        return self.__sum




stack_object = AddingStack()

stack_object.push(1)
stack_object.push(3)
stack_object.push(8)

stack_object.print_stack()

print("pop: ", stack_object.pop())
stack_object.push(12)

stack_object.print_stack()

print(stack_object.get_sum())

#print(not 23)
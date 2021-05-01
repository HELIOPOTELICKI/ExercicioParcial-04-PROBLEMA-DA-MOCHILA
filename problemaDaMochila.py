import timeit
import sys

sys.setrecursionlimit(100000)


#=========================================== Item ===========================================#
class Item:
    def __init__(self, item_weight, item_value):
        self.item_weight = item_weight
        self.item_value = item_value

    def getItem_weight(self):
        return int(self.item_weight)

    def getItem_value(self):
        return int(self.item_value)


#=========================================== Backpack ===========================================#
class Backpack:
    def __init__(self, weight):
        self.weight = weight

    def getWeight(self):
        return int(self.weight)

    def recursive(self, value, weight, item_list_size, capacity):
        if (item_list_size == 0 or capacity == 0):
            return 0

        else:
            if (weight[item_list_size - 1] > capacity):
                return self.recursive(value, weight, item_list_size - 1,
                                      capacity)
            else:
                use = value[item_list_size - 1] + self.recursive(
                    value, weight, item_list_size - 1,
                    capacity - weight[item_list_size - 1])

                doNotUse = self.recursive(value, weight, item_list_size - 1,
                                          capacity)
                return max(use, doNotUse)

    def insertRecursive(self, item_list):
        if (len(item_list) == 0):
            return 'Lista vazia'

        value = []
        weight = []
        item_list_size = len(item_list)
        capacity = int(self.getWeight())

        for item in item_list:
            value.append(int(item.getItem_value()))
            weight.append(int(item.getItem_weight()))

        return self.recursive(value, weight, item_list_size, capacity)

    def insertBottomUp(self, item_list):

        backpack = [[0] * (self.getWeight() + 1)]

        for i, item in enumerate(item_list, start=1):
            backpack.append([0] * (self.getWeight() + 1))

            for weight in range(1, self.getWeight() + 1):
                if item.getItem_weight() <= weight:
                    if backpack[i - 1][weight] > backpack[i - 1][
                            weight -
                            item.getItem_weight()] + item.getItem_value():
                        backpack[i][weight] = backpack[i - 1][weight]
                    else:
                        backpack[i][weight] = backpack[i - 1][
                            weight -
                            item.getItem_weight()] + item.getItem_value()
                else:
                    backpack[i][weight] = backpack[i - 1][weight]

        i, backpackCapacity = len(item_list), self.getWeight()
        output = []

        while backpackCapacity > 0:
            if backpack[i][backpackCapacity] != backpack[i -
                                                         1][backpackCapacity]:
                output.append(item_list[i - 1])
                backpackCapacity = backpackCapacity - item_list[
                    i - 1].getItem_weight()

            i -= 1

        return backpack[-1][-1]


#=========================================== Main ===========================================#
def createListOfItems(text):
    item_list = []

    for i in range(0, len(text)):
        newItem = text[i].replace('\t', ',')
        newItem = newItem.split(',')
        item = Item(newItem[0], newItem[1])
        item_list.append(item)

    return item_list


folder = 'entry'
entryList = [
    'Teste.in', 'mochila1000.in', 'mochila5000.in', 'mochila10000.in',
    'mochila20000.in', 'mochila100000.in'
]

# Define o arquivo de entrada [0 - 5]
entry = entryList[1]

text = open(f'{folder}\\{entry}', 'r')
text = text.read()

text = text.splitlines()
backpack = Backpack(text[0])
del text[0]

item_list = createListOfItems(text)

# POR PROGRAMAÇÃO DINÂMICA
start = timeit.default_timer()
value_max = backpack.insertBottomUp(item_list)
end = timeit.default_timer()

print(
    f'\nMochila Bottom Up: arquivo -> {entry}, pode levar R${value_max},00 em itens'
)
print('Tempo de execução: %f segundos' % (end - start))

# POR RECURSÃO
start = timeit.default_timer()
value_max = backpack.insertRecursive(item_list)
end = timeit.default_timer()

print(
    f'\nMochila Recursiva: arquivo -> {entry}, pode levar R${value_max},00 em itens'
)
print('Tempo de execução: %f segundos' % (end - start))
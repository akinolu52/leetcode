list1 = ['little', 'blue', 'widget']
list2 = ['there', 'is', 'a', 'little', 'blue', 'cup', 'on', 'the', 'table']

list3 = set(list1) & set(list2)

list4 = sorted(list3, key=lambda k: list1.index(k))

print(list4)


# {'o', 'a', 'r', 'l', 'e', 'b'}

        # for word in words:
        #     word_list += list(word)
        #     word_set.update(word_list)
        #     # word_list.append(list(word))
        #     # word_set.add(list(word))
        # # word_list = [word_set.update(word_list)]

        # result = []
        # for x in word_set:
        #     w_l = list(word)
        #     if x in list(words):
        #         result.append(x)

        # # print(word_set, word_list)
        # return result

        # abel
        # abel
        # elor

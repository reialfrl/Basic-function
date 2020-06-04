if __name__ == "__main__":

    def sub_list(list_x, list_y):

        final_list = []
        if len(list_x) > len(list_y):
            return final_list
        else:
            for i in list_x:
                if i in list_y:
                    final_list.append(i)

        return final_list

final_list = sub_list([1, 2, 3, 4, 5, 6, 7, 8],  [
                      10, 25, 52, 80, 1, 46, 6, 33, 14, 27, 19])
print(final_list)

import os, random
def generate_file(file_prefix=""):
    for i in range(1, 6):
        filename = f"{file_prefix}{i}.txt"
        print(filename)
        with open(filename, 'w+') as f:
            f.writelines("col1,col2\n")
            for i in range(1, 101):
                line_s = f"{i},{i*i}\n"
                f.writelines(line_s)

            print(f"{os.path.abspath('.')}{os.sep}{filename}")

# generate_file("text_file_")

def read_file(filepath):
    alist = []
    with open(filepath, "r") as f:
        for i in f:
            if "col" not in i:
                i = i.replace("\n", "")
                a_t = tuple(i.split(","))
                alist.append(a_t)

    print(alist)

    # 2.extract only col2
    col_keys_list = [int(y[1]) for y in alist ]
    print(col_keys_list)

    # 3. shuffle list
    random.shuffle(col_keys_list)
    # 4. sort the shuffled_list
    col_keys_list.sort(reverse=True)

    print("===============")
    print(col_keys_list)
    # 2nd largest
    print(col_keys_list[1])
    # 3rd smallest
    print(col_keys_list[-3])

    # sum_odd
    odd_values = [j for j in col_keys_list if j % 2 != 0]
    even_values = [j for j in col_keys_list if j % 2 == 0]

    odd_sum = sum(odd_values)
    even_sum = sum(even_values)
    print(f"odd_sum={odd_sum}")
    print(f"even_sum={even_sum}")

# read_file(filepath="./text_file_1.txt")


def count_words(filepath):
    lines_list = []
    with open(filepath, "r+") as f:
        for i in f:
            if i:
                lines_list.append(i)
    print(lines_list)
    print(len(lines_list))
    words_list = []
    for i in lines_list:
        word = i.split(" ")
        words_list += word

    print(f"words_list=={words_list}")
    set_words = set(words_list)
    adict = {}
    for k in set_words:
        adict[k] = words_list.count(k)


    print(adict)
    return adict

# count_words("./third_text.txt")


def filter_word_count(adict, threshold_value= 3):
    new_dict = {}
    for key, value in adict.items():
        if value>=threshold_value:
            new_dict[key] = value

    return  new_dict

print(filter_word_count(count_words("./third_text.txt")))


class GenerateInt:
    def __init__(self, n):
        self.n = n

    def generate_random_num(self):
        alist = []
        for i in range(self.n):
            alist.append(random.randrange(0, 100000))

        return alist

    def drop_duplicates(self, alist):
        print(f"the originally generated random numbers:{alist}")
        # drop duplicates
        new_list = list(set(alist))
        new_list.sort()

        return new_list


ainstance = GenerateInt(3)
random_list = ainstance.generate_random_num()
print(ainstance.drop_duplicates(random_list))

































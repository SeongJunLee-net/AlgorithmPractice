def Solution():
    n = input()
    data = input()
    data_list = list(data)
    data_list = map(int, data_list)
    return sum(data_list)
if __name__ == "__main__":
    print(Solution())
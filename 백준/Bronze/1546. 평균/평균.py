def Solution():
    n = int(input())
    data = input()
    data_list = data.split(" ")
    data_list = list(map(int,data_list))
    maximum = max(data_list)
    result = list(map(lambda x: (x/maximum)*100,data_list))

    summation = sum(result)
    return summation/n
if __name__ == "__main__":
    print(Solution())
if __name__ == '__main__':
    n = int(input().strip())
    if 1 <= n <= 150:
        for i in range(1, n + 1):
            print(i)
    else:
        print("Angka lebih dari 150")
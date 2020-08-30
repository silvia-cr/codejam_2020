import time


def main():
    t = int(input())

    for i in range(1, t+1):
        n = input()

        print('Case #{0}: {1}'.format(i, n))


if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print('-- {0} seconds --'.format(end_time - start_time))

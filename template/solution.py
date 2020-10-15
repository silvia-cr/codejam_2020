import time

import psutil


def main():
    t = int(input())

    for x in range(1, t + 1):
        n = int(input())

        print('Case #{0}: {1}'.format(x, n))


if __name__ == '__main__':
    start_mem = psutil.virtual_memory().available
    start_time = time.time()
    main()
    end_time = time.time()
    end_mem = psutil.virtual_memory().available
    print('-- {0} seconds --'.format(end_time - start_time))
    print('-- {0} bytes --'.format(end_mem - start_mem))

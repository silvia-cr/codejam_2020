import time

import psutil


def main():
    t = int(input())

    for x in range(1, t + 1):
        n = int(input())

        k = 0
        r = 0
        c = 0
        col = list()

        for i in range(n):
            row = list(map(int, input().split()))

            k += row[i]
            r += 1 if len(row) != len(set(row)) else 0

            for idx, val in enumerate(row):
                if idx >= len(col):
                    col.append(list())

                col[idx].append(val)

        for val_list in col:
            c += 1 if len(val_list) != len(set(val_list)) else 0

        print('Case #{0}: {1} {2} {3}'.format(x, k, r, c))


if __name__ == '__main__':
    start_mem = psutil.virtual_memory().available
    start_time = time.time()
    main()
    end_time = time.time()
    end_mem = psutil.virtual_memory().available
    print('-- {0} seconds --'.format(end_time - start_time))
    print('-- {0} bytes --'.format(end_mem - start_mem))

import time

import psutil


def main():
    t = int(input())

    for x in range(1, t + 1):
        s = input()

        open = 0
        output = ''
        for n in s:
            while open < int(n):
                output += '('
                open += 1

            while open > int(n):
                output += ')'
                open -= 1

            output += n

        while open:
            output += ')'
            open -= 1
        
        print('Case #{0}: {1}'.format(x, output))


if __name__ == '__main__':
    start_mem = psutil.virtual_memory().available
    start_time = time.time()
    main()
    end_time = time.time()
    end_mem = psutil.virtual_memory().available
    print('-- {0} seconds --'.format(end_time - start_time))
    print('-- {0} bytes --'.format(end_mem - start_mem))

import sys

def main():
    N = 100
    print(f'{N = }', file=sys.stderr)
    for i in range(1, N + 1):
        if i % 3 == 0 and i % 5 == 0:
            print('fizzbuzz')
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else:
            print(i)

    print(f'Finish!!', file=sys.stderr)

if __name__ == '__main__':
    main()
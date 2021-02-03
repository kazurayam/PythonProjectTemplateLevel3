def execute(name='World'):
    print(f'Hello, {name}!')


def main():
    import sys
    arg1 = sys.argv[1]
    execute(arg1)


if __name__ == "__main__":
    main()
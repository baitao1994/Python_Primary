def main():
    file = input('Enter:').strip()
    with open(file,'r') as infile:
        a = infile.readlines()
        print(a[1])
        print(a)
main()

import sys

def validation(argv):
    print(argv[1])
    print(argv[2])

if __name__ == '__main__':
    print ('Start Validation...')
    validation(sys.argv[1:])
    print ('Validation Finished!')
    sys.exit(0)
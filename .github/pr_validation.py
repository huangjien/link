import sys

def validation(argv):
    print(argv[0])


if __name__ == '__main__':
    print ('Start Validation...')
    validation(sys.argv[1:])
    print ('Validation Finished!')
    sys.exit(0)
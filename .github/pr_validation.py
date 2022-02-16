import sys
import json

def validation(argv):
    print(argv[0])
    f = open (argv[0])
    data = json.loads(f.read())
    print(data['pull_request']['title'])
    print(data['changes']['title']['from'])


if __name__ == '__main__':
    print ('Start Validation...')
    validation(sys.argv[1:])
    print ('Validation Finished!')
    sys.exit(0)
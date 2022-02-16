import sys
import os
import json

def validation(argv):
    print(argv[0])
    # check if file exist
    if not os.path.exists(argv[0]):
        print ('important file: ' + argv[0] + ' not exist!')
        return False
    f = open (argv[0])
    data = json.loads(f.read())
    title = data['pull_request']['title']

    state = data['pull_request']['state']
    print('PR state: ' + state)
    # title must match some rules:
    
    if 'changes' not in data:
        return True
    if 'title' not in data['changes']:
        return True
    if 'from' not in data['changes']['title']:
        return True
    old_title = data['changes']['title']['from']
    # title changed, now we check them
    if title.split(' ')[0] != old_title.split(' ')[0]:
        return False
    return True


if __name__ == '__main__':
    print ('Start Validation...')
    result = validation(sys.argv[1:])
    
    if result :
        print ('Validation Finished!')
        sys.exit(0)
    else :
        print ('Validation Failed: JIRA No. Changed.')
        sys.exit(1)
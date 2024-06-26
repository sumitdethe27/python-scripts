# List all the container and describe them
import subprocess
from docker_ops import Docker
row='{print $1}'
describe_container="docker ps | awk  'NR=={cmds.get(container_number)}' | awk "
cmds={
    'container_list': 'docker ps',
    'container_stop': 'docker stop',
    'container_inspect': 'docker inspect',
    'view_images': 'docker images',
    'describe_container': describe_container 
}


def list(docker):
    result=docker.listcontainer()
    
    print(result)

def output(cond,ops):
    if cond:
        print("writing on output.txt file")
        with open('output.txt', 'a') as file:
            file.write(ops)
            file.write('\n')
            file.write('===========================================================================================')
            file.write('\n')
            file.close()
    return

def actions(docker):
    record_input=input('''Do you want to record the output in output.txt file
                       (y/n) :  ''' )
    
    if(record_input == 'y' or record_input=='Y'):
        record_input=True
        print("Output will be recorded")
    else:
        record_input=False
        print('Output not recorded')
    
    action=int(input('''
    What actions you want to perfrom 
    (1)  Stop the Container
    (2) Inspect the container          
    (3) No actions
    '''))
    ops=docker.containeroperation(action)
    output(record_input,ops)    
    print(ops)
def images(docker):
    result=docker.images()
    print(result)
def validate_user_input(user_input,ops)-> bool:
    if  user_input > -1 and user_input < len(ops):
        return True
    else:
        return False 
def takeinput(ops):
    user_input=int(input('''
    Enter actions 
    (1) List all the container
    (2) Interact with Containers
    (3) List images
    '''))
    if not validate_user_input(user_input,ops) :
        print("Invalid Input")
        takeinput(ops)
    return user_input-1

def main():
    docker=Docker(cmds,describe_container)
    ops=[list,actions,images]
    user_input=takeinput(ops)

    ops[user_input](docker)
    # list(docker)
    # actions(docker)
    
if __name__=='__main__':
    main()
# container_number= int(input("Enter the serial num of the container "))
 

# action=input('''
# What actions you want to perfrom 
# (1)  Stop the Container
# (2) Inspect the container          
        
# ''')


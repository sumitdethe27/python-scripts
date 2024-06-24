# List all the container and describe them
import subprocess
cmds={
    'container_list': 'docker ps',
    'describe_container': f'''{cmds.get('container_list') | grep }'''
}
result=subprocess.run([cmds.get('container_list')  ], shell=True,capture_output=True, text=True)

print(cmds.get(describe_container))
print(type(result.stdout))


print(result.stdout)


import subprocess
class Docker:
    def __init__(self,cmds,describe_container) -> None:
       self.cmds=cmds
       self.describe_container=describe_container


    def listcontainer(self):
        result=subprocess.run([self.cmds.get('container_list')  ], shell=True,text=True,capture_output=True)
        return result.stdout
    
    def containeroperation(self,action):
        print(self.listcontainer())
        if(action==1):
            containernumber=input("Enter the Container ID ")
            result=subprocess.run([ f"{self.cmds.get('container_stop')} {containernumber} "  ], shell=True,text=True,capture_output=True)
            
            return result.stdout
        elif action==2:
            containernumber=input("Enter the Container ID ")
            result=subprocess.run([ f"{self.cmds.get('container_inspect')} {containernumber} "  ], shell=True,text=True,capture_output=True)    
            return result.stdout
        else:
            print("no actions performed")
            
        return 1
    def images(self):
        result=subprocess.run([f"{self.cmds.get('view_images')} "],shell=True,capture_output=True,text=True)
        return result.stdout    
            
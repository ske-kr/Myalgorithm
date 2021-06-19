servers=[10,63,95,16,85,57,83,95,6,29,71]
tasks=[70,31,83,15,32,67,98,65,56,48,38,90,5]

servers_ok=[0 for _ in range(len(servers))]
clk=0
result=[]
servers_index=[]
task_left=0
mytask=[tasks[0]]
for i in range(len(servers)):
    servers_index.append([servers[i],i])
servers_index.sort(key=lambda x:x[0])
while len(mytask)>0:
    if(clk>=12):
        print(clk,servers_ok)
        print("left tasks:",mytask)
    for i in range(len(servers)):
        if clk >= servers_ok[i]:
            result.append(servers_index[i][1])
            servers_ok[i]=clk+mytask[-1]
            mytask.pop()
            if len(mytask)==0:
                break
                    
    clk+=1
    if clk<len(tasks):
        mytask.append(tasks[clk])

print(result)
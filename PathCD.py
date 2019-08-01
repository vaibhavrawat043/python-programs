class Path:
    def __init__(self, path):
        self.currentPath = path

    def cd(self, new_path):
        i=0;
        newPathList=new_path.split('/')
        pathLength=len(newPathList)
        pathList=self.currentPath.split('/')
        #print(newPathList)
        if newPathList[0]=='':
            #direct pathname
            del pathList[:]
            pathList.append('/'+newPathList[1])
            i=i+2
        while(i<pathLength):
            j=len(pathList)-1
            if newPathList[i]=='..':
                #parent directory
                pathList.pop(j)
            else:
                pathList.append(newPathList[i])
            i=i+1
        self.currentPath="/".join(pathList)


path = Path('/a/b/c/d')
path.cd('../x')
print(path.currentPath)

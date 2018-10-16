#modernCV to HTML site
#Written by  Aakash Patil(https://github.com/aakash30jan) in September 2018.
#Problems? Please raise an issue at "https://github.com/aakash30jan/LatexToWebpage/issues" and I will get back to you.

texFile='./CV/LaTeX/main.tex'
htmlFile='index.html'


##########################################################
inFile=open(texFile,'r')
#
import datetime
today = datetime.date.today()
newDate=" {:%d %b, %Y} ".format(today)

print "#"*10  
##GET
projects=[]
for line in inFile:
    if line.startswith("\cventry{"):  #for all the projects
        #print line
        projects.append(line)
        
print "Total projects found in "+texFile+" : ", len(projects)        
projectsData=[]
for i in range(len(projects)):  
    #print "#"*10          
    location=projects[i][projects[i].find("{")+1:projects[i].find("}{")]      
    string=projects[i].replace(location,"") 
    string=string[string.find(":")+1:]
    supervisor= string[:string.find("}{")] 
    string=string[string.find("}{")+2:]
    title=string[:string.find("}{")]
    string=string[string.find("}{"):]
    string=string[string.find("}{")+2:]
    period=string[:string.find("}{")]
    location=location.replace(location[location.find("\\textsuperscript{"):location.find("}")+1],"") #remove this and do hyperlinking
    details=projects[i][projects[i].find("Details=")+8:projects[i].find(";")]
    image=projects[i][projects[i].find("Image=")+6: projects[i].find("Image=")+(projects[i][projects[i].find("Image="):].find(";"))].replace(' ','')
    URL=projects[i][projects[i].find("URL=")+4:projects[i].find("\n")]   
    #print title , supervisor,  location, period, details, URL
    projectsData.append([title , supervisor,  location, period, details, URL,image])
    
    
    
    
    
######PUT   
def cleanURL(URL):
    """ This function is not implemented properly ."""
    if URL.find("&")>1:
        Flag=True
        URL1=URL[ URL.find("\"")+1:URL.find("&")].replace("\""," ")
        URL2=URL[ URL.find("&")+1:].replace("\""," ")
        return [URL1,URL2], Flag;
    else:
        Flag=False
        return URL, Flag;

inFile=open(htmlFile,'r')
data=inFile.readlines()
for i in range(len(data)):
     if data[i].find("<!---- START SAMPLE PROJECT BLOCK")>-1 :
        blockFrom=i
     elif data[i].find("<!---- END SAMPLE PROJECT BLOCK")>-1 :
        blockTo=i
     elif data[i].find("<!--- START TO APPEND ALL PROJECT BLOCKS")>-1:
        AppendFrom=i  
     elif data[i].find("<!--- END TO APPEND ALL PROJECT BLOCKS")>-1:   
        AppendTo=i 
     elif data[i].find("Last Modified:")>-1 :        
        workString= data[i]
        upDate= workString[workString.find(":")+1:workString.find("<")]
        print "Previous update was on: ",upDate
        workString=workString.replace(upDate,newDate)
        data[i] = workString
         
def getORGblock():
    ORGblock=[]         
    for i in range(blockFrom,blockTo+1): #this is one project block
        #print data[i]
        ORGblock.append(data[i])
    return ORGblock;

AllBlocks=[]   
for j in range (0,len(projectsData)):   
    print "*"*10
    print "Supervisor: ",projectsData[j][1] 
    block=getORGblock()#ORGblock
    for i in range(0,len(block)):    
        if block[i].find("style='visibility:collapse'")>-1:
            block[i]=block[i].replace("style='visibility:collapse'"," ")
        
        elif block[i].find("'./website/images/project1.png'")>-1:
            block[i]=block[i].replace("'./website/images/project1.png'","'./website/images/"+projectsData[j][-1]+"'")
                
        elif block[i].find("papertitle")>-1:
            string=block[i]
            string=string[string.find(">")+1:string.find("</")]
            block[i]=block[i].replace(string,projectsData[j][0])
            
            
        elif block[i].find("Author 1")>-1:
            string=block[i]
            string=string[string.find(">")+1:string.find("</")]
            block[i]=block[i].replace(string,projectsData[j][1])
            
        elif block[i].find("Journal")>-1:
            string=block[i]
            string=string[string.find(">")+1:string.find("</")]
            block[i]=block[i].replace(string,projectsData[j][2])
             
        elif block[i].find("Period")>-1:
            string=block[i]
            string=string[string.find(">")+1:string.find("</")]
            block[i]=block[i].replace(string,projectsData[j][3])
            
        elif block[i].find("#URL")>-1:
        #    URLS, Flag=cleanURL(projectsData[j][5])
        #    if Flag: totalURLS= len(URLS)
        #    else: totalURLS=1
        #    for k in range(totalURLS):
                #print block[i]
                string=block[i]
                workstring=string[string.find("\"#")+1:string.find(">")].replace("\"","")
                #print block[i].replace(string,projectsData[j][3]) 
       #         if Flag:
       #             block[i]=block[i].replace(string,URLS[k])
       #         else:
       #             block[i]=block[i].replace(string,URLS)
                block[i]=block[i].replace(workstring,projectsData[j][5].replace("\"",""))
                #print block[i]      
                           
        elif block[i].find("Short Description")>-1:
            string=block[i]
            string=string[string.find(">")+1:string.find("</")]
            block[i]=block[i].replace(string,projectsData[j][4])
        
    print "Appended project: ",projectsData[j][0]    
                                       
    thisBlock= block[1:-1]    
    AllBlocks.append(thisBlock)
    
    
dataBackup=data[:] 
#remove everytime between AppendFrom to AppendTo
dataBackup[ AppendFrom+1:AppendTo]= "\n"
for i in range (len(projectsData)-1,0-1,-1):
    thisBlock=AllBlocks[i]
    dataBackup[AppendFrom+1:AppendFrom+1]=thisBlock

with open(htmlFile, 'w') as file:
    file.writelines( dataBackup ) 
file.close()
 
print "Done !"
print "#"*10  

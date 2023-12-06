import datetime
import time
 
print("Job begins")
 
with open("job-output.txt", "w") as output:
    output.write("%s\n" % datetime.datetime.now())
  
for i in range(0, 600):
    print("job %d" % (i))
    time.sleep(1)
    
print("Job ends")

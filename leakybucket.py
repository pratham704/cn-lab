from time import sleep

def leaky_bucket(packets,bucket_size,rate):
    bucket=0
    cycle=0
    
    for p in packets :
        
        if bucket+p>bucket_size:
           bucket=0
           cycle+=1
           print(f"Dropped {p}\tcycle {cycle} complete")
           sleep(1/rate)
           
           
        else:

            
            bucket+=p
            print(f"Packet sent {p}")
            
            
            
packets = [2, 3, 5, 6, 7, 9, 2, 8, 10, 11, 2, 4, 7, 5, 8, 9, 1, 3, 12]
bucket_size = 10
rate = 2
leaky_bucket(packets,bucket_size , rate)            
        
        
        
    
    
    

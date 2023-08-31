# Import STL libraries
import time
import threading

def process():
    """ Representing any process
    INPUTS:
        None
    OUTPUTS:
        None
    """
    print('Working on process...')
    #sleep process for 3 seconds
    time.sleep(3)
    print('Process completed!')

    return None

def main():
    #This function lustrates how to create a pool
    #INPUTS:
    #    None
    #OUTPUTS:
    #    None
    startTime = time.perf_counter()

    #Create an empty list to hold the thread pool
    threadPool = list()
    THREADPOOLSIZE = 1000

    #Loop through the thread pool (create & start each)
    for _ in range(THREADPOOLSIZE):
        #Create thread
        t = threading.Thread(target=process)
        #Create thread
        t.start()
        #Append current thread to thread pool
        threadPool.append(t)

    #Loop through the thread pool (join them all)
    for thread in threadPool:
        #Join current thread
        thread.join()

    #Get end time
    endTime = time.perf_counter()

    #Display total time taken by the two calls
    print(f'Process completed in {endTime-startTime} seconds(s)')


    return None
main()
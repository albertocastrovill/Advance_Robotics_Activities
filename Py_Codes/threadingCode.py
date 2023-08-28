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
    #Testing how sequential processes are completed
    #The total processing time is the addition of the
    #time it takes to solve each individual process
    #INPUTS:
    #    None
    #OUTPUTS:
    #    None
    startTime = time.perf_counter()
    
    #First call to process
    firstThread = threading.Thread(target=process)
    secondThread = threading.Thread(target=process)
    thirdThread = threading.Thread(target=process)

    #Start threads
    firstThread.start()
    secondThread.start()
    thirdThread.start()

    #Joing threads
    firstThread.join()
    secondThread.join()
    thirdThread.join()

    # Get end time
    endTime = time.perf_counter()
    print('Process completed in {} second(s)'.format(endTime-startTime))
    return None
main()
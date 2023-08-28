#import STL libraries
import time

def process():
    """ Representing any process
    INPUTS:
        None
    OUTPUTS:
        None
    """
    print('Working on process...')
    time.sleep(3)
    print('Process completed!')

    #return none
    return None
process()


def main():
    
    #Testing how sequential processes are completed
    #The total processing time is the addition of the
    #time it takes to solve each individual process
    #INPUTS:
    #    None
    #OUTPUTS:
    #    None

    # Get initial time
    startTime = time.perf_counter()
    # first call to process() function
    process()
    # second call to process() function
    process()

    # Get end time
    endTime = time.perf_counter()

    #display total time taken bt the two calls
    print('Process completed in {} second(s)'.format(endTime-startTime))

    return None
# call main function
main()

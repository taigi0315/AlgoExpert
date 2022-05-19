def minimumWaitingTime(queries):
    queries = sorted(queries)
    total_wait_time = 0
    wait_time = 0

    for q in queries:
       total_wait_time += wait_time
       wait_time += q
    
    return total_wait_time


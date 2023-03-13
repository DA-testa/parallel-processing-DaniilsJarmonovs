# python3
#Izstrādāja Daniils Jarmonovs, 18. grupa, 221RDC003
from queue import PriorityQueue

def parallel_processing(n, m, tasks):
    output = []
    threads = []
    for i in range(n):
        threads.append(False)
    totaltime = 0
    threadsWork = 0
    q = PriorityQueue()
    for i in range(m):
        current = threads.index(False)
        q.put((tasks[i]+totaltime, current))
        output.append((current, totaltime))
        threads[current] = True
        threadsWork += 1
        if(threadsWork == n):
            endedJob = q.get()
            threads[endedJob[1]] = False
            threadsWork -= 1
            if(endedJob[0] > totaltime):
                totaltime = endedJob[0]
    return output

def main():
    n = 0 #threads
    m = 0 #jobs/tasks
    tasks = []
    inp = input()
    if("I" in inp):
        counts = list(map(int, input().split()))
        n = counts[0]
        m = counts[1]
        tasks = list(map(int, input().split()))
    elif("F" in inp):
        FName = input()
        with open("./test/"+FName, mode="r") as file:
            counts = file.readline()
            counts = list(map(int, counts.split()))
            n = counts[0]
            m = counts[1]
            text = file.readline()
            tasks = list(map(int, text.split()))

    result = parallel_processing(n,m,tasks)
    for i in result:
        print(i[0], i[1])


if __name__ == "__main__":
    main()
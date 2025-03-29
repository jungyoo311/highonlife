# highonlife
정무의 취준 일기

# Hailort CLI Case Study
usage of CMAKE: Mange building across OS. Top level CmakeLists sets up the project and includes subdirectories for each component. Using Cmake with clearly separated modules is a best practice for scalability. It allows optional components and platform differences to be managed easily. 

# Testing and Continous Integration
`Catch2` provides a lightweight way to write test cases in C++.
`Jenkins` opensource automation server used for CI/CD `build-test-deploy` cycle.

Practicing integrating Github with Jenkins for automated builds and deployments.
Learning Docker and containerization for efficient deployment.

ad-hoc: when it's needed or necessary

# Testing HEF compiled NNM
"measure-nnc-performance.cpp/hpp"
1. Loads your .hef file
2. configure it to run directly on the hailo device
3. runs inference using hardward only execution (no input)
4. prepare benchmark table
5. output will be
```Starting HW infer Estimator...

======================
        Summary
======================
Batch count: 4
Total transfer size [KB]: 512
Total frames passed: 100
Total time [s]: 2.500
Total FPS [1/s]: 40.0
BW [Gbps]: 1.20
======================
    End of report
======================
```
low-latency: High BW
high-latency: low BW

# Difference Between sorted() and .sort()
list = [1,3,4,2]
1. sorted(list); Does NOT modify original height. Returns a new sorted list
2. list.sort(); Sorts the list in-place, it modifies height; Reutnrs None by python design;

list.sort()
list
will print out sorted list

# Depth First Search
Explore each branch completely before moving on to the next branch.
We go DEEP first before we go WIDE
pseudocode
```
def search(Node root):
    if root == null return # Base case: If input node is null, return null
    visit(root) # visit the node
    root.visited = true # Mark the current node as visited
    for each Node n in root.adjacent: # Loop through all the neighbors(adjacent nodes) of the current node
        if n.visited == false: # Check if the neighbor n has not been visited yet, if it hasn't been visited, explore it next.
            search(n) # recursively call search() on the neighbor n
```
# Breath First Search
Explore each neighbor before going on to any of their children.
We go WIDE before we go DEEP
pseudocode
```
def search(Node root):
    Queue queue = new Queue() # creates new Queue
    root.marked = true # Marks the root node as visited
    queue.enqueue(root) #  Add to the end of the queue # Adds the root node to the queue
    while !queue.isEmpty(): # While queue is not empty, keep exploring
        Node r = queue.dequeue() # Remove r from the front of the queue
        visit(r) # Processes the node
        for each Node n in r.adjacent: # iterates through each of node r's neighbors - the nodes it's directly connected to. 
            n.marked = true # marks neighbor node n as visited
            queue.enqueue(n) # Adds neighbor n to the back of the queue so it can be vistied in future iterations. 
```
from graph import Graph

def courseOrder(numCourses, prerequisites):
    """Return a course schedule according to the prerequisites provided."""

    graph = Graph(is_directed=True)

    course = [graph.add_vertex(each) for courses in prerequisites for each in courses]

    if numCourses != len(graph.get_vertices()):
        return []

    for each in prerequisites:
        graph.add_edge(each[1], each[0])

    return graph.topological_sort()
    # return graph

if __name__ == "__main__":

    courses1 = [ [1,0] ]
    assert courseOrder(2, courses1) == [0, 1]

    courses2 = [ [1,0], [2,0], [3,1], [3,2] ]
    possibleSchedules = [ [0, 1, 2, 3], [0, 2, 1, 3] ]
    assert courseOrder(4, courses2) in possibleSchedules

    print(courseOrder(4, courses2))


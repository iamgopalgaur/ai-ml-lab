class Graph:
    def __init__(self, adjac_list):
        self.adjac_list = adjac_list
    def get_neighbors(self,v):
        return self.adjac_list[v]
    def h(self, n):
        H={
            'A': 1,
            'B': 1,
            'C': 1,
            'D': 1
        }
        return H[n]
    def a_star_algorithm(self,start,stop):
        open_list=set({start})
        closed_list=set({})
        dist={}
        dist[start]=0
        par={}
        par[start]=start
        while len(open_list)>0:
            n=None
            for v in open_list:
                if n == None or dist[v] + self.h(v) < dist[n] + self.h(n):
                    n = v
            if n == None:
                print('path doesnt exist')
                return None
            if n == stop:
                reconst_path=[]
                while par[n]!=n:
                    reconst_path.append(n)
                    n=par[n]
                reconst_path.append(start)
                reconst_path.reverse()
                return print('Path found:{}'.format(reconst_path))
            for(m,weight) in self.get_neighbors(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    par[m]=n
                    dist[m]= dist[n]+weight
                else:
                    if dist[m]> dist[n]+weight:
                        dist[m]= dist[n]+weight
                        par[m]=n
                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)
            open_list.remove(n)
            closed_list.add(n)
        print("path doesnt exist")
        return None
adjac_list={
    'A':[('B',1),('C',3),('D',7)],
    'B':[('D',5)],
    'C':[('D',12)]
}
graph_1 = Graph(adjac_list)
graph_1.a_star_algorithm('A','D')
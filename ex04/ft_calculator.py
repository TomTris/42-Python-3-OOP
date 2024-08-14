class calculator:
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Count total value of the list"""
        li = 0
        i = 0
        for nbr in V1:
            li += V1[i] * V2[i]
            i += 1
        print(li)

    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Sum value of each element in the list"""
        li = []
        i = 0
        for nbr in V1:
            li.append(float(V1[i] + V2[i]))
            i += 1
        print(li)

    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Difference value of each element in the list"""
        li = []
        i = 0
        for nbr in V1:
            li.append(float(V1[i] - V2[i]))
            i += 1
        print(li)

import networkx as nx
import matplotlib.pyplot as plt

# Tạo đồ thị
G = nx.Graph()

# Thêm các đỉnh vào đồ thị
G.add_nodes_from([1, 2, 3, 4, 5])

# Thêm các cạnh vào đồ thị
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (4, 5)])

# Vẽ đồ thị
nx.draw(G, with_labels=True)
plt.show()

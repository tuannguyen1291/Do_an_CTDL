import networkx as nx
import matplotlib.pyplot as plt

# Tạo một đối tượng đồ thị
G = nx.DiGraph()

# Thêm các đỉnh
G.add_nodes_from(range(1, 6))

# Thêm các cạnh
G.add_edges_from([(1, 2), (2, 3), (3, 1), (3, 4), (4, 5), (5, 3), (5, 2)])

# Vẽ đồ thị
nx.draw(G, with_labels=True)

# Hiển thị đồ thị
plt.show()



class Graph {
	// TODO: Add conversion
	contructor(adjacency, incidence, list) {
		this.adjacency = adjacency;
		this.incidence = incidence;
		this.adjacency_list = list;
		// TODO: Depending on which of them is null set the rest
	}

	get_adjacency_matrix() {
		return adjacency;
	}

}

var get_matrix = (a, b) => Array.from(Array(a), () => Array.from(Array(b), () => 0));

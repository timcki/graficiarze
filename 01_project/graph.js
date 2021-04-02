

class Graph {
	// TODO: Add conversion
	constructor(nodes, adj, inc, list) {
		this.nodes = nodes;
		this.adjacency = adj;
		this.incidence = inc;
		this.adjacency_list = list;
		// TODO: Depending on which of them is null set the rest
	}

	get_pairs() {
		let ret = [];
		let len = this.adjacency.length;
		for (i = 0; i < len; i++)
			for (j = i+1; j < len; j++)
				if (this.adjacency[i][j] == 1) ret.push([i, j])

		console.log(ret);
		return ret;
	}

	test() {
		return "abc";
	}

}

var get_matrix = (a, b) => Array.from(Array(a), () => Array(b).fill(0));

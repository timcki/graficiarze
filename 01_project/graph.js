class Graph {
	// TODO: Add conversion
	constructor(nodes, adj, inc, list) {
		this.nodes = nodes;
		this.adjacency = adj;
		this.incidence = inc;
		this.adjacency_list = list;

		let arg = [adj, inc, list]
		//!() instead of != catch aslo undefine 
		let index = arg.findIndex(val => !(val == null))
		
		switch(index){
			case 0:
				this.incidence = adj_matrix_to_inc_matrix(this.adjacency)
				this.adjacency_list = adj_matrix_to_adj_list(this.adjacency)
				break;
			case 1:
				this.adjacency = inc_matrix_to_adj_matrix(this.incidence)
				this.adjacency_list = inc_matrix_to_adj_list(this.incidence)
				break;
			case 2:
				this.adjacency = adj_list_to_adj_matrix(this.adjacency_list)
				this.incidence = adj_list_to_inc_matrix(this.adjacency_list)
				break;
		}
	}

	get_pairs() {
		let ret = [];
		let len = this.adjacency.length;
		for (let i = 0; i < len; i++)
			for (let j = i+1; j < len; j++)
				if (this.adjacency[i][j] == 1) ret.push([i, j])

		//console.log(ret);
		return ret;
	}

	test() {
		return "abc";
	}

}

var get_matrix = (a, b) => Array.from(Array(a), () => Array(b).fill(0));

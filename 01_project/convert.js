transpose = m => m[0].map((x,i) => m.map(x => x[i]))

function adj_matrix_to_adj_list(matrix){
    let adjList = new Array(matrix.length).fill([]);
    for(let i = 0; i < matrix.length; i++){
        let tmp = [];
        for(let j = 0; j < matrix[i].length; j++){
            if (matrix[i][j] == 1){
                tmp.push(j);  
            }
        }
        adjList[i] = tmp;
    }

    return adjList;
}

function adj_list_to_adj_matrix(list){
    let adjMatrix = new Array(list.length).fill(0);
    for (let i = 0; i < list.length; i++)
        adjMatrix[i] = new Array(list.length).fill(0);

    for (let i = 0; i < list.length; i++)
        for(let j = 0; j < list[i].length; j++)
            adjMatrix[i][list[i][j]] = 1;
    
    return adjMatrix;
}

function adj_list_to_inc_matrix(list){
    let incMatrix = [];
    for(let node = 0; node < list.length; node++){
        for(let i = 0; i < list[node].length; i++){
            if(list[node][i] > node){
                let edge = new Array(list.length).fill(0)
                edge[node] = 1;
                edge[list[node][i]] = 1;
                incMatrix.push(edge);
            }    
        }
    }

    return incMatrix
}

function inc_matrix_to_adj_list(incMatrix){
    if(typeof incMatrix[0] == 'undefined'){
        console.log("catch")
        return new Array(incMatrix.length).fill([]);
    }
    let adjList = new Array(incMatrix[0].length);
    for(let i = 0; i < adjList.length; i++)
        adjList[i] = new Array(0)

    for(let edge = 0; edge < incMatrix.length; edge++){
        let first = incMatrix[edge].indexOf(1);
        let second = incMatrix[edge].indexOf(1, first+1);
        adjList[first].push(second);
        adjList[second].push(first);
    }
    
    return adjList;
}

function adj_matrix_to_inc_matrix(adjMatrix){
    return adj_list_to_inc_matrix(adj_matrix_to_adj_list(adjMatrix))
}

function inc_matrix_to_adj_matrix(incMatrix){
    return adj_list_to_adj_matrix(inc_matrix_to_adj_list(incMatrix))
}

function matrix_to_int_matrix(i, j, matrix){
    console.log(matrix)
}



function test_conversions(){
    let adjMatrix = [[0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0],
        [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1],
        [0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0]]

    console.log(adjMatrix)
    let adjList = adj_matrix_to_adj_list(adjMatrix)
    let incMatrix = adj_list_to_inc_matrix(adjList)
    console.log("adj -> list")
    console.log(adj_matrix_to_adj_list(adjMatrix))
    console.log("list -> adj")
    console.log(adj_list_to_adj_matrix(adjList))
    console.log("list -> inc")
    console.log(adj_list_to_inc_matrix(adjList))
    console.log("inc -> adj")
    console.log(inc_matrix_to_adj_list(incMatrix))
    console.log("adj -> inc")
    console.log(adj_matrix_to_inc_matrix(adjMatrix))
    console.log("inc -> adj")
    console.log(inc_matrix_to_adj_matrix(incMatrix))
}

//test_conversions()





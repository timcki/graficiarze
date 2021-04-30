function setValueAdj(element){
    console.log(element.value);
    element.value = +element.value % (+element.max + 1);
    let str = element.id;
    let words = str.split(',');
    let symetric = document.getElementById(words[1].slice(0,-1) + ',' + words[0] + 'f');
    symetric.value = element.value;
}

function setValueInc(element){
    element.value = +element.value % (+element.max + 1);
}

function setValueList(element){
    element.value = +element.value % (+element.max + 1);
}

function add_to_node(element){
    let str = element.id;
    let node = Number(str.slice(0,-1));

    let setTxt = document.getElementById(node + 'L').innerText;
    let setNumbers = setTxt.split(' ');
    for(let i = 0; i < setNumbers.length; i++)
        setNumbers[i] = +setNumbers[i];

    let set = new Set(setNumbers);

    let val = Number(document.getElementById(String(node) + 'V').value);
    console.log('Value: ' + val)
    if (val == node){
        alert("You can't link node to itself");
        return;
    }

    if(set.has(val)){
        alert("This edge already exist!");
        return;
    }

    setTxt = setTxt + ' ' + String(val);
    document.getElementById(node + 'L').innerText = setTxt;
    setTxt = document.getElementById(val + 'L').innerText;
    document.getElementById(val + 'L').innerText = setTxt + ' ' + String(node);

    document.getElementById("edgesInput").value = +document.getElementById("edgesInput").value + 1;

}


function create_adj_graph(){
    let n = Number(document.getElementById("nodesInput").value);

    let adj = get_matrix(n, n);
    for(let i = 0; i < n; i++)
        for(let j = 0; j < n; j++)
            adj[i][j] = document.getElementById(String(i) + ',' + String(j) + 'f').value;

    let l = 0;
    for(let i = 0; i < n; i++)
        for(let j = i; j < n; j++)
            l += Number(adj[i][j]);

    document.getElementById("edgesInput").value = l;
    let list = adj_matrix_to_adj_list(adj);
    
    let out = '<h2>Adjacency list <h2> <ol start=0>';
    for(let i = 0; i < list.length; i++){
        let str = list[i].toString(); 
        out +=  '<li>' + str + '</li>';
    }
    out += '</ol>';
    out += '<h2> Incidence Matrix</h2>';
    document.getElementById('firstOutput').innerHTML = out;
     
    let inc = adj_matrix_to_inc_matrix(adj);
    print_matrix(n, l, transpose(inc), 'secoundOutput');

    window.graph = new Graph(n, adj, null, null);
    draw_graph();
}

function draw_list_and_inc(adj, n) {
    let l = 0;
    for(let i = 0; i < n; i++)
        for(let j = i; j < n; j++)
            l += Number(adj[i][j]);
    let list = adj_matrix_to_adj_list(adj);
    
    let out = '<h2>Adjacency list <h2> <ol start=0>';
    for(let i = 0; i < list.length; i++){
        let str = list[i].toString(); 
        out +=  '<li>' + str + '</li>';
    }
    out += '</ol>';
    out += 'Incidence Matrix';
    document.getElementById('representations1').innerHTML = out;
     
    let inc = adj_matrix_to_inc_matrix(adj);
    print_matrix(n, l, transpose(inc), 'representations2');

    window.graph = new Graph(n, adj, null, null);
    draw_graph();
}

function create_inc_graph(){
    let n = Number(document.getElementById("nodesInput").value);
    let l = Number(document.getElementById("edgesInput").value);
    
    let inc = get_matrix(l, n);
    for(let i = 0; i < n; i++)
        for(let j = 0; j < l; j++)
            inc[j][i] = Number(document.getElementById(String(i) + ',' + String(j) + 'I').value);

    for(let edge = 0; edge < l; edge++)
        for(let previous = 0; previous < edge; previous++)
            if(inc[previous].toString() == inc[edge].toString()){
                alert("Edge defined twice! Edges: " + previous + ', ' + edge);
                return;
            }
                

    for(let i = 0; i < inc.length; i++){
        if(inc[i].reduce((a,b) => Number(a) + Number(b)) != 2){
            alert("Edge number: " + i + " doesn't link 2 nodes. Correct this in order to proceed.");
            return
        }
    }

    let list = inc_matrix_to_adj_list(inc);
    
    let out = '<h2>Adjacency list <h2> <ol start=0>';
    for(let i = 0; i < list.length; i++){
        let str = list[i].toString(); 
        out +=  '<li>' + str + '</li>';
    }
    out += '</ol>';
    out += '<h2> Adjacency Matrix</h2>';
    document.getElementById('firstOutput').innerHTML = out;
     
    let adj = inc_matrix_to_adj_matrix(inc);
    print_matrix(n, n, adj, 'secoundOutput');
    window.graph = new Graph(n, null, inc, null);
    draw_graph();
}

function draw_list_and_adj(inc, n){
    let list = inc_matrix_to_adj_list(inc);
    
    let out = '<h2>Adjacency list <h2> <ol start=0>';
    for(let i = 0; i < list.length; i++){
        let str = list[i].toString(); 
        out +=  '<li>' + str + '</li>';
    }
    out += '</ol>';
    out += '<h2>Adjacency Matrix</h2>';
    document.getElementById('representations1').innerHTML = out;
     
    let adj = inc_matrix_to_adj_matrix(inc);
    print_matrix(n, n, adj, 'representations2');
    window.graph = new Graph(n, null, inc, null);
    draw_graph();
}

function create_list_graph(){
    let n = Number(document.getElementById("nodesInput").value);
    

    let list = new Array(n);
    for(let i = 0; i < list.length; i++){
        let nodeEdges = document.getElementById(i + 'L').innerText.split(' ');
        if (nodeEdges[0] == "")
            nodeEdges = [];
        console.log(nodeEdges)
        for(let i = 0; i < nodeEdges.length; i++)
            nodeEdges[i] = +nodeEdges[i];
        
        list[i] = nodeEdges;
    }

    let l = 0;
    for(let i = 0; i < list.length; i++)
        l += list[i].length;
    l /= 2;
    console.log(l);
    
    let inc = adj_list_to_inc_matrix(list);
    let adj = adj_list_to_adj_matrix(list);

    
 
    print_matrix(n, n, adj,'firstOutput');
    let append = document.getElementById('firstOutput').innerHTML;
    append += '<h2>Incidence matrix<h2>';
    document.getElementById('firstOutput').innerHTML = append;
    document.getElementById('firstOutput').insertAdjacentHTML('afterbegin', '<h2>Adjacency matrix<h2>');
    try{
        print_matrix(n, l, transpose(inc), 'secoundOutput');
    }
    catch{
        let tmp = [];
        for(let i = 0; i < inc.length; i++)
            tmp.push([]);
        print_matrix(n, l, tmp, 'secoundOutput');
    }
    
         

    window.graph = new Graph(n, null, null, list);
    draw_graph();
}

function adj_form(n,l){
    const result = document.getElementById("inputGraph");
    let form = "";

    form += '<form id="inputField" role="form"></form>';
    for(let i = 0; i < n; i++){
        for(let j = 0; j < n; j++){
            let str =  String(i) + ',' + String(j) + 'f';
            if(i==j)
                form += '<input id=' + str + ' type="number" min=0 max=0 value=0' +
                ' style="all: initial" onChange="setValueAdj(this)">'
            else
                form += '<input id=' + str + ' type="number" min=0 max=1 value=0' +
                ' style="all: initial" onChange="setValueAdj(this)">'
        }
        form +="<br>"
    }
    form += '</form>';


    form += "<button onclick=create_adj_graph()>Draw graph</button>";

    result.innerHTML = form;
}

function list_form(n,l){
    const result = document.getElementById("inputGraph");
    let form = "<ol start=0>";

    for(let i = 0; i < n; i++){
        let str =  String(i) + 'L';
        form += '<li><span id=' + str +'> </span> <input id=' +
        String(i) + 'V' +' type="number" min=0 max=' +  String(n-1) +
        ' value=0 style="all: initial; background-color:yellow;" onChange="setValueList(this)">' + 
        '<button id='+ String(i) + 'B' + ' onclick=add_to_node(this)> Add </button></li>';
    }

    form += "</ol><button onclick=create_list_graph()>Draw graph</button>";

    result.innerHTML = form;
    document.getElementById("edgesInput").value = 0;
    
}

function inc_form(n,l){
    const result = document.getElementById("inputGraph");
    let form = "";

    form += '<form id="inputField" role="form"></form>';
    for(let i = 0; i < n; i++){
        for(let j = 0; j < l; j++){
            let str =  String(i) + ',' + String(j) + 'I';
            form += '<input id=' + str + ' type="number" min=0 max=1 value=0' + 
            ' style="all: initial" onChange="setValueInc(this)">'
        }
        form +="<br>"
    }
    form += '</form>';



    form += "<button onclick=create_inc_graph()>Draw graph</button>";

    result.innerHTML = form;
    result.innerHTML = form;
}

function gen_graph_input(){
    let n = Number(document.getElementById("nodesInput").value)
    let l = Number(document.getElementById("edgesInput").value)

    if (n < 0 || l < 0) {
        alert("Podaj liczby większe od 0")
        return
    }

    if (n*(n-1)/2 < l) {
        alert("Dla podanej liczby wierzchołków podana liczba krawędzi jest za duża")
        return
    }

    switch(document.getElementById("type").value){
        case "adj":
            adj_form(n,l);
            break;
        case "list":
            list_form(n, l);
            break;
        case "inc":
            inc_form(n, l);
            break;
    }
}

function showInput() {
    var input = document.getElementById("input");
	var random = document.getElementById("random");
	random.style.display = 'none';
	input.style.display = 'block';
}
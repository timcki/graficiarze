window.graph = null;

function gen_n_l() {

    let n = Number(document.getElementById("nodes").value)
    let l = Number(document.getElementById("edges").value)

    if (n < 0 || l < 0) {
        alert("Podaj liczby większe od 0")
        return
    }

    if (n*(n-1)/2 < l) {
        alert("Dla podanej liczby wierzchołków podana liczba krawędzi jest za duża")
        return
    }

    var matrix = get_matrix(l, n) // Macierz incydencji
    var nodes = get_matrix(n, n) // Macierz, w ktorej 1 oznacza, ze pomiedzy dwoma wierzcholkami jest juz krawedz

    for (j = 0; j < l; j++) {
        do {
            x = Math.floor(Math.random() * Math.floor(n));
            do { y = Math.floor(Math.random() * Math.floor(n)); } while (y === x)
        } while (nodes[x][y] === 1)

        nodes[x][y] = 1; nodes[y][x] = 1;
        matrix[j][x] = 1; matrix[j][y] = 1;
    }

    print_matrix(n, l, transpose(matrix), "result");

    
    // matrix = transpose(matrix);

    window.graph = new Graph(n, null, matrix, null)

}

function gen_n_p() {
   
    let n = Number(document.getElementById("nodes2").value)
    let p = Number(document.getElementById("prob").value)

    if (n < 0 || p < 0 || p > 1) {
        alert("Podaj n większe od 0, p z przedziału [0, 1]")
        return
    }

    let matrix = get_matrix(n, n) // Macierz sasiedztwa

    for (i = 0; i < n; i++)
        for (j = i+1; j < n; j++)
            matrix[i][j] = matrix[j][i] = +(Math.random() <= p);


    print_matrix(n, n, matrix, "result");
    window.graph = new Graph(n, matrix, null, null);
    console.log(window.graph.test());
    window.graph.get_pairs();
}


function print_matrix(a, b, matrix, idOut) {
    const result = document.getElementById(idOut)
    let table = "";
    if(idOut == "result")
        table += "<button onclick=draw_graph()>Draw graph</button>";
    table += "<table><tbody>";
    table += "<thead>";
    table += "<th></th>";

    for (j = 0; j < b; j++) table += "<th>" + j + "</th>";
    table += "</thead>";

    for (i = 0; i < a; i++) {
        table += "<tr>";
        table += "<td><b>" + i + "</b></td>";
        for (j = 0; j < b; j++)
            table += ("<td>"+ matrix[i][j] + "</td>");
        table += "</tr>";
    }

    table += "</tbody></table>"
    result.innerHTML = table;
}

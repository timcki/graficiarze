function gen_n_l() {

    n = document.getElementById("nodes").value
    l = document.getElementById("edges").value

    if (n < 0 || l < 0) {
        alert("Podaj liczby większe od 0")
        return
    }

    if (n*(n-1)/2 < l) {
        alert("Dla podanej liczby wierzchołków podana liczba krawędzi jest za duża")
        return
    }

    //macierz incydencji
    var matrix = getMatrix(n, l)
    
    //macierz, w ktorej 1 oznacza, ze pomiedzy dwoma wierzcholkami jest juz krawedz
    var nodes = getMatrix(n, n)

    for (j = 0; j < l; j++) {

        do {
            x = Math.floor(Math.random() * Math.floor(n));
            do {
                y = Math.floor(Math.random() * Math.floor(n));
            } while(y === x)
        } while(nodes[x][y] === 1)

        nodes[x][y] = 1;
        nodes[y][x] = 1;
        matrix[x][j] = 1;
        matrix[y][j] = 1;
    }

    console.log(matrix)

    printMatrix(n, l, matrix)

    return matrix
}

function gen_n_p() {
   
    n = document.getElementById("nodes2").value
    p = document.getElementById("prob").value

    if (n < 0 || p < 0 || p > 1) {
        alert("Podaj n większe od 0, p z przedziału [0, 1]")
        return
    }

    //macierz sasiedztwa
    var matrix = getMatrix(n, n)

    for (i = 0; i < n; i++) {
        for (j = i+1; j < n; j++) {
            if (Math.random() <= p) {
                matrix[i][j] = 1
            }
        }
    }

    for (i = 0; i < n; i++) {
        for (j = 0; j < i; j++) {
            matrix[i][j] = matrix[j][i]
        }
    }

    console.log(matrix)

    printMatrix(n, n, matrix)

    return matrix
}

function getMatrix(a, b) {
    var matrix = new Array(a)

    for (i = 0; i < a; i++) {
        matrix[i] = []
        for (j = 0; j < b; j++) {
            matrix[i].push(0)
        }
    }

    return matrix
}

function printMatrix(a, b, matrix) {
    result = document.getElementById("result")

    result.innerHTML = "<pre>";

    for (i = 0; i < a; i++) {
        for (j = 0; j < b; j++) {
            result.innerHTML += matrix[i][j] + " "
        }
        result.innerHTML += "<br/>"
    }

    result.innerHTML += "</pre>"
}
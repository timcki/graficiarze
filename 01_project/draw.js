function draw_graph() {
    // Set the content of the table to blank
    document.getElementById("result").innerHTML = "";
    //document.getElementById(
    // Generate the coordinates of the circles

    const points = gen_points(window.graph.nodes);

    // Init canvas and center it
    const canvas = document.getElementById('canvas');
    const context = canvas.getContext('2d');

    context.clearRect(0, 0, canvas.width, canvas.height);

    const cx = canvas.width / 2;
    const cy = canvas.height / 2;
    context.save();
    context.translate(cx, cy);

    draw_edges(points, context);
    draw_nodes(points, context);
    context.restore();
}

function gen_points(number) {

    const angle = 360 / number;
    const radius = 250;

    let points = [];
    for (var i = 0; i < number; i++)
        points.push([
            radius*Math.cos(deg2rad(angle*i)),
            radius*Math.sin(deg2rad(angle*i))
        ]);
        
    return points
}

function draw_nodes(points, context) {

    const r = 25; // Radius of the node
    points.forEach((val, i, arr) => {
      draw_circle(val[0], val[1], r, context);
      draw_text(val[0], val[1], i.toString(), context);
    });

}

function draw_edges(points, context) {
    const edges = window.graph.get_pairs();
    edges.forEach((val, i, arr) => {
      let n1 = val[0];
      let n2 = val[1];
      draw_line(points[n1][0], points[n1][1], points[n2][0], points[n2][1], context);
    })
    //points.forEach((val, i, arr) => draw_line(0, 0, val[0], val[1], context));

}

function draw_text(x, y, text, context) {
  y += 8; 
  console.log(text, text.length)
  if (text.length == 1) x -= 5;
  else x-= 10;

  context.save();
    context.font = "20px Arial";
    context.fillText(text, x, y);
  context.restore();
}

function draw_circle(x,y,r,context){
      context.save();
        context.beginPath();
        context.arc(x, y, r, 0, 2*Math.PI, false);
        context.fillStyle = '#a1b56c';
        context.fill();
        context.lineWidth = 3;
        context.strokeStyle = '#f7ca88';
        context.stroke();
      context.restore();
}

function draw_line(x0, y0, x1, y1, context) {
  context.save();
    context.beginPath();
    context.moveTo(x0, y0);
    context.lineTo(x1, y1)
    context.stroke();
  context.restore();
}

function deg2rad(degrees) {
      return degrees * Math.PI / 180;
}
function rad2deg(radians) {
      return radians * 180 / Math.PI;
};

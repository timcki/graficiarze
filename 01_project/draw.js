function draw_graph() {
    document.getElementById("result").innerHTML = "";
    document.getElementById(
    const points = gen_points(18);
    draw_edges(points);
    draw_nodes(points);
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

function draw_nodes(points) {
    const canvas = document.getElementById('canvas');
    const context = canvas.getContext('2d');

    const cx = canvas.width / 2;
    const cy = canvas.height / 2;
    const r = 25;

    context.translate(cx, cy);
    points.forEach((val, i, arr) => draw_circle(val[0], val[1], r, context));

}

function draw_edges(points) {
}

function draw_circle(x,y,r,context){
      context.save();
          context.translate(x, y);
          context.beginPath();
          context.arc(0, 0, r, 0, 2*Math.PI, false);
          context.fillStyle = '#a1b56c';
          context.fill();
          context.lineWidth = 3;
          context.strokeStyle = '#f7ca88';
          context.stroke();
      context.restore();
}

function deg2rad(degrees) {
      return degrees * Math.PI / 180;
}
function rad2deg(radians) {
      return radians * 180 / Math.PI;
};

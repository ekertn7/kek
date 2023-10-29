var canvas = document.querySelector("#visualisation");
var ctx = canvas.getContext("2d");
ctx.canvas.width = document.querySelector(".canvasParent").getBoundingClientRect().width;
ctx.canvas.height = document.querySelector(".canvasParent").getBoundingClientRect().height;

// canvas.addEventListener('mousemove', e => {
//     console.log({x:e.offsetX, y:e.offsetY});
// });

// canvas.addEventListener('mousedown', e => {
//     console.log({x:e.offsetX, y:e.offsetY, z:'click'});
// });

// canvas.addEventListener('mouseup', e => {
//     console.log({x:e.offsetX, y:e.offsetY, z:'up'});
// });

function Node(node_name, node_attributes, shape, color_hex, border_hex, size, group_name, x, y) {
    this.name = node_name;
    this.attributes = node_attributes;
    this.shape = shape;
    this.color = color_hex;
    this.border = border_hex;
    this.size = size;
    this.group = group_name;
    this.x = x;
    this.y = y;

    this.draw = function() {
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size/2, 0, 2 * Math.PI, false);
        ctx.fillStyle = this.color;
        ctx.fill();
        ctx.lineWidth = 3;
        ctx.strokeStyle = this.border;
        ctx.stroke();
    };
};

function Edge(edge_name, node_left, node_right, edge_attributes, arrow_style, line_style, color_hex) {
    this.name = edge_name;
    this.attributes = edge_attributes;
    this.arrow_style = arrow_style;
    this.line_style = line_style;
    this.color = color_hex;

    this.node_left = node_left;
    this.node_right = node_right;

    this.left_x = node_left.x;
    this.left_y = node_left.y;
    this.right_x = node_right.x;
    this.right_y = node_right.y;

    this.draw = function() {
        ctx.beginPath();
        ctx.lineWidth = 3;
        ctx.strokeStyle = this.color;
        ctx.moveTo(this.node_left.x, this.node_left.y);
        ctx.lineTo(this.node_right.x, this.node_right.y);
        ctx.stroke();
    };
};

function mouse_down(event) {
    event.preventDefault();
    var index = 0;
    for (var node of nodes) {
        if (is_mouse_on_node(parseInt(event.layerX), parseInt(event.layerY), node)) {
            current_node_index = index;
            is_dragging = true;
            console.log(true);
            return;
        };
        index ++;
    }
};
canvas.onmousedown = mouse_down;

function mouse_up(event) {
    if (!is_dragging) {
        return;
    };
    event.preventDefault();
    is_dragging = false;
};
canvas.onmouseup = mouse_up;

function mouse_out(event) {
    if (!is_dragging) {
        return;
    };
    event.preventDefault();
    is_dragging = false;
    draw_all();
};
canvas.onmouseout = mouse_out;

function mouse_move(event) {
    if (!is_dragging) {
        return;
    } else {
        event.preventDefault();
        nodes[current_node_index].x = parseInt(event.layerX);
        nodes[current_node_index].y = parseInt(event.layerY);
        // for (var edge of edges) {
        //     if (edge.node_left === nodes[current_node_index]) {
        //         edge.node_left = 
        //     } else if (edge.node_right === nodes[current_node_index]) {
        //         edge.right_x = parseInt(event.layerX);
        //         edge.right_y = parseInt(event.layerY);
        //     };
        // };
        draw_all();
    };
};
canvas.onmousemove = mouse_move;

function is_mouse_on_node(x, y, node) {
    var halfSize = node.size/2;
    // console.log({x, y}, {x_s: node.x - halfSize, x_e: node.x + halfSize, y_s: node.y - halfSize, y_e: node.y + halfSize});
    if (x >= (node.x - halfSize) && x <= (node.x + halfSize) && y >= (node.y - halfSize) && y <= (node.y + halfSize)) {
        return true;
    };
    return false;
};

function draw_all() {
    ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
    for (var edge of edges) {
        edge.draw();
    };
    for (var node of nodes) {
        node.draw();
    };
};

// ------------

var e1 = new Edge('e1', n1, n2, {'weight': 150}, 'Default', 'Default', '#555555');
var e2 = new Edge('e1', n1, n3, {'weight': 640}, 'Default', 'Default', '#555555');
// e1.draw();
// e2.draw();
var n0 = new Node('n0', {'label': 'node0'}, 'Circle', '#555555', '#0000FF', 40, 'Group_1', 0, 0);
var n1 = new Node('n1', {'label': 'node1'}, 'Circle', '#555555', '#0000FF', 40, 'Group_1', 160, 70);
var n2 = new Node('n2', {'label': 'node2'}, 'Circle', '#555555', '#FF0000', 40, 'Group_2', 250, 150);
var n3 = new Node('n3', {'label': 'node3'}, 'Circle', '#555555', '#FF0000', 40, 'Group_2', 550, 250);
// n1.draw();
// n2.draw();
// n3.draw();

var current_node_index = 0;
var is_dragging = false;
var edges = [e1, e2];
var nodes = [n0, n1, n2, n3];

draw_all();

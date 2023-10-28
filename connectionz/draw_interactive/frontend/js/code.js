canvas = document.querySelector("#visualisation");
ctx = canvas.getContext("2d");
ctx.canvas.width = document.querySelector(".canvasParent").getBoundingClientRect().width;
ctx.canvas.height = document.querySelector(".canvasParent").getBoundingClientRect().height;

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

    this.draw = function() {
        ctx.beginPath();
        ctx.lineWidth = 3;
        ctx.strokeStyle = this.color;
        ctx.moveTo(this.node_left.x, this.node_left.y);
        ctx.lineTo(this.node_right.x, this.node_right.y);
        ctx.stroke();
    };
};

var e1 = new Edge('e1', n1, n2, {'weight': 150}, 'Default', 'Default', '#555555');
e1.draw();
var n1 = new Node('n1', {'label': 'node1'}, 'Circle', '#00FF00', '#0000FF', 40, 'Group_1', 160, 70);
var n2 = new Node('n2', {'label': 'node2'}, 'Circle', '#00FF00', '#FF0000', 40, 'Group_2', 250, 150);
n1.draw();
n2.draw();



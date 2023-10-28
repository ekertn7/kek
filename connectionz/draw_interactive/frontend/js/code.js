canvas = document.querySelector("#visualisation");
ctx = canvas.getContext("2d");
ctx.canvas.width = document.querySelector(".canvasParent").getBoundingClientRect().width;
ctx.canvas.height = document.querySelector(".canvasParent").getBoundingClientRect().height;

define(function() {
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
});

define(function() {
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
});

var n1 = new Node(node_name='n1', node_attributes={'label': 'node1'}, shape='Circle', color_hex='#555555', border_hex='#0000FF', size=40, group_name='Group_1', x=160, y=70);
var n2 = new Node(node_name='n2', node_attributes={'label': 'node2'}, shape='Circle', color_hex='#555555', border_hex='#FF0000', size=40, group_name='Group_2', x=250, y=150);
n1.draw();
n2.draw();
var e1 = new Edge(edge_name='e1', node_left=n1, node_right=n2, edge_attributes={'weight': 150}, arrow_style='Default', line_style='Default', color_hex='#555555');
e1.draw();

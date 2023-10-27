canvas = document.querySelector("#visualisation");
ctx = canvas.getContext("2d");
ctx.canvas.width = document.querySelector(".canvasParent").getBoundingClientRect().width;
ctx.canvas.height = document.querySelector(".canvasParent").getBoundingClientRect().height;

class Node {
    constructor(node_name, node_attributes, shape, color_hex, border_hex, size, group_name, x, y) {
        this.name = node_name;
        this.attributes = node_attributes;
        this.shape = shape;
        this.color = color_hex;
        this.border = border_hex;
        this.size = size;
        this.group = group_name;
        this.x = x;
        this.y = y;
    };

    draw() {
        ctx.beginPath();
        ctx.arc(100, 100, this.size/2, 0, 2 * Math.PI, false);
        ctx.fillStyle = '#555555';
        ctx.fill();
        ctx.lineWidth = 3;
        ctx.strokeStyle = '#0000FF';
        ctx.stroke();
    };

    sasat() {
        console.log(this.attributes);
    }
};

var n1 = new Node(node_name='kek', node_attributes={'label': 'hui'}, shape='Circle', color_hex='#555555', border_hex='#0000FF', size=40, group_name='Group_1', x=50, y=70);
n1.draw()
n1.sasat()

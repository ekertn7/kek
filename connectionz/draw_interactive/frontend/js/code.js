var canvas = document.querySelector("#visualisation");
var ctx = canvas.getContext("2d");
ctx.canvas.width = document.querySelector(".canvasParent").getBoundingClientRect().width;
ctx.canvas.height = document.querySelector(".canvasParent").getBoundingClientRect().height;
var current_node_index = 0;
var is_dragging = false;
var legend_name = document.querySelector("#legend_name");
var legend_attribute = document.querySelector("#legend_attribute");
var legend_group = document.querySelector("#legend_group");

var graph = {
    "info":
        {
            "directed": true,
            "layout": "Circle",
            "groups": [
                {
                    "group_name": "Group_1",
                    "group_color": "#0000FF"
                },
                {
                    "group_name": "Group_2",
                    "group_color": "#00FF00"
                },
                {
                    "group_name": "Group_3",
                    "group_color": "#FF0000"
                },
            ]
        }, 
    "nodes":
        [
            {
                "node_name": "n1",
                "node_attributes": {"label": "Андрей"},
                "shape": "Circle",
                "color": "#424242",
                "group": "Group_2",
                "position": {"x": 160, "y": 70},
                "size": 50
            },
            {
                "node_name": "n2",
                "node_attributes": {"label": "Борис"},
                "shape": "Circle",
                "color": "#797979",
                "group": "Group_2",
                "position": {"x": 250, "y": 150},
                "size": 40
            },
            {
                "node_name": "n3",
                "node_attributes": {"label": "Виктор"},
                "shape": "Circle",
                "color": "#AAAAAA",
                "group": "Group_2",
                "position": {"x": 320, "y": 245},
                "size": 30
            },
            {
                "node_name": "n4",
                "node_attributes": {"label": "Глеб"},
                "shape": "Circle",
                "color": "#AAAAAA",
                "group": "Group_2",
                "position": {"x": 410, "y": 120},
                "size": 30
            },
            {
                "node_name": "n5",
                "node_attributes": {"label": "Дмитрий"},
                "shape": "Circle",
                "color": "#AAAAAA",
                "group": "Group_1",
                "position": {"x": 730, "y": 320},
                "size": 30
            },
            {
                "node_name": "n6",
                "node_attributes": {"label": "Евгений"},
                "shape": "Circle",
                "color": "#AAAAAA",
                "group": "Group_3",
                "position": {"x": 700, "y": 70},
                "size": 30
            },
            {
                "node_name": "n7",
                "node_attributes": {"label": "Илья"},
                "shape": "Circle",
                "color": "#AAAAAA",
                "group": "Group_3",
                "position": {"x": 800, "y": 140},
                "size": 30
            },
            {
                "node_name": "n8",
                "node_attributes": {"label": "Константин"},
                "shape": "Circle",
                "color": "#AAAAAA",
                "group": "Group_1",
                "position": {"x": 280, "y": 500},
                "size": 30
            },
            {
                "node_name": "n9",
                "node_attributes": {"label": "Лев"},
                "shape": "Circle",
                "color": "#AAAAAA",
                "group": "Group_1",
                "position": {"x": 330, "y": 380},
                "size": 30
            },
            {
                "node_name": "n10",
                "node_attributes": {"label": "Михаил"},
                "shape": "Circle",
                "color": "#797979",
                "group": "Group_1",
                "position": {"x": 505, "y": 430},
                "size": 40
            },
            {
                "node_name": "n11",
                "node_attributes": {"label": "Никита"},
                "shape": "Circle",
                "color": "#AAAAAA",
                "group": "Group_2",
                "position": {"x": 40, "y": 120},
                "size": 30
            },
        ],
    "edges":
        [
            {
                "edge_name": "e1",
                "node_left": "n1",
                "node_right": "n2",
                "edge_attributes": {"weight": 150},
                "arrow_style": "Default",
                "line_style": "Default",
                "color": "#000000"
            },
            {
                "edge_name": "e2",
                "node_left": "n6",
                "node_right": "n7",
                "edge_attributes": {"weight": 150},
                "arrow_style": "Default",
                "line_style": "Default",
                "color": "#000000"
            },
            {
                "edge_name": "e3",
                "node_left": "n1",
                "node_right": "n4",
                "edge_attributes": {"weight": 150},
                "arrow_style": "Default",
                "line_style": "Default",
                "color": "#000000"
            },
            {
                "edge_name": "e4",
                "node_left": "n10",
                "node_right": "n5",
                "edge_attributes": {"weight": 150},
                "arrow_style": "Default",
                "line_style": "Default",
                "color": "#000000"
            },
            {
                "edge_name": "e5",
                "node_left": "n2",
                "node_right": "n3",
                "edge_attributes": {"weight": 150},
                "arrow_style": "Default",
                "line_style": "Default",
                "color": "#000000"
            },
            {
                "edge_name": "e6",
                "node_left": "n1",
                "node_right": "n11",
                "edge_attributes": {"weight": 150},
                "arrow_style": "Default",
                "line_style": "Default",
                "color": "#000000"
            },
            {
                "edge_name": "e7",
                "node_left": "n9",
                "node_right": "n10",
                "edge_attributes": {"weight": 150},
                "arrow_style": "Default",
                "line_style": "Default",
                "color": "#000000"
            },
            {
                "edge_name": "e8",
                "node_left": "n8",
                "node_right": "n10",
                "edge_attributes": {"weight": 150},
                "arrow_style": "Default",
                "line_style": "Default",
                "color": "#000000"
            },
        ]
};

function draw(node_for_draw_border) {
    ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
    for (var edge of graph["edges"]) {
        ctx.beginPath();
        ctx.lineWidth = 2;
        ctx.strokeStyle = edge["color"];
        var left_x;
        var left_y;
        var right_x;
        var right_y;
        for (var node of graph["nodes"]) {
            if (node["node_name"] == edge["node_left"]) {
                left_x = node["position"]["x"];
                left_y = node["position"]["y"];
            };
            if (node["node_name"] == edge["node_right"]) {
                right_x = node["position"]["x"];
                right_y = node["position"]["y"];
            };
        };
        ctx.moveTo(left_x, left_y);
        ctx.lineTo(right_x, right_y);
        ctx.stroke();
    };
    for (var node of graph["nodes"]) {
        ctx.beginPath();
        ctx.arc(node["position"]["x"], node["position"]["y"], node["size"]/2, 0, 2 * Math.PI, false);
        ctx.fillStyle = node["color"];
        ctx.fill();
        ctx.lineWidth = 4;
        var group_color = "#000000";
        for (var group of graph["info"]["groups"]) {
            if (group["group_name"] == node["group"]) {
                group_color = group["group_color"];
            };
        };
        ctx.strokeStyle = group_color;
        ctx.stroke();

        ctx.fillStyle = "#000000";
        // ctx.font = "16px Arial";
        ctx.textAlign = "center";
        ctx.textBaseline = "top";
        ctx.fillText((node["node_attributes"]["label"]) ? node["node_attributes"]["label"] : node["node_name"], node["position"]["x"], node["position"]["y"] + node["size"]/2 + 8);
    };
    if (node_for_draw_border) {
        ctx.beginPath();
        ctx.roundRect(node_for_draw_border["position"]["x"] - node_for_draw_border["size"]/2 - 5, node_for_draw_border["position"]["y"] - node_for_draw_border["size"]/2 - 5, node_for_draw_border["size"] + 10, node_for_draw_border["size"] + 10, 4);
        ctx.lineWidth = 2;
        ctx.strokeStyle = "#EB801E";
        ctx.stroke();
    };
};

function mouse_down(event) {
    event.preventDefault();
    var index = 0;
    for (var node of graph["nodes"]) {
        if (is_mouse_on_node(parseInt(event.layerX), parseInt(event.layerY), node)) {
            current_node_index = index;
            is_dragging = true;
            console.log(true);
            legend_name.innerHTML = node["node_name"];
            legend_attribute.innerHTML = JSON.stringify(node["node_attributes"]);
            legend_group.innerHTML = node["group"];
            draw(graph["nodes"][current_node_index]);
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
};
canvas.onmouseout = mouse_out;

function mouse_move(event) {
    if (!is_dragging) {
        return;
    } else {
        event.preventDefault();
        graph["nodes"][current_node_index]["position"]["x"] = parseInt(event.layerX);
        graph["nodes"][current_node_index]["position"]["y"] = parseInt(event.layerY);
        draw(graph["nodes"][current_node_index]);
    };
};
canvas.onmousemove = mouse_move;

function is_mouse_on_node(x, y, node) {
    var halfSize = node["size"]/2;
    if (x >= (node["position"]["x"] - halfSize) && x <= (node["position"]["x"] + halfSize) && y >= (node["position"]["y"] - halfSize) && y <= (node["position"]["y"] + halfSize)) {
        return true;
    };
    return false;
};

// -------------------

draw();

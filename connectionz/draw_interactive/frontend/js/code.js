var canvas = document.querySelector("#visualisation");
var ctx = canvas.getContext("2d");
ctx.canvas.width = document.querySelector(".canvasParent").getBoundingClientRect().width;
ctx.canvas.height = document.querySelector(".canvasParent").getBoundingClientRect().height;
var current_node_index = 0;
var is_dragging = false;
var legend_name = document.querySelector("#legend_name");
var legend_attribute = document.querySelector("#legend_attribute");
var legend_group = document.querySelector("#legend_group");

// console.log({'graph': graph});

if (!graph["info"]["show_nodes_without_groups"]) {
    for (var node of graph["nodes"]) {
        if (!node["group_name"]) {
            graph["nodes"].splice(graph["nodes"].indexOf(node), 1, null);
            // console.log({'node_without_group': graph["nodes"].indexOf(node), 'gname': node["group_name"]});
        };
    };
    graph["nodes"] = graph["nodes"].filter(function (el) {return el != null;});
    console.log(graph["nodes"]);
    for (var edge of graph["edges"]) {
        console.log(graph["nodes"][edge["node_left"]]);
    };
};

function draw(node_for_draw_border) {
    ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
    for (var edge of graph["edges"]) {
        // edge
        ctx.beginPath();
        ctx.lineWidth = 2;
        ctx.strokeStyle = edge["color_hex"];
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
    // test triangle
    // ctx.beginPath();
    // ctx.lineWidth = 2;
    // ctx.strokeStyle = "#000000";
    // ctx.moveTo(100, 100);
    // ctx.lineTo(105, 110);
    // ctx.moveTo(100, 100);
    // ctx.lineTo(95, 110);
    // ctx.stroke();
    // --
    for (var node of graph["nodes"]) {
        // node
        if (node != graph["nodes"][current_node_index]) {
            ctx.beginPath();
            ctx.arc(node["position"]["x"], node["position"]["y"], node["size"]/2, 0, 2 * Math.PI, false);
            ctx.fillStyle = node["color_hex"];
            ctx.fill();
            ctx.lineWidth = 4;
            var group_color = "#000000";
            for (var group of graph["info"]["groups"]) {
                if (group["group_name"] == node["group_name"]) {
                    group_color = group["group_color_hex"];
                };
            };
            ctx.strokeStyle = group_color;
            ctx.stroke();
            // text
            ctx.fillStyle = "#000000";
            // ctx.font = "16px Arial";
            ctx.textAlign = "center";
            if (graph["info"]["nodes_label"]) {
                if (graph["info"]["nodes_label_align"] == "bottom") {
                    ctx.textBaseline = "top";
                    ctx.fillText((node["node_attributes"]["label"]) ? node["node_attributes"]["label"] : node["node_name"], node["position"]["x"], node["position"]["y"] + node["size"]/2 + 8);
                } else if (graph["info"]["nodes_label_align"] == "top") {
                    ctx.textBaseline = "bottom";
                    ctx.fillText((node["node_attributes"]["label"]) ? node["node_attributes"]["label"] : node["node_name"], node["position"]["x"], node["position"]["y"] - node["size"]/2 - 8);
                };
            };
        };
    };
    // draw selected node
    selected_node = graph["nodes"][current_node_index]
    ctx.beginPath();
    ctx.arc(selected_node["position"]["x"], selected_node["position"]["y"], selected_node["size"]/2, 0, 2 * Math.PI, false);
    ctx.fillStyle = selected_node["color_hex"];
    ctx.fill();
    ctx.lineWidth = 4;
    var group_color = "#000000";
    for (var group of graph["info"]["groups"]) {
        if (group["group_name"] == selected_node["group_name"]) {
            group_color = group["group_color_hex"];
        };
    };
    ctx.strokeStyle = group_color;
    ctx.stroke();
    // text
    ctx.fillStyle = "#000000";
    // ctx.font = "16px Arial";
    ctx.textAlign = "center";
    if (graph["info"]["nodes_label"]) {
        if (graph["info"]["nodes_label_align"] == "bottom") {
            ctx.textBaseline = "top";
            ctx.fillText((selected_node["node_attributes"]["label"]) ? selected_node["node_attributes"]["label"] : selected_node["node_name"], selected_node["position"]["x"], selected_node["position"]["y"] + selected_node["size"]/2 + 8);
        } else if (graph["info"]["nodes_label_align"] == "top") {
            ctx.textBaseline = "bottom";
            ctx.fillText((selected_node["node_attributes"]["label"]) ? selected_node["node_attributes"]["label"] : selected_node["node_name"], selected_node["position"]["x"], selected_node["position"]["y"] - selected_node["size"]/2 - 8);
        };
    };
    //--
    if (node_for_draw_border) {
        // active border
        ctx.beginPath();
        ctx.roundRect(node_for_draw_border["position"]["x"] - node_for_draw_border["size"]/2 - 5, node_for_draw_border["position"]["y"] - node_for_draw_border["size"]/2 - 5, node_for_draw_border["size"] + 10, node_for_draw_border["size"] + 10, 8);
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
            legend_group.innerHTML = (node["group_name"]) ? node["group_name"] : "Без группы";

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

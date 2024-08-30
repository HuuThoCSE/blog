# Trang Chủ

# Graph View

<div id="mynetwork"></div>

<script type="text/javascript" src="https://unpkg.com/vis-network@9.1.2/dist/vis-network.min.js"></script>
<link href="https://unpkg.com/vis-network@9.1.2/styles/vis-network.min.css" rel="stylesheet" type="text/css" />

<script type="text/javascript">
// Load graph data from JSON file
fetch('/graph_data.json')
  .then(response => response.json())
  .then(data => {
    const uniqueNodes = new Map();
    const nodes = [];
    const edges = [];

    data.nodes.forEach(node => {
      if (!uniqueNodes.has(node.id)) {
        uniqueNodes.set(node.id, true);
        nodes.push(node);
      }
    });

    data.edges.forEach(edge => {
      edges.push(edge);
    });

    const container = document.getElementById('mynetwork');
    const graphData = {
      nodes: new vis.DataSet(nodes),
      edges: new vis.DataSet(edges)
    };

    const options = {
      nodes: {
        shape: 'dot',
        size: 20
      },
      edges: {
        arrows: 'to'
      },
      physics: {
        enabled: true
      }
    };

    new vis.Network(container, graphData, options);
  })
  .catch(error => console.error('Error loading graph data:', error));
</script>

<style>
#mynetwork {
  width: 100%;
  height: 600px;
  border: 1px solid lightgray;
}
</style>

# 23_24_HK1
[TH1383 - Blockchain](blockchain/lecture.md)

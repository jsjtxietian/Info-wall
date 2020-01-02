import React from "react";
import Graphin, { Utils } from "@antv/graphin";

import "@antv/graphin/dist/index.css";

const NodeExpand = () => {
    const [state, setState] = React.useState({
        selected: [],
        data: Utils.mock(5).graphin()
    });

    const { data, selected } = state;
    const graphRef = React.createRef(null);
    React.useEffect(() => {
        const { graph } = graphRef.current;
        const onNodeClick = e => {
            console.log("node:click", e);
            setState({
                ...state,
                selected: [e.item.get("model")]
            });
        };
        graph.on("node:click", onNodeClick);
        return () => {
            graph.off("node:click", onNodeClick);
        };
    }, [state]);

    const onExpand = () => {
        const count = 5;
        const expandData = Utils.mock(count)
            .expand(selected)
            .graphin();
        setState({
            ...state,
            data: {
                nodes: [...state.data.nodes, ...expandData.nodes],
                edges: [...state.data.edges, ...expandData.edges]
            }
        });
    };
    return (
        <div className="App">
            <button onClick={onExpand}>Node Expand</button>
            <Graphin data={data} layout={{ name: "concentric" }} ref={graphRef} />
        </div>
    );
};

export default NodeExpand;
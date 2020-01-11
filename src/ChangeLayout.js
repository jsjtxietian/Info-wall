import React from "react";
import Graphin, { Utils } from "@antv/graphin";
import { Toolbar } from "@antv/graphin-components";
import LayoutSelector from "./layout-selector";
import { ContextMenu } from "@antv/graphin-components";
import "@antv/graphin/dist/index.css";
import "@antv/graphin-components/dist/index.css";
import "./App.css";

const options = [
	{
		key: "deleteNode",
		title: "Delete",
		visible: true,
		iconType: "delete",
		onClick: () => {
			console.log("deleted");
		}
	},
	{
		key: "invertSelect",
		title: "Invert Select",
		iconType: "select",
		visible: true,
		onClick: () => { }
	}
];


const data = Utils.mock(100)
	.random(2.5)
	.graphin();


console.log(JSON.stringify(data));

const ChangeLayout = () => {
	const [layout, changeLayout] = React.useState({ name: "force", options: {} });
	return (
		<div className="App">
			<Graphin data={data} layout={layout}>
				<LayoutSelector
					value={layout.name}
					onChange={value => {
						changeLayout({
							...layout,
							name: value
						});
					}}
				/>
				<Toolbar />
				<ContextMenu options={options} />
			</Graphin>
		</div>
	);
};


export default ChangeLayout;
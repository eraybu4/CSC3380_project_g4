/**
* starRender.js
* Renders the constellations in all of the inner boxes. 
*/

	const boxes = document.querySelectorAll('.box1_inner, .box2_inner, .box3_inner');

	boxes.forEach(function(box){
		
		const svg = box.querySelector('svg');
		const stars = Array.from(box.querySelectorAll('.star'));

	/**
	* Creates and appends the lines to the SVG. 
	* Wipes any pre-existing elements before appending any new ones. 
	*/
		 function createLines() {
			while (svg.firstChild) svg.removeChild(svg.firstChild);
			const needed = stars.length - 1

			for (let i = 0; i < needed; i++) {
			const ln = document.createElementNS('http://www.w3.org/2000/svg', 'line');
			ln.setAttribute('id', 'lineNumber' + (i+1));
			svg.appendChild(ln);
    		}
  		 }

	/**
	* Gets the position and size of the element and SVG.
	* Uses them to calculate the center of the star PNG. 
	*/
		 function centerOf(element) {
			const svgRect = svg.getBoundingClientRect();
			const r = element.getBoundingClientRect();
			return {
			x: (r.left - svgRect.left) + r.width / 2,
			y: (r.top  - svgRect.top)  + r.height / 2
			};
		 }

	/**
	* Renders the connecting lines using the center coordinates of two stars at a time.
	* Sets those center coordinates as the start and endpoint of the line.
	*/
		 function updateLines() {
			const lines = Array.from(svg.querySelectorAll('line'));
			for (let i = 0; i < lines.length; i++) {
			const a = centerOf(stars[i]);
			const b = centerOf(stars[i+1]);
			const ln = lines[i];
			ln.setAttribute('x1', a.x);
			ln.setAttribute('y1', a.y);
			ln.setAttribute('x2', b.x);
			ln.setAttribute('y2', b.y);
    		}
  		 }

			createLines();
			updateLines();

			window.addEventListener('resize', updateLines);


	});

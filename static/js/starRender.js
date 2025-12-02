
	const boxes = document.querySelectorAll('.box1_inner, .box2_inner, .box3_inner');

	boxes.forEach(function(box){
		
		const svg = box.querySelector('svg');
		const stars = Array.from(box.querySelectorAll('.star'));


		 function createLines() {
			while (svg.firstChild) svg.removeChild(svg.firstChild);
			const needed = stars.length - 1

			for (let i = 0; i < needed; i++) {
			const ln = document.createElementNS('http://www.w3.org/2000/svg', 'line');
			ln.setAttribute('id', 'lineNumber' + (i+1));
			svg.appendChild(ln);
    		}
  		 }

		 function centerOf(element) {
			const svgRect = svg.getBoundingClientRect();
			const r = element.getBoundingClientRect();
			return {
			x: (r.left - svgRect.left) + r.width / 2,
			y: (r.top  - svgRect.top)  + r.height / 2
			};
		 }

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
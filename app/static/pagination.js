




document.addEventListener('DOMContentLoaded', function() {
	
		var curr = document.querySelector(".pagination").dataset.curr;
		var plen = document.querySelector(".pagination").dataset.pagelen;

		if (curr == 1) {
			
			document.querySelector("#page_prev").hidden = true;
		}

		if (curr == plen) {
			
			document.querySelector("#page_next").hidden = true;
		}
	}
);
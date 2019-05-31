document.addEventListener('DOMContentLoaded', function() {

 	document.querySelectorAll('.glyphicon.glyphicon-chevron-up').forEach(function(upbutton) {
		let id = upbutton.id;
		

		if(localStorage.getItem(id)){
			if(localStorage.getItem(id) == "up"){
				
				upbutton.style.color = "#337ab7";
				upbutton.dataset.state = "up";

			}		
			
		}
		else{
			localStorage.setItem(id, "down");
		}

    });

 	document.querySelectorAll('.glyphicon.glyphicon-chevron-down').forEach(function(downbutton) {
		let id = downbutton.id;
		
		//alert(id);

		if(localStorage.getItem(id)){
			if(localStorage.getItem(id) == "up"){
				
				downbutton.style.color = "#337ab7";
				downbutton.dataset.state = "up";

			}		
			
		}
		else{
			localStorage.setItem(id, "down");
		}

    });

});
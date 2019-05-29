



document.addEventListener('DOMContentLoaded', function() {

	try{
		var val = document.querySelector("p").dataset.cntry;
		var abrev = document.querySelector("p").dataset.abrev;
		var country = document.querySelector("p").dataset.full_cntry;
		if(val == "true"){
			document.querySelector('#dropdownMenuButton').innerHTML = `<span class="flag-icon flag-icon-${abrev}"></span> ${country}`;
		}
	}
	catch(err){

	}

}

);


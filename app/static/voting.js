function upvote(upbutton){

	var id = upbutton.dataset.postid;

	if (upbutton.dataset.state == "down"){
		upbutton.style.color = "#337ab7";
		upbutton.dataset.state = "up";
		localStorage.setItem(`up_${id}`, "up");

		var downbutton = document.querySelector(`#down_${id}`);

		if(downbutton.dataset.state == "up"){

			downbutton.style.color = "#333";
			downbutton.dataset.state = "down";
			localStorage.setItem(`down_${id}`, "down");
		}

	}
	else{
		upbutton.style.color = "#333";
		upbutton.dataset.state = "down";
		localStorage.setItem(`up_${id}`, "down");
	}
	
}

function downvote(downbutton){

	var id = downbutton.dataset.postid;

	if (downbutton.dataset.state == "down"){
		downbutton.style.color = "#337ab7";
		downbutton.dataset.state = "up";
		localStorage.setItem(`down_${id}`, "up");

		var upbutton = document.querySelector(`#up_${id}`);

		if(upbutton.dataset.state == "up"){

			upbutton.style.color = "#333";
			upbutton.dataset.state = "down";
			localStorage.setItem(`up_${id}`, "down");
		}
	}
	else{
		downbutton.style.color = "#333";
		downbutton.dataset.state = "down";
		localStorage.setItem(`down_${id}`, "down");
	}


	
}

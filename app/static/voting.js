function upvote(upbutton){

	var id = document.querySelector(".post-border.post-back").dataset.post_id;

	if (upbutton.dataset.state == "down"){
		upbutton.style.color = "#337ab7";
		upbutton.dataset.state = "up";

		var downbutton = document.querySelector(`#down_${id}`);

		if(downbutton.dataset.state == "up"){

			downbutton.style.color = "#333";
			downbutton.dataset.state = "down";
		}

	}
	else{
		upbutton.style.color = "#333";
		upbutton.dataset.state = "down";
	}
	
}

function downvote(downbutton){

	var id = document.querySelector(".post-border.post-back").dataset.post_id;

	if (downbutton.dataset.state == "down"){
		downbutton.style.color = "#337ab7";
		downbutton.dataset.state = "up";

		var upbutton = document.querySelector(`#up_${id}`);

		if(upbutton.dataset.state == "up"){

			upbutton.style.color = "#333";
			upbutton.dataset.state = "up";
		}
	}
	else{
		downbutton.style.color = "#333";
		downbutton.dataset.state = "down";
	}


	
}
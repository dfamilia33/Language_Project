function upvote(upbutton){

	var id = upbutton.dataset.postid;

	const request = new XMLHttpRequest();
    var op;
    request.open('POST', '/voting');

	if (upbutton.dataset.state == "down"){
		op ='+'

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
		op = '-'
		upbutton.style.color = "#333";
		upbutton.dataset.state = "down";
		localStorage.setItem(`up_${id}`, "down");
	}
    
    request.onload = () => {

        // Extract JSON data from request
        const data = JSON.parse(request.responseText);

        // Update the result div
        if (data.success) {
    		alert(data.value);
            document.querySelector(`#uptext_${id}`).innerHTML = `${data.value}`;
        }
    }
 

	// Add data to send with request
    const data = new FormData();
    data.append('operation', op);
    data.append('id', parseInt(id));

    // Send request
    request.send(data);
	
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

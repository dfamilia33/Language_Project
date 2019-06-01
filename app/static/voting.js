function upvote(upbutton){

	var id = upbutton.dataset.postid;

	const request = new XMLHttpRequest();
    var op;
 	var downstate;
    request.open('POST', '/voting');
    var dec_up = false;

	if (upbutton.dataset.state == "down"){
		op ='+';

		upbutton.style.color = "#337ab7";
		upbutton.dataset.state = "up";
		localStorage.setItem(`up_${id}`, "up");

		var downbutton = document.querySelector(`#down_${id}`);
		downstate = downbutton.dataset.state;

		if(downbutton.dataset.state == "up"){
			dec_up = true;
			downbutton.style.color = "#333";
			downbutton.dataset.state = "down";
			localStorage.setItem(`down_${id}`, "down");
		}


	}
	else{
		op = '-';
		upbutton.style.color = "#333";
		upbutton.dataset.state = "down";
		localStorage.setItem(`up_${id}`, "down");
	}
    
    request.onload = () => {

        // Extract JSON data from request
        const data = JSON.parse(request.responseText);

        // Update the result div
        if (data.success) {
    		//alert(data.value);
            document.querySelector(`#uptext_${id}`).innerHTML = `${data.upvalue}`;

            if (dec_up) {
            	document.querySelector(`#downtext_${id}`).innerHTML = `${data.downvalue}`;
            }


        }
    }
 

	// Add data to send with request
    const data = new FormData();
    data.append('operation', op);
    data.append('id', parseInt(id));
    data.append('type', 'upvote');
    data.append('state', downstate);

    // Send request
    request.send(data);
	
}

function downvote(downbutton){

	var id = downbutton.dataset.postid;

	const request = new XMLHttpRequest();
    var op;
 	var upstate;
    request.open('POST', '/voting');
    var dec_up = false;



	if (downbutton.dataset.state == "down"){
		op ='+';
		downbutton.style.color = "#337ab7";
		downbutton.dataset.state = "up";
		localStorage.setItem(`down_${id}`, "up");

		var upbutton = document.querySelector(`#up_${id}`);
		upstate = upbutton.dataset.state;

		if(upbutton.dataset.state == "up"){
			dec_up = true;

			upbutton.style.color = "#333";
			upbutton.dataset.state = "down";
			localStorage.setItem(`up_${id}`, "down");
		}
	}
	else{
		op = '-';
		downbutton.style.color = "#333";
		downbutton.dataset.state = "down";
		localStorage.setItem(`down_${id}`, "down");
	}

    request.onload = () => {

        // Extract JSON data from request
        const data = JSON.parse(request.responseText);

        // Update the result div
        if (data.success) {
    		//alert(data.value);
            document.querySelector(`#downtext_${id}`).innerHTML = `${data.downvalue}`;

            if (dec_up) {
            	
            	document.querySelector(`#uptext_${id}`).innerHTML = `${data.upvalue}`;
            }


        }
    }
 

	// Add data to send with request
    const data = new FormData();
    data.append('operation', op);
    data.append('id', parseInt(id));
    data.append('type', 'downvote');
    data.append('state', upstate);

    // Send request
    request.send(data);	


	
}

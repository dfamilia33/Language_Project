document.addEventListener('DOMContentLoaded', () => {

    document.querySelector('#sugbox').onsubmit = () => {

    	
/*    	block_to_insert = document.createElement('div');
    	block_to_insert.innerHTML = 'Your request has been submitted - Thank you!';
    	container_block = document.getElementById('alertdiv');
    	container_block.setAttribute("class", "alert alert-success");
    	container_block.setAttribute("role", "alert");
    	container_block.appendChild(block_to_insert);*/
    	
    	const request = new XMLHttpRequest();
        request.open('POST', '/suggestpost');



    	var word = document.querySelector('#wordsug').value;
    	var sel = document.getElementById('countrysug');

    	var i;
		var countstring = "";

		for(i of sel.options){
			if(i.selected == true){
		        countstring += i.value+ "," ;

		    }
		}
		
		countstring = countstring.substring(0, countstring.length - 1);

		var definition = document.getElementById('defsug').value;
		var sentence = document.getElementById('sensug').value

    	

        request.onload = () => {

            // Extract JSON data from request
            const data = JSON.parse(request.responseText);

            // Update the result div
            if (data.success) {
               alert("Your request has been submitted - Thank you!");
            }
            else {
                alert("There was an error submitting your request - please contact the admin");
            }
        }




    	// Add data to send with request
        const data = new FormData();
        data.append('word', word);
        data.append('countries', countstring);
        data.append('definition', definition);
        data.append('sentence', sentence);

        // Send request
        request.send(data);




    };

});

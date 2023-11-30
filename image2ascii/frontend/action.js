async function SubmitVars() {

    // data sent from the POST request
    var formData = new FormData()

    const fileInput = document.querySelector('input[type="file"]');
    const file = fileInput.files[0];

    formData.append('file',file)

    const response = await fetch('http://127.0.0.1:8080/say/upload/', {
    method: "POST",
    body: formData,
    headers: { "accept": "application/json", "Content-type": "multipart/form-data; charset=UTF-8"}
  })

  const responseText = await response.text();
  console.log(responseText); // logs 'OK'
  var index_page = document.getElementById("answer"); 
  index_page.style.color = "blue"; 
  if(JSON.stringify(responseText).indexOf('overlap') > -1){index_page.style.color = "red"};
  index_page.innerHTML = (responseText);
}
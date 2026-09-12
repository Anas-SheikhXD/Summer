document.getElementById("fetchButton").addEventListener("click", function() {
    fetch("https://dog.ceo/api/breeds/image/random")
        .then(response => response.json())
        .then(data => {
            document.getElementById("output").innerHTML = `<img src="${data.message}" width="300">`;
        });
});
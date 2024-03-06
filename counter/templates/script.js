import api from views.py

function handleClick() {
    var name = document.getElementById("name");
    name.innerText = api.name;
        
}

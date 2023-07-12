is_shown = false;

document.getElementById('loadMore').addEventListener('click', function() {
if(is_shown == false){
    show();
}else{
close();
}


});

function show(){
    document.getElementById('extraContent').style.height = '500px';
    document.getElementById('extraContent').style.opacity = '1';
    document.getElementById('loadMore').textContent = 'Show Less';
    is_shown = true;
}
function close(){
    document.getElementById('extraContent').style.height = '0';
    document.getElementById('extraContent').style.opacity = '0';
    document.getElementById('loadMore').textContent = 'Show More';
    is_shown = false;
}



// search js

const searchBtn = document.querySelector(".search-btn");
const cancelBtn = document.querySelector(".cancel-btn");
const searchBox = document.querySelector(".search-box");

searchBtn.onclick = () => {
    searchBox.classList.add("active");
}

cancelBtn.onclick = () => {
    searchBox.classList.remove("active");
}